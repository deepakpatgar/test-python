from diagrams import Diagram, Cluster
from diagrams.aws.analytics import Athena
from diagrams.aws.compute import EC2, AutoScaling
from diagrams.aws.database import Redshift, RDS
from diagrams.aws.management import Cloudwatch
from diagrams.aws.network import VPC
from diagrams.aws.security import IdentityAndAccessManagementIamRole as IAM
from diagrams.aws.storage import S3
from diagrams.custom import Custom
from diagrams.onprem.database import MySQL, MSSQL
from diagrams.generic.network import Firewall
from diagrams.generic.storage import Storage

with Diagram("Data Architecture with Databricks", show=False, outformat="png", direction="TB"):
    with Cluster("Legacy Databases"):
        legacy_mysql = MySQL("Legacy MySQL")
        legacy_sqlserver = MSSQL("Legacy SQL Server")
        legacy_oracle = Custom("Legacy Oracle", "./oracle.png")

    flat_files = Storage("Flat Files")

    with Cluster("VPC"):
        with Cluster("EC2 Instance"):
            ec2_instance = EC2("EC2 Instance")
            ec2_instance_scaled = AutoScaling("AutoScaling")

    with Cluster("Layers"):
        raw_layer = S3("Raw Layer (S3)")
        sanitize_layer = S3("Sanitized Layer (S3)")
        conformed_layer = Redshift("Conformed Layer (Redshift)")

    with Cluster("Services"):
        aurora = RDS("Aurora MySQL")
        athena = Athena("Athena")
        cloudwatch = Cloudwatch("CloudWatch")
        databricks = Custom("Databricks", "./databricks.png")
        delta_lake = Custom("DeltaLake", "./deltalake.png")
    aurora >> aurora

    legacy_mysql >> raw_layer
    legacy_sqlserver >> raw_layer
    legacy_oracle >> raw_layer
    flat_files >> raw_layer

    raw_layer >> sanitize_layer
    sanitize_layer >> conformed_layer

    athena >> sanitize_layer

    databricks >> sanitize_layer
    databricks >> conformed_layer

    ec2_instance_scaled >> conformed_layer

    with Cluster("Security & Compliance"):
        iam = IAM("IAM")
        firewall = Firewall("Firewall")

    iam >> aurora
    iam >> raw_layer
    iam >> sanitize_layer
    iam >> conformed_layer

    cloudwatch >> raw_layer
    cloudwatch >> sanitize_layer
    cloudwatch >> conformed_layer
    cloudwatch >> aurora
    cloudwatch >> ec2_instance

    vpc = VPC("VPC")
    vpc >> ec2_instance

    iam_user = IAM("IAM User")
    iam_role = IAM("IAM Role")

    iam_user >> iam
    iam_role >> iam
