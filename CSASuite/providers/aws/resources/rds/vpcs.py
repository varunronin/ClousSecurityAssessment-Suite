from CSASuite.providers.aws.resources.vpcs import Vpcs
from CSASuite.providers.aws.resources.rds.instances import RDSInstances
from CSASuite.providers.aws.resources.rds.snapshots import Snapshots
from CSASuite.providers.aws.resources.rds.subnetgroups import SubnetGroups


class RDSVpcs(Vpcs):
    _children = [
        (RDSInstances, 'instances'),
        (Snapshots, 'snapshots'),
        (SubnetGroups, 'subnet_groups'),
    ]
