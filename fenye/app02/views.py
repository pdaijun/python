from django.shortcuts import render ,render_to_response ,redirect

# Create your views here.

def login(request):
    if request.method == "POST":
        user=request.POST.get('username',None)
        passwd=request.POST.get('password',None)
        if user=='daijun' and passwd =='123456':
            request.session['is_login']=True
            return redirect("/app02/index/")   
    return render_to_response('app02/index.html') 
def index(request):
    if request.session.get('is_login'):
        return render_to_response('app02/login.html')
    return render_to_response('404')
def logout(request):
    del request.session['is_login']
