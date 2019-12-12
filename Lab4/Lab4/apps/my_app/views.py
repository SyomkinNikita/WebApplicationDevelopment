from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


def function_view(request):
    return render(request, 'gkgl')


class ExampleClassBased(View):
    def get(self, request):
        return render(request, 'example.html', {'my_variable': 'Этот подставится вместо переменной'})


class OrdersView(View):
    def get(self, request):
        data = {
            'orders': [
                {'title': 'Первый заказ', 'id': 1}
            ]
        }
        return render(request, 'orders.html', data)


class OrderView(View):
    def get(self, request, id):
        data = {
            'order': {
                'id': id
            }
        }
        return render(request, 'order.html', data)
