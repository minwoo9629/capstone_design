from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def main(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            group = request.user.groups.all()
            if group == ('student'):
                return redirect('student')
            else:
                return redirect('manager')    
            return redirect('manager')
            # 로그인 성공한 경우
        else:
            return render(request, 'main.html', {'error':'username or password is incorrect.'})
            # 로그인에 실패했을 경우 ERROR Message
    else:
        return render(request, 'main.html')
        # GET 요청인 경우 로그인 화면
    return render(request,'main.html')
