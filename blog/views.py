from django.shortcuts import render
from blog.models import Article


def index(request):
    data = Article.objects.all()
    context = {
        "data":data,
    }
    return render(request, "list.html", context)