from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def upload_image():
    image = open("test_data/test_image.jpg", 'rb')
    response = client.post(
        "/upload", files={"image": image.read()})
    return response


def test_image_upload():
    response = upload_image()
    assert response.status_code == 200
    assert response.json().get("pic_id")


def test_image_download():
    img_id = upload_image()
    img_id = img_id.json().get("pic_id")
    response = client.get(f"/get/?pic_id={img_id}")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "image/jpeg"
