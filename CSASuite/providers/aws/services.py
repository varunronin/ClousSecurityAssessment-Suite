from CSASuite.providers.aws.facade.base import AWSFacade
from CSASuite.providers.aws.resources.acm.base import Certificates
from CSASuite.providers.aws.resources.awslambda.base import Lambdas
from CSASuite.providers.aws.resources.cloudformation.base import CloudFormation
from CSASuite.providers.aws.resources.cloudtrail.base import CloudTrail
from CSASuite.providers.aws.resources.cloudwatch.base import CloudWatch
from CSASuite.providers.aws.resources.cloudfront.base import CloudFront
from CSASuite.providers.aws.resources.codebuild.base import CodeBuild
from CSASuite.providers.aws.resources.config.base import Config
from CSASuite.providers.aws.resources.directconnect.base import DirectConnect
from CSASuite.providers.aws.resources.dynamodb.base import DynamoDB
from CSASuite.providers.aws.resources.ec2.base import EC2
from CSASuite.providers.aws.resources.efs.base import EFS
from CSASuite.providers.aws.resources.elasticache.base import ElastiCache
from CSASuite.providers.aws.resources.elb.base import ELB
from CSASuite.providers.aws.resources.elbv2.base import ELBv2
from CSASuite.providers.aws.resources.emr.base import EMR
from CSASuite.providers.aws.resources.iam.base import IAM
from CSASuite.providers.aws.resources.kms.base import KMS
from CSASuite.providers.aws.resources.rds.base import RDS
from CSASuite.providers.aws.resources.redshift.base import Redshift
from CSASuite.providers.aws.resources.route53.base import Route53
from CSASuite.providers.aws.resources.s3.base import S3
from CSASuite.providers.aws.resources.ses.base import SES
from CSASuite.providers.aws.resources.sns.base import SNS
from CSASuite.providers.aws.resources.sqs.base import SQS
from CSASuite.providers.aws.resources.vpc.base import VPC
from CSASuite.providers.aws.resources.secretsmanager.base import SecretsManager
from CSASuite.providers.base.services import BaseServicesConfig

# Try to import proprietary services
try:
    from CSASuite.providers.aws.resources.private_cognito.base import Cognito
except ImportError:
    pass
try:
    from CSASuite.providers.aws.resources.private_docdb.base import DocDB
except ImportError:
    pass
try:
    from CSASuite.providers.aws.resources.private_ecr.base import ECR
except ImportError:
    pass
try:
    from CSASuite.providers.aws.resources.private_ecs.base import ECS
except ImportError:
    pass
try:
    from CSASuite.providers.aws.resources.private_eks.base import EKS
except ImportError:
    pass
try:
    from CSASuite.providers.aws.resources.private_guardduty.base import GuardDuty
except ImportError:
    pass
try:
    from CSASuite.providers.aws.resources.private_ssm.base import SSM
except ImportError:
    pass


class AWSServicesConfig(BaseServicesConfig):
    """
    Object that holds the necessary AWS configuration for all services in scope.

    :ivar cloudtrail:                   CloudTrail configuration
    :ivar cloudwatch:                   CloudWatch configuration:
    :ivar cloudfront:                   CloudFront configuration
    :ivar config:                       Config configuration
    :ivar dynamodb:                     DynamoDB configuration
    :ivar ec2:                          EC2 configuration
    :ivar ecs:                          ECS configuration
    :ivar ecr:                          ECR configuration
    :ivar eks:                          EKS configuration
    :ivar guarduty:                     GuardDuty configuration
    :ivar iam:                          IAM configuration
    :ivar kms:                          KMS configuration
    :ivar rds:                          RDS configuration
    :ivar redshift:                     Redshift configuration
    :ivar s3:                           S3 configuration
    :ivar ses:                          SES configuration:
    :ivar sns:                          SNS configuration
    :ivar sqs:                          SQS configuration
    """

    def __init__(self, credentials=None, **kwargs):

        super().__init__(credentials)

        facade = AWSFacade(credentials)

        self.acm = Certificates(facade)
        self.awslambda = Lambdas(facade)
        self.cloudformation = CloudFormation(facade)
        self.cloudtrail = CloudTrail(facade)
        self.cloudwatch = CloudWatch(facade)
        self.cloudfront = CloudFront(facade)
        self.codebuild = CodeBuild(facade)
        self.config = Config(facade)
        self.directconnect = DirectConnect(facade)
        self.dynamodb = DynamoDB(facade)
        self.ec2 = EC2(facade)
        self.efs = EFS(facade)
        self.elasticache = ElastiCache(facade)
        self.elb = ELB(facade)
        self.elbv2 = ELBv2(facade)
        self.emr = EMR(facade)
        self.iam = IAM(facade)
        self.kms = KMS(facade)
        self.rds = RDS(facade)
        self.redshift = Redshift(facade)
        self.route53 = Route53(facade)
        self.s3 = S3(facade)
        self.ses = SES(facade)
        self.sns = SNS(facade)
        self.sqs = SQS(facade)
        self.vpc = VPC(facade)
        self.secretsmanager = SecretsManager(facade)

        # Instantiate proprietary services
        try:
            self.cognito = Cognito(facade)
        except NameError as _:
            pass
        try:
            self.docdb = DocDB(facade)
        except NameError as _:
            pass
        try:
            self.ecr = ECR(facade)
        except NameError as _:
            pass
        try:
            self.ecs = ECS(facade)
        except NameError as _:
            pass
        try:
            self.eks = EKS(facade)
        except NameError as _:
            pass
        try:
            self.guardduty = GuardDuty(facade)
        except NameError as _:
            pass
        try:
            self.ssm = SSM(facade)
        except NameError as _:
            pass

    def _is_provider(self, provider_name):
        return provider_name == 'aws'
