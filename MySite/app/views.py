from django.shortcuts import render

from app.models import PostImage, Portfolio


def index(request):
    if request.method == 'GET':
        postimage = PostImage.objects.all()
        content = Portfolio.objects.all().order_by('-pub')[0:3]
        return render(request, 'index.html', {'postimages': postimage, 'content': content})
