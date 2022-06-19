from .base import *
import requests
from boto3 import Session

DEBUG = False

region = requests.get('http://169.254.169.254/latest/meta-data/local-hostname').text.split('.')[1]
instance_id = requests.get('http://169.254.169.254/latest/meta-data/instance-id').text

# 予めEC2にCloudWatchへデータを送るためのポリシーをEC2のロールに設定しておく
BOTO3_SESSION = Session(region_name=region)

# 操作ログの設定
LOGGING["handlers"]["watchtower"] = {
    'class': 'watchtower.CloudWatchLogHandler',
    'filters': ['admin'],
    'boto3_session': BOTO3_SESSION,
    'log_group': 'HinoMultiAccessPFStaging',
    'stream_name': instance_id,
    'formatter': 'aws',
}

LOGGING["loggers"] = {
    "django_structlog": {
        "handlers": ["watchtower"],
        "level": "INFO",
    },
}

# oauth用パラメータ
XID_CLIENT_ID = "a4f5502c-8be5-4ef0-a20a-d2691af7fad9"
XID_CLIENT_SECRET = "RYOOA4FCnJQp0k_Tu2hvT~C2X6"
XID_REDIRECT_URI = "https://vaccination-hino.scpdev.cloud/oauth/callback"
XID_SCOPE = "openid verification mynumber"
XID_TOKEN_PASS = "YTRmNTUwMmMtOGJlNS00ZWYwLWEyMGEtZDI2OTFhZjdmYWQ5OlJZT09BNEZDbkpRcDBrX1R1Mmh2VH5DMlg2"
XID_PRIVATE_KEY = "cuXN1F933x884TB0q9NTMrCkxXIn5TQXVJkWMJz4Jdc="

# マイナンバーAPI用のURL
GET_MY_NUMBER_URL = "https://vaccination-hino.scpdev.cloud/oauth/get-my-number/"
XID_LOGIN_URL = "https://vaccination-hino.scpdev.cloud/oauth/xID-login/"
REAUTH_URL = "https://vaccination-hino.scpdev.cloud/oauth/"
