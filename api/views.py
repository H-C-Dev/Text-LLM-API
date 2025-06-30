import json
from django.http import JsonResponse
from django.conf import settings
from api.bedrock_request_body_config import request_body
from api.bedrock_client import get_bedrock_client


def index(request):
    client = get_bedrock_client()
    resp = client.invoke_model(
        modelId = settings.BEDROCK_MODEL,
        contentType = "application/json",
        accept = "application/json",
        body=json.dumps(request_body)
    )
    bytes = resp['body'].read()
    summary = json.loads(bytes)
    output = summary['results'][0]['outputText']
    return JsonResponse({'outputText': output})
