from django.views.decorators.csrf import csrf_exempt
from api.request_handler import RequestHandler

@csrf_exempt
def index(request):
    handleRequest = RequestHandler()
    return handleRequest.request_handler(request)

