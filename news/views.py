from django.shortcuts import render
from django.http import HttpResponse

from .models import News, Category

def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    context = {"news": news,
               "title": "Все новости",
               'category':categories,

               }

    return render(request,'news/index.html', context )

def get_category(request,cat_id):
    news = News.objects.filter(category_id=cat_id)
    categoties = Category.objects.all()
    category = Category.objects.get(pk=cat_id)
    return render(request,'news/category.html', {'news': news, 'categories': categoties, 'category': category } )

