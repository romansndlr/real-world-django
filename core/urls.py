from django.urls import include, path
from .views.home import HomeView
from .views.articles import ArticleDetailView
from .views.profiles import ProfileDetailView


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("articles/<pk>", ArticleDetailView.as_view(), name="article_detail"),
    path("profiles/<pk>", ProfileDetailView.as_view(), name="profile_detail"),
]
