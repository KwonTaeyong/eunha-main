from django.shortcuts import render


def orderlist(requests):


    return render(requests, 'order/orderlist.html')


def orderlistLTO(requests):


    return render(requests, 'order/orderlistLTO.html')

def orderlistnc(requests):


    return render(requests, 'order/orderlistnc.html')