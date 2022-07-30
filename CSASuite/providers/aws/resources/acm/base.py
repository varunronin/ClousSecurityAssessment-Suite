from CSASuite.providers.aws.facade.base import AWSFacade
from CSASuite.providers.aws.resources.regions import Regions

from .certificates import Certificates


class Certificates(Regions):
    _children = [
        (Certificates, 'certificates')
    ]

    def __init__(self, facade: AWSFacade):
        super().__init__('acm', facade)
