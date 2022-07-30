from CSASuite.providers.aliyun.resources.regions import Regions
from CSASuite.providers.aliyun.facade.base import AliyunFacade
from CSASuite.providers.aliyun.resources.kms.keys import Keys


class KMS(Regions):
    _children = [
        (Keys, 'keys')
    ]

    def __init__(self, facade: AliyunFacade):
        super().__init__('kms', facade)
