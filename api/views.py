from django.http import HttpResponse
import boto3


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the api index.")