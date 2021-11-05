from uuid import uuid4
import uuid

from PIL import Image
import imagehash
from sqlalchemy.future import select

from main_app.models import Image as ImageModel


def check_ratio_equality(image, another_image):
    image_width = image.size[0]
    image_height = image.size[1]
    image_size_ratio = round(image_width / image_height, 2)

    another_image_width = another_image.size[0]
    another_image_height = another_image.size[1]
    another_image_size_ratio = round(another_image_width / another_image_height, 2)

    return image_size_ratio == another_image_size_ratio


def is_image_bigger(image, another_image):
    image_width = image.size[0]
    image_height = image.size[1]

    another_image_width = another_image.size[0]
    another_image_height = another_image.size[1]
    if another_image_width > image_width or another_image_height > image_height:
        return True


async def search_similar_image(original_image, session):
    images = select(ImageModel.path, ImageModel.uuid)
    images = await session.execute(images)
    images = list(images)
    if len(images) == 0:
        return None, None

    for path, uuid in images:
        image = Image.open(path)
        difference = image_difference(original_image, image)

        if difference < 10:
            is_ratio_equal = check_ratio_equality(original_image, image)
            if is_ratio_equal:
                if is_image_bigger(image, original_image):
                    original_image.save(image.filename)

                return path, uuid
    return None, None


def image_difference(original: Image, another: Image):
    original_hash = imagehash.phash(original)
    another_hash = imagehash.phash(another)

    difference = original_hash - another_hash
    
    return difference


def scale_image(file, factor):
    im = Image.open(file)
    height, width = im.size
    new_height = int(height * factor)
    new_width = int(width * factor)
    im.thumbnail((new_height, new_width))
    return im


async def create_image(session, directory):
    uuid = str(uuid4())
    filepath = f'{directory}/{uuid}.jpg'
    image = ImageModel(uuid=uuid, path=filepath)

    session.add(image)
    await session.commit()
    return uuid


async def get_image(session, uuid):
    image = select(ImageModel.path)\
        .where(ImageModel.uuid == uuid)
    image = await session.execute(image)
    image = list(image)
    if len(image) == 0:
        return None
    image = image[0][0]
    await session.commit()

    return image


async def get_all_uuids(session):
    uuids = select(ImageModel.uuid)
    uuids = await session.execute(uuids)
    uuids = list(uuids)

    return uuids
