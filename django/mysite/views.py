from django.http import HttpResponse
import datetime
def hello(request):
    return  HttpResponse("hello,world")
    
def NowTime(request):
    now=datetime.datetime.now()
    html="<html><body> It's time %s </body></html> "% now
    return HttpResponse(html)