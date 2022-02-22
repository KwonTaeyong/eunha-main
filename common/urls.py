from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import main, order, delivery, Estatistics, joborder, management
from .views import yj_test

app_name = 'common'

urlpatterns = [
    ## test view
    path('test/', yj_test.test, name='test'),
    path('testajax/', yj_test.testView.as_view(), name='testajax'),

    ##  views.main
    path('', main.index, name='index'), # dashboard / 시작 페이지 index
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    ## views.order 주문
    path('order/orderlist', order.orderlist, name='orderlist' ), # 주문 리스트
    path('order/orderlist/LTO/', order.orderlistLTO, name='orderlistLTO'), # 주문리스트 -롯데온
    path('order/orderlist/nc/', order.orderlistnc, name='orderlistnc'), # 체크 필요

    ## views.delivery 출고
    path('delivery/list/', delivery.list, name='list'), ## 출고 리스트

    ## views.statistics 통계
    path('statistics/boxct/', Estatistics.boxct, name='boxct'), ## 냉장, 냉동 수량
    path('statistics/salesdaily/', Estatistics.salesdaily, name='salesdaily'), ## 매출 일일
    path('statistics/salesmonthly/', Estatistics.salesmonthly, name='salesmonthly'), ## 월별 매출 실적


    ## views.joborder 작업 지시서
    path('joborder/', joborder.index, name='joborder'), ## 지시서 int 받을지 index로 임시 지정
    path('joborder/confirm/', joborder.confirm, name='confirm' ), ## 작업지시서 수동확정
    path('joborder/confirm/FT/', joborder.confirmFT, name='confirmFT'), ## 고객사 수동확정 / 스마일
    path('joborder/confirm/LTO/', joborder.confirmLTO, name='confirmLTO'), ## 고객사 수동확정 / 롯데온

    ## views.management 관리

    #설정
    path('management/userlist/', management.userlist, name='userlist' ), ## 계정관리
    path('management/productlist/', management.productlist, name='productlist'), ## 상품명관리
    path('management/itemlist/', management.itemlist, name='itemlist'), ## 품목관리
    path('management/componentlist/', management.componentlist, name='componentlist'), ##구성품 관리
    path('management/categorylist/', management.categorylist, name='categorylist'), ## 카테고리 관리
    path('management/restdays/', management.restdays, name='restdays'), ## 휴무일 관리
    path('management/shoplist/', management.shoplist, name='shoplist'), ## 몰 관리
    path('management/objectives/', management.objectives, name='objectives') ## 목표 관리


]
