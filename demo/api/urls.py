from django.urls import path, include

from api import views

app_name = 'api'

urlpatterns = [
    path('v1/users/create/', views.createUserApiView.as_view(), name='user_create'),
    path('v1/users/list/', views.UserListAPIView.as_view(), name='user-list'),
    path('v1/users/detail/<int:pk>/', views.UserDetailAPIView.as_view(), name='user-detail'),

    #bank urls
    path('v1/banks/list/', views.BankListAPIView.as_view(), name='bank-list'),
    path('v1/banks/detail/<int:pk>/', views.BankDetailAPIView.as_view(), name='bank-detail'),

    #Account urls
    path('v1/accounts/list/', views.AccountListAPIView.as_view(), name='accounts-list'),
    path('v1/accounts/detail/<int:pk>/', views.AccountDetailAPIView.as_view(), name='account-detail')

]