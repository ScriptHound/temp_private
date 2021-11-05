from fastapi.testclient import TestClient
import pytest
from httpx import AsyncClient

from main import app

client = TestClient(app)


def upload_image():
    image = open("test_data/test_image.jpg", 'rb')
    response = client.post(
        "/upload", files={"image": image.read()})
    image.close()
    return response


def test_image_upload():
    response = upload_image()
    assert response.status_code == 200
    assert response.json().get("pic_id")


# @pytest.mark.anyio
# @pytest.mark.skip # not implemented yet
# async def test_image_download():
#     img_id = upload_image()
#     img_id = img_id.json().get("pic_id")
#     async with AsyncClient(app=app, base_url='http://localhost') as client:
#         response = await client.get(f"/get/?pic_id={img_id}")
#     assert response.status_code == 200
#     assert response.headers["Content-Type"] == "image/jpeg"
