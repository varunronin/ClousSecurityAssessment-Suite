from CSASuite.providers.aws.facade.base import AWSFacade
from CSASuite.providers.aws.resources.base import AWSResources
from CSASuite.providers.aws.utils import format_arn


class Clusters(AWSResources):
    def __init__(self, facade: AWSFacade, region: str, vpc: str):
        super().__init__(facade)
        self.region = region
        self.vpc = vpc
        self.partition = facade.partition
        self.service = 'elasticache'
        self.resource_type = 'cluster'

    async def fetch_all(self):
        raw_clusters = await self.facade.elasticache.get_clusters(self.region, self.vpc)
        for raw_cluster in raw_clusters:
            name, resource = self._parse_cluster(raw_cluster)
            self[name] = resource

    def _parse_cluster(self, raw_cluster):
        raw_cluster['name'] = raw_cluster.pop('CacheClusterId')
        return raw_cluster['name'], raw_cluster
