from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import ArticleForm
from .models import Article


def home(request):
    return render(request, 'artik/home_orig.html')


def index(request):
    return render(request, 'artik/index.html')


@login_required
def create_article(request):
    print('Lin 10 - views.py =', request)
    if request.method == "POST":
        # print('Lin 12 - views.py =', request)
        form = ArticleForm(request.POST)
        if form.is_valid():
            print('Lin 15 - views.py =', request, form)
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('create_article')
    else:
        form = ArticleForm()
    return render(request, 'artik/create_article.html', {'form': form})


import markdown


def article_detail(request, pk):
    article = Article.objects.get(id=pk)
    content = markdown.markdown(article.content)
    return render(request, 'artik/article_detail.html', {'article': article, 'content': content})

# ==========================================================================
