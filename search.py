import requests


def handler(event, context):
    res = requests.get('https://jisho.org/api/v1/search/words',
                       params=event['queryStringParameters'])
    return {'statusCode': 200, 'body': res.text}
