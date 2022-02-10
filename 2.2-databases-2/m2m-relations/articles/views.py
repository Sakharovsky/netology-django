from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    articles = Article.objects.prefetch_related('tags').all()
    template = 'articles/news.html'
    context = {
        'object_list': articles
    }

    return render(request, template, context)
