from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Article
from . import forms


def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html',
                  {'articles': articles})


def article_details(request, slug):
    article = Article.objects.get(slug=slug)
    article_address = 'articles/' + str(slug) + '.html'
    return render(request, article_address,
                  {'article': article})


@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        # use request.FILES, because files are not going with request.POST
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # only give that instance
            instance = form.save(commit=False)
            # request.user keeps the user name, which is now log in
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html',
                  {'form': form})
