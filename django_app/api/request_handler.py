import json
from django.conf import settings
from api.bedrock_request_body import RequestBody
from django.http import JsonResponse
import boto3
from api.bedrock_config import BedrockConfig
from django.http import HttpResponse

class RequestHandler:
    def __init__(self):
        self.__client = None
    
    def __set_bedrock_client(self):
        self.__client = boto3.client(
            "bedrock-runtime",
            region_name=settings.REGION,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        ) 
    def __parse_resp(self, raw_resp):
        raw_resp = raw_resp['body'].read()
        resp = json.loads(raw_resp)
        return resp
    
    def __extract_output(self, resp):
        output = resp['results'][0]['outputText']
        return JsonResponse({'outputText': output})
    
    def __extract_input(self, req):
        return json.loads(req.body)['text']
    
    def __create_request_body(self, text):
        request_body = RequestBody(input = text, temp = BedrockConfig.TEMP.value, topP = BedrockConfig.TOP_P.value, maxTokenCount = BedrockConfig.MAX_TOKEN_COUNT.value)
        return request_body.get_request_body()

    def __invoke_model(self, text):
        request_body = self.__create_request_body(text)
        raw_resp = self.__client.invoke_model(
           modelId = settings.BEDROCK_MODEL,
           contentType = "application/json",
           accept = "application/json",
           body=json.dumps(request_body)
       )
        return raw_resp
        
    def request_handler(self, req):
       if req.method == 'POST':      
            text = self.__extract_input(req)
            self.__set_bedrock_client()
            raw_resp = self.__invoke_model(text)
            resp = self.__parse_resp(raw_resp)
            return self.__extract_output(resp)
       else:
           return HttpResponse(status=500, content='Internal Server Error')
           

    