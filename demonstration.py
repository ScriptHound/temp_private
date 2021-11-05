import argparse

import requests


def upload_image(address, port):
    image = open("test_data/test_image.jpg", 'rb')
    response = requests.post(
        f"http://{address}:{port}/upload", files={"image": image.read()})
    print(response.json())
    return response


def get_image(address, port):
    response = upload_image(address, port)
    img_id = response.json().get("pic_id")
    response = requests.get(f"http://{address}:{port}/get?pic_id={img_id}")
    print(response.status_code)
    print(response.headers)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--address", default="localhost")
    parser.add_argument("--port", default=8888)
    args = parser.parse_args()

    port = args.port
    address = args.address

    get_image(address, port)
