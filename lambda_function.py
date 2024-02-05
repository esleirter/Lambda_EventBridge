import json
import base64
import requests

def lambda_handler(event, context):
    # Jira Cloud credentials and API endpoint
    username = 'exampleemail@gmail.com'
    api_token = '<YOUR_TOKEN>'
    base_url = 'https://example.atlassian.net/rest/api/2'
    jira_project_key = 'EXP'
    jira_issue_type = 'Incident'

    guardduty_detail = event['detail']
    title = guardduty_detail['title']
    description = guardduty_detail['description']

    # Issue fields
    issue_data = {
        "fields": {
            "project": {
                "key": jira_project_key  # e.g., "PROJ"
            },
            "summary": title,
            "description": description,
            "issuetype": {
                "name": jira_issue_type  # You can change this to the type you want
            }
        }
    }

    # Authentication headers
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    # Base64 encode the username and API token
    auth_string = f'{username}:{api_token}'.encode('utf-8').strip()
    encoded_auth = b'Basic ' + base64.b64encode(auth_string)

    # Make the request to create the issue
    response = requests.post(
        f'{base_url}/issue',
        headers=headers,
        data=json.dumps(issue_data),
        auth=(username, api_token)
    )

    if response.status_code == 201:
        return {
            'statusCode': 200,
            'body': json.dumps('Issue created successfully! Issue Key: ' + response.json()["key"])
        }
    else:
        return {
            'statusCode': response.status_code,
            'body': json.dumps('Failed to create issue. Status code: ' + str(response.status_code) + '. Response: ' + response.text)
        }
