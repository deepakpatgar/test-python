from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import EC2, Lambda
from diagrams.aws.database import RDS, Redshift, Dynamodb
from diagrams.aws.storage import S3
from diagrams.aws.network import VPC, Route53, ELB
from diagrams.aws.integration import SQS, SNS, Kinesis
from diagrams.aws.analytics import Glue, Athena, Quicksight
from diagrams.aws.security import IAM, KMS, WAF, Shield
from diagrams.aws.management import Cloudwatch, Cloudtrail
from diagrams.aws.general import User
from diagrams.onprem.network import Internet
from diagrams.onprem.compute import Server

with Diagram("Complex AWS Data Migration Architecture", show=False):

    user = User("Data Engineer")
    internet = Internet("Internet")

    with Cluster("On-Premise Environment"):
        onprem_db = Server("On-Prem Database")
        onprem_app = Server("Legacy Application")

    with Cluster("AWS Environment"):
        
        with Cluster("VPC"):
            elb = ELB("Load Balancer")
            
            with Cluster("Public Subnet"):
                ec2_migration = EC2("EC2 Migration Server")
                lambda_etl = Lambda("Lambda ETL")

            with Cluster("Private Subnet"):
                s3_landing = S3("S3 Landing Zone")
                s3_raw = S3("S3 Raw Data")
                s3_processed = S3("S3 Processed Data")
                
                rds_target = RDS("RDS Target")
                dynamo_target = Dynamodb("DynamoDB Target")
                redshift = Redshift("Redshift Data Warehouse")
                glue = Glue("AWS Glue")
                athena = Athena("Athena Query")

        with Cluster("Data Processing"):
            kinesis_stream = Kinesis("Kinesis Data Stream")
            sqs_queue = SQS("SQS Queue")
            sns_topic = SNS("SNS Topic")
            cloudwatch = Cloudwatch("CloudWatch")
            cloudtrail = Cloudtrail("CloudTrail")

        with Cluster("Security and Monitoring"):
            iam = IAM("IAM Roles")
            kms = KMS("KMS Encryption")
            waf = WAF("Web Application Firewall")
            shield = Shield("Shield")
            logging = Cloudwatch("CloudWatch Logging")

        with Cluster("Analytics & Visualization"):
            quicksight = Quicksight("QuickSight")
        
    # Data Flow
    user >> internet >> onprem_app >> elb >> ec2_migration >> s3_landing
    onprem_db >> ec2_migration >> s3_landing >> s3_raw
    
    s3_raw >> glue >> s3_processed
    s3_processed >> redshift >> athena
    s3_processed >> dynamo_target
    s3_processed >> rds_target
    s3_processed >> kinesis_stream >> lambda_etl >> redshift
    
    sns_topic >> sqs_queue >> lambda_etl
    kinesis_stream >> lambda_etl
    
    cloudwatch >> logging
    cloudtrail >> logging

    s3_processed >> athena >> quicksight

    # Security & Monitoring
    internet >> waf >> shield >> elb
    iam >> [s3_landing, s3_raw, s3_processed, rds_target, redshift, dynamo_target, glue, athena, lambda_etl, ec2_migration]
    kms >> [s3_landing, s3_raw, s3_processed, redshift]
