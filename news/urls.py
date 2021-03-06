from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeList.as_view(),name='home'),
    path('cat/<int:cat_id>/', NewsByCategory.as_view(), name='category' ),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news' ),
    path('news/add_news/', CreateNews.as_view(), name='add_news'),
path('register/', register, name='register'),
path('login/', user_login, name='login'),
path('logout/', user_logout, name='logout'),

]
