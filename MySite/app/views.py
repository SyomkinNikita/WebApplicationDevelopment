from django.shortcuts import render

from app.models import PostImage


def index(request):
    if request.method == 'GET':
        postimage = PostImage.object.all()
        return render(request, 'index.html', {'postimages': postimage})
