from django.shortcuts import render
from .models import News


def news_page(request):
    news = News.objects.all()
    return render(request, 'news/news_page.html', context={'news': news})
