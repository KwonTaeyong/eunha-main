from django.shortcuts import render



def list(requests):

    return render(requests, 'delivery/list.html')