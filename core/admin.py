from django.contrib import admin
from .models.tag import Tag
from .models.article import Article
from .models.profile import Profile

admin.site.register(Tag)
admin.site.register(Article)
admin.site.register(Profile)
