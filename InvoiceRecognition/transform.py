import json
import base64
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.ocr.v20181119 import ocr_client, models


with open('./发票/通行票6.jpg', 'rb') as file:  # 转换图片成base64格式
    data = file.read()
    encodestr = base64.b64encode(data)
    image_data = str(encodestr, 'utf-8')

try:
    cred = credential.Credential("AKIDiPwLYXq77wVpztn1QfJ0dKFqHbovn6Ms", "gZkKQberwunaY6Ij3UrREBNUVVpyvjcB")
    httpProfile = HttpProfile()
    httpProfile.endpoint = "ocr.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = ocr_client.OcrClient(cred, "ap-guangzhou", clientProfile)

    req = models.MixedInvoiceOCRRequest()
    params = {
        "ImageBase64": image_data
    }
    req.from_json_string(json.dumps(params))

    resp = client.MixedInvoiceOCR(req)
    print(resp.to_json_string())

except TencentCloudSDKException as err:
    print(err)