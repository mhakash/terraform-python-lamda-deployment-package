import json
import requests


def handler(event, context):
    r = requests.get("https://www.google.com")
    if r.status_code == 200:
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "msg": "Hello World"
            })
        }
    else:
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "msg": "not Hello World"
            })
        }
