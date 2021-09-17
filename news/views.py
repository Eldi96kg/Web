
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import News, Category
from .forms import NewsForm,UserRegisterForm, UserLoginForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, DetailView, CreateView

categories = Category.objects.all()


class HomeList(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category']=categories
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)
# def index(request):
#     news = News.objects.all()
#     categories = Category.objects.all()
#     context = {"news": news,
#                "title": "Все новости",
#                'category':categories,
#                }
#     return render(request,'news/index.html', context )


class NewsByCategory(ListView):
    model = News
    template_name = 'news/category.html'
    context_object_name = 'news'

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['cat_id'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']=Category.objects.get(pk=self.kwargs['cat_id'])
        context['categories'] = categories
        return context
# def get_category(request,cat_id):
#     news = News.objects.filter(category_id=cat_id)
#     category = Category.objects.get(pk=cat_id)
#     return render(request,'news/category.html', {'news': news, 'categories': categories, 'category': category } )


class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'
    template_name = 'news/view_news.html'
# def view_news(request,news_id):
#     news_item = News.objects.get(pk=news_id)
#     return render(request,'news/view_news.html', {'news_item':news_item})


class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
# def add_news(request):
#     if request.method =='POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()
#     return render(request,'news/add_news.html',{'form':form})


def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request,'news/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request,'news/login.html', {"form": form})



