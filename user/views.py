import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from .models import User


# User 생성
class CreateView(View):
    def post(self, request):
        User.objects.create(
            email="djangojjang@naver.com",
            name="양봉현"
        )
        return JsonResponse({'status': '200', 'message': '성공!'})


# User 읽어오기
class ReadView(View):
    def get(self, request):
        queryset = User.objects.all().values()
        user_list = list(queryset)
        return JsonResponse({'status': '200', 'list': user_list})


# Home 렌더링
class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')





