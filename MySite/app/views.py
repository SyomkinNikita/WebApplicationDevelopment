from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views import View, generic

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


def carpicture_detail_view(request, pk):
    try:
        carpicture_id = CarPicture.objects.get(pk=pk)
    except CarPicture.DoesNotExist:
        raise Http404("Image does not exist")

    # book_id=get_object_or_404(Book, pk=pk)

    return render(
        request,
        'app/carpicture_detail.html',
        context={'carpicture': carpicture_id, }
    )


# Внутри данного шаблона вы можете получить доступ к списку книг при помощи переменной шаблона object_list ИЛИ
# book_list (если обобщить, то "the_model_name_list").
class PictureListView(generic.ListView):
    model = CarPicture


class PictureDetailView(generic.DetailView):
    model = CarPicture


