from CSASuite.providers.aliyun.resources.regions import Regions
from CSASuite.providers.aliyun.resources.rds.instances import Instances
from CSASuite.providers.aliyun.facade.base import AliyunFacade


class RDS(Regions):
    _children = [
        (Instances, 'instances')
    ]

    def __init__(self, facade: AliyunFacade):
        super().__init__('rds', facade)

