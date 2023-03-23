import json
import logging
import dnspython
# import requests


def lambda_handler(event, context):
    logger = logging.getLogger('simple_example')
    filename = input("Enter a filename: ")
    logger.info("Processing %s", filename)
    
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }