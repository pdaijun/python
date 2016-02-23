from django.shortcuts import render
from django.shortcuts import render_to_response
from web.models import Asset
from django.http.response import HttpResponse

# Create your views here.


def Add(request,name):
    Asset.objects.create(hostname=name)
    
    return HttpResponse('OK')
def Delet(request,id):    
    Asset.objects.get(id=id).delete()
    return HttpResponse('ok')
def Updet(request,id,hostname):
    obj=Asset.objects.get(id=id)
    obj.hostname=hostname
    obj.save()
    return HttpResponse('ok')
def Get(request,name):
    
    ASD=Asset.objects.filter(hostname__contains=name)
    print ASD.query
    for item in ASD:
        print item.hostname
    '''
    ASD=Asset.objects.all()
   
    
    for item in ASD:
        print item.hostname
    '''
    
    
    return HttpResponse('OK')
def asset_list(request):
    Asset_list=Asset.objects.all()
    return render_to_response('assert_list.html',{'data':Asset_list,'user':'daijun'})