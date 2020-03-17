from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializer import UserSerializer

# Create your views here.
def main(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if user.groups.filter(name = 'student').exists():
                return redirect('student')
            elif user.groups.filter(name = 'professor').exists():
                return redirect('prof')    
            else:
                return redirect('manager')
            # 로그인 성공한 경우
        else:
            return render(request, 'main.html', {'error':'username or password is incorrect.'})
            # 로그인에 실패했을 경우 ERROR Message
    else:
        return render(request, 'main.html')
        # GET 요청인 경우 로그인 화면
    return render(request,'main.html')

def index(request):
    return render(request,'index.html')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer