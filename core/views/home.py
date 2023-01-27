from django.shortcuts import render
from django.views import View
from ..models.article import Article
from ..models.tag import Tag


class HomeView(View):
    def get(self, request):
        articles = Article.objects.select_related("author", "author__profile")

        context = {"articles": articles}

        return render(request, "index.html", context)
