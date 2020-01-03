from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from app.models import CarPicture, CarPictureInstance


def index(request):
    # Функция для отображения домашней страницы
    num_image = CarPicture.objects.all().count()
    num_instance = CarPictureInstance.objects.all().count()
    # Доступные книги по статусу
    num_instance_available = CarPictureInstance.objects.filter(status__exact='a').count()

    # HTML отрисовка
    # Вот так передаются данные в шаблон, то есть их надо сначала вытянуть в въюшки и передать в шаблон!!!
    return render(request, 'index.html', context={'num_image': num_image, 'num_instance': num_instance,
                                                  'num_instance_available': num_instance_available},
                  )
