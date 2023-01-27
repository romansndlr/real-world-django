from django.views.generic import DetailView
from ..models.article import Article


class ArticleDetailView(DetailView):
    model = Article
