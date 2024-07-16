import base64


# 이미지 파일을 base64로 인코딩하는 함수
def get_base64_encoded_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()