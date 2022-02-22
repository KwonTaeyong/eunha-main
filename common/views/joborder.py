from django.shortcuts import render


def index(requests):


    return render(requests, 'joborder/index.html')


def confirm(requests):

    return render(requests, 'joborder/confirm.html')

def confirmFT(requests):

    return render(requests, 'joborder/confirmFT.html')


def confirmLTO(requests):

    return render(requests, 'joborder/confirmLTO.html')