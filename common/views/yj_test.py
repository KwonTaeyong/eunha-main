from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import User
from django.http import JsonResponse
from django.views.generic import View
from django.core import serializers



def test(requests):

    user_list = User.objects.all()


    context = {'user_list':user_list}



    return render(requests, 'main/test.html', context)


class testView(View):
    def get(self, requests):

        user_list = User.objects.all()

        if requests.GET.get('id_data'):

            sh_id = user_list.filter(username=requests.GET.get('id_data'))
            if len(sh_id) > 0:
                text = '아이디가 존재 합니다.'
            else:
                text = '사용 가능한 아이디 입니다.'

            context = {'text': text}
            print(context)
            return JsonResponse(context)



        if requests.GET.get('kw'):
            user_list = user_list.filter(name=requests.GET.get('kw'))

        user_data = []
        for iloc in user_list:
            dictdata = dict()
            dictdata['username'] = iloc.username
            dictdata['name'] = iloc.name
            dictdata['rank'] = iloc.rank
            dictdata['id'] = iloc.id
            user_data.append(dictdata)

        context = {'data':user_data}


        return JsonResponse(context)

    def post(self,request):


        if request.POST.get('method') == 'patch':
            dataget = request.POST.get
            datalen = int(dataget('len'))
            print(dataget)
            for i in range(datalen):
                checked = f'data[{i}][_attributes][checked]'

                if dataget(checked) == 'true':
                    t_data = get_object_or_404(User, pk=dataget(f'data[{i}][id]'))
                    print(t_data)
                    t_data.name = dataget(f'data[{i}][name]')
                    t_data.username = dataget(f'data[{i}][username]')
                    t_data.rank = dataget(f'data[{i}][rank]')
                    t_data.save()


            user_list = User.objects.all()
            user_data = []
            for iloc in user_list:
                dictdata = dict()
                dictdata['username'] = iloc.username
                dictdata['name'] = iloc.name
                dictdata['rank'] = iloc.rank
                dictdata['id'] = iloc.id
                user_data.append(dictdata)

            context = {'data':user_data}


            return JsonResponse(context)


        if request.POST.get('method') == 'delete':
            dataget = request.POST.get
            datalen = int(dataget('len'))
            print(dataget)
            for i in range(datalen):
                checked = f'data[{i}][_attributes][checked]'

                if dataget(checked) == 'true':
                    t_data = get_object_or_404(User, pk=dataget(f'data[{i}][id]'))
                    t_data.delete()


            user_list = User.objects.all()
            user_data = []
            for iloc in user_list:
                dictdata = dict()
                dictdata['username'] = iloc.username
                dictdata['name'] = iloc.name
                dictdata['rank'] = iloc.rank
                dictdata['id'] = iloc.id
                user_data.append(dictdata)

            context = {'data':user_data}


            return JsonResponse(context)