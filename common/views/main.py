from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from ..models import User
from django.http import JsonResponse
from django.views.generic import View
from django.core import serializers

@login_required(login_url='common:login')
def index(requests):


    return render(requests, 'main/index.html')

