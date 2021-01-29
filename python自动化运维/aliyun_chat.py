import base64
import urllib.parse
import hmac
from hashlib import sha1
import requests
import uuid
import time
import hmac, ssl
import json


def ssl():
    # 解决 访问ssl网站证书的问题
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        # Legacy Python that doesn't verify HTTPS certificates by default
        pass
    else:
        # Handle target environment that doesn't support HTTPS verification
        ssl._create_default_https_context = _create_unverified_https_context


def percent_encode(encodeStr):
    encodeStr = str(encodeStr)
    res = urllib.parse.quote(encodeStr)
    res = res.replace('+', '%20')
    res = res.replace('*', '%2A')
    res = res.replace('%7E', '~')
    return res


def sign(parameters,ALIYUN_ACCESS_KEY_ID,ALIYUN_ACCESS_KEY_SECRET):
    sortedParameters = sorted(parameters.items(), key=lambda parameters: parameters[0])
    print(sortedParameters)
    canonicalizedQueryString = ''
    for (k, v) in sortedParameters:
        canonicalizedQueryString += '&' + percent_encode(k) + '=' + percent_encode(v)

    stringToSign = 'GET&%2F&' + percent_encode(canonicalizedQueryString[1:])  # 使用get请求方法
    bs = ALIYUN_ACCESS_KEY_SECRET + '&'
    bs = bytes(bs, encoding='utf8')
    stringToSign = bytes(stringToSign, encoding='utf8')
    h = hmac.new(bs, stringToSign, sha1)
    # 进行编码
    signature = base64.b64encode(h.digest()).strip()
    return signature


def robot(message):
    ALIYUN_ACCESS_KEY_ID = "LTAI4GADR84j5cA2yLLSPza3"
    ALIYUN_ACCESS_KEY_SECRET = "v5lsDq16FQY7M4lPVB9Yb6A58uKgZg"

    D = {
        'Format': 'JSON',
        'Version': '2017-10-11',
        'SignatureMethod': 'HMAC-SHA1'
    }
    timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    D['SignatureNonce'] = str(uuid.uuid1())
    D['SignatureVersion'] = 1.0
    D['AccessKeyId'] = ALIYUN_ACCESS_KEY_ID
    D['Timestamp'] = timestamp

    D['Action'] = "Chat"
    D['InstanceId'] = "chatbot-cn-q6AQAQY3Ff"  # 你阿里云的机器人实例id
    D['Utterance'] = message
    D['Signature'] = sign(D,ALIYUN_ACCESS_KEY_ID,ALIYUN_ACCESS_KEY_SECRET)

    sortedParameters = sorted(D.items(), key=lambda D: D[0])

    url = 'https://chatbot.cn-shanghai.aliyuncs.com/?' + urllib.parse.urlencode(sortedParameters)
    print(url)
    r = requests.get(url)
    res=json.loads(r.text)
    res=res["Messages"][0]
    res=res['Text']['Content']
    return res

if __name__ == '__main__':
    r=robot("你好笨")
    print(r)