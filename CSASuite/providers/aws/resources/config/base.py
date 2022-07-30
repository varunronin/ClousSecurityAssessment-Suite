from CSASuite.providers.aws.facade.base import AWSFacade
from CSASuite.providers.aws.resources.config.recorders import Recorders
from CSASuite.providers.aws.resources.config.rules import Rules
from CSASuite.providers.aws.resources.regions import Regions


class Config(Regions):
    _children = [
        (Recorders, 'recorders'),
        (Rules, 'rules')
    ]

    def __init__(self, facade: AWSFacade):
        super().__init__('config', facade)
