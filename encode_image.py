import base64

def encode_image_base64(image_path):
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
        return base64.b64encode(image_data).decode('utf-8')

image_path = 'images/avatar_linkedin.png'
base64_encoded_image = encode_image_base64(image_path)
print(base64_encoded_image)