from uuid import uuid4

from PIL import Image
from sqlalchemy.future import select

from main_app.models import Image as ImageModel


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
