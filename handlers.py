from handlerResponse import HttpResponse
from handlerResponse import JsonResponse


# define your handlers here


def home(request, **kwargs):
    status = 200
    body = "This is the handler home"
    headers = {'Content-Type' : 'text/plain'}
    return HttpResponse(headers = headers, status = status, body = body)


def contact(request , **kwargs):
    status = 200
    data = {'name':'dagim'}
    headers = {}
    return JsonResponse(headers = headers, status = status, data = data)