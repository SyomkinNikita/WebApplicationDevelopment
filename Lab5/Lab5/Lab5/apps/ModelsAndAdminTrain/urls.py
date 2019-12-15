from django.conf.urls import url

from Lab5.Lab5.apps.ModelsAndAdminTrain.views import signup

urlpatterns = [
    url(r'^signup/$', signup, name='signup'),
]
