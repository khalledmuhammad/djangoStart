import json
from django.http import JsonResponse
#  to get json data that has been passed from the client

def api_home(request , *args , **kwargs):
    body = request.body
    print(f"body {body}")
    print(request.GET) #get the params
    print(request.POST)
    data={}
    try:
        data= json.loads(body)
    except:
        pass
    print(data.values())
    print(data.keys())
    print(data)
    #here is how to send in head in the get request
    data['params']=dict(request.GET)
    data['headers']= dict(request.headers ) # request.META to get the headers
    data['content_type']=request.content_type
    print(request.content_type )
    return JsonResponse(data)

#    return JsonResponse({ "message" : "hi there this django api response"})