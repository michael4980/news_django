from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .forms import NewsForm
from .models import News


def add_news(request):
    '''add news from page'''
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsForm()
    return render(request, 'add_news.html', {'form': form})


def news_list(request):
    '''return list of news'''
    news = News.objects.filter(is_displayed=True).order_by('-pub_date')
    paginator = Paginator(news, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'news': page_obj,
        'paginator': paginator,
        'page_obj': page_obj,
    }
    return render(request, 'news_list.html', context)


def news_detail(request, pk):
    '''description of each news on page'''
    news = get_object_or_404(News, pk=pk)
    context = {'news': news}
    return render(request, 'news_detail.html', context)


def not_displayed(request):
    '''return list of not displayed news'''
    news = News.objects.filter(is_displayed=False).order_by('-pub_date')
    paginator = Paginator(news, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'news': page_obj,
        'paginator': paginator,
        'page_obj': page_obj,
    }
    return render(request, 'not_displayed.html', context)


def delete_news(request, pk):
    '''delete news from database'''
    news = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        news.delete()
        return redirect('news_list')
    context = {'news': news}
    return render(request, 'delete_news.html', context)
