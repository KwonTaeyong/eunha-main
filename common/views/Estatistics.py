from django.shortcuts import render



def boxct(requests):


    return render(requests, 'Estatistics/boxct.html')


def salesdaily(requests):

    return render(requests, 'Estatistics/salesdaily.html')


def salesmonthly(requests):

    return render(requests, 'Estatistics/salesmonthly.html')