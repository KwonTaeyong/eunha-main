from django.shortcuts import render



def userlist(requests):

    return render(requests, 'management/userlist.html')


def productlist(requests):

    return render(requests, 'management/productlist.html')


def itemlist(requests):

    return render(requests, 'management/itemlist.html')

def componentlist(requests):

    return render(requests, 'management/componentlist.html')

def categorylist(requests):

    return render(requests, 'management/categorylist.html')


def restdays(requests):

    return render(requests, 'management/restdays.html')


def shoplist(requests):


    return render(requests, 'management/shoplist.html')

def objectives(requests):

    return render(requests,'management/objectives.html')