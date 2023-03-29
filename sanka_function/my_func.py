import json
import os
import urllib.request
import urllib.error

def lambda_handler(event, context):
    json_event = json.loads(event["body"])

    payload = {"text": f"Issue Created: {json_event['issue']['html_url']}"}
    data = json.dumps(payload).encode("utf-8")
    headers = {"Content-Type": "application/json"}

    url = os.environ["SLACK_URL"]
    req = urllib.request.Request(url, data=data, headers=headers)

    try:
        response = urllib.request.urlopen(req)
        response_data = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        response_data = f"Error sending message: {e.reason}"

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"message": response_data}),
    }