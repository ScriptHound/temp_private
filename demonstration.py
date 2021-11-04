import requests


def upload_image():
    image = open("test_data/test_image.jpg", 'rb')
    response = requests.post(
        "http://localhost:8888/upload", files={"image": image.read()})
    return response


def get_image():
    response = upload_image()
    img_id = response.json().get("pic_id")
    response = requests.get(f"http://localhost:8888/get?pic_id={img_id}")
    print(response.content)
    print(response.status_code)
    print(response.headers)


if __name__ == "__main__":
    get_image()
