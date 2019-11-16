from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Article
from django.urls import reverse


def index(request):
    latest_article_list = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'articles/list.html', {'latest_article_list': latest_article_list})


def detail(requests, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Статья не найдена!")

    latest_comments_list = a.comment_set.order_by('-id')[:10]

    return render(requests, 'articles/detail.html', {'article': a, 'latest_comments_list': latest_comments_list})


def leave_comment(requests, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Статья не найдена!")

    a.comment_set.create(author_name=requests.POST['name'], comment_text= requests.POST['text'])

    return HttpResponseRedirect(reverse('articles:detail', args=(a.id,)))