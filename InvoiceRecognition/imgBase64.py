import base64


with open('./发票/专票1.jpg', 'rb') as file:  # 转换图片成base64格式
    data = file.read()
    encodestr = base64.b64encode(data)
    image_data = str(encodestr, 'utf-8')

print(image_data)

