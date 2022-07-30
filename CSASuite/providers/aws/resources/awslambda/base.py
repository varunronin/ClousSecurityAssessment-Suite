from CSASuite.providers.aws.facade.base import AWSFacade
from CSASuite.providers.aws.resources.regions import Regions

from .functions import Functions


class Lambdas(Regions):
    _children = [
        (Functions, 'functions')
    ]

    def __init__(self, facade: AWSFacade):
        super().__init__('lambda', facade)
