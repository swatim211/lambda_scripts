import sys
import time
import boto3
import datetime

def lambda_handler(event, context):
    # TODO implement
        date = time.strftime("-%d-%m-%Y")
        print date
        global db_inst
        snapshot_name = '%name%'+date
        db = boto3.client('rds', '%region%' )
        db.delete_db_instance(DBInstanceIdentifier='%name%', SkipFinalSnapshot=False, FinalDBSnapshotIdentifier=snapshot_name)
   
   