from CSASuite.providers.aws.resources.vpcs import Vpcs
from CSASuite.providers.aws.resources.ec2.instances import EC2Instances
from CSASuite.providers.aws.resources.ec2.securitygroups import SecurityGroups
from CSASuite.providers.aws.resources.ec2.networkinterfaces import NetworkInterfaces


class Ec2Vpcs(Vpcs):
    _children = [
        (EC2Instances, 'instances'),
        (SecurityGroups, 'security_groups'),
        (NetworkInterfaces, 'network_interfaces')
    ]
