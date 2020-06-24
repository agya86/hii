from django.shortcuts import render
from django.http import HttpResponse
def mypage(request):
    return HttpResponse("hello india")
