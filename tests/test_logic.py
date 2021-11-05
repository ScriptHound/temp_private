from PIL import Image

from main_app.logic import scale_image, image_difference


def test_scale_image():
    """
    Test the scale_image function
    """
    with open("test_data/test_scale.jpg", 'rb') as my_image:
        original_image = Image.open(my_image)
        original_image_width, original_image_height = original_image.size
        scale_ratio = 0.5

        expected_width = int(original_image_width * scale_ratio)
        expected_height = int(original_image_height * scale_ratio)

        scaled_image = scale_image(my_image, scale_ratio)
        scaled_image_width, scaled_image_height = scaled_image.size

        is_height_scaled = scaled_image_height == expected_height
        is_width_scaled = scaled_image_width == expected_width

        assert is_height_scaled or is_width_scaled


def test_image_similarity():
    """
    Test the image_similarity function
    """
    original_image = Image.open("test_data/test_scale.jpg")
    image_2 = Image.open("test_data/test_scale.jpg")

    similarity = image_difference(original_image, image_2)

    assert similarity == 0


def test_image_similarity_different():
    """
    Test the image_similarity function
    """
    original_image = Image.open("test_data/test_scale.jpg")
    image_2 = Image.open("test_data/return_test.jpg")

    similarity = image_difference(original_image, image_2)

    assert similarity > 0
