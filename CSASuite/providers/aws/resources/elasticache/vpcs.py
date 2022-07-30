from CSASuite.providers.aws.resources.vpcs import Vpcs
from CSASuite.providers.aws.resources.elasticache.cluster import Clusters
from CSASuite.providers.aws.resources.elasticache.subnetgroups import SubnetGroups


class ElastiCacheVpcs(Vpcs):
    _children = [
        (Clusters, 'clusters'),
        (SubnetGroups, 'subnet_groups')
    ]
