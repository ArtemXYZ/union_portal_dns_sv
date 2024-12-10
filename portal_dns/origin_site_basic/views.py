"""
    Модуль предназначен для хранения представлений (функций обеспечивающих передачу данных во фронтенд для страниц HTML.
"""

# _________________________________________
from django.urls import reverse
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django.http import JsonResponse


from django import forms
from origin_site_basic.forms import CheckReg
# _________________________________________
from origin_site_basic.models import Users
# from .models import Users
from origin_site_basic.serializers import UsersSerializer

# from django.db.models import Manager
# objects = Manager()


# ======================================================================================================================
# Create your views here.
# def index_p(request):
#     # Users
#     # code = Users.objects.all()
#     return render(request, 'index.html', {'data': 5, })  # 'code': code


# Представления на страницы:
# def create_page_view(request, page_name):
#     return render(request, f'{page_name}.html')

def index(request):
    return render(request, 'index.html')  # 'code': code

def price_tags_instrument(request):
    return render(request,  '01_instrument_price_tags.html')  # 'origin_site_basic/01_instrument_price_tags.html'

def instrument_requests(request):
    return render(request, '02_instrument_requests.html')






def site_map(request, template_name):
    # data_links = {
    #     'Инструмент "Ценники': '01_instrument_price_tags.html/',
    #     'Инструмент "Обращения': '02_instrument_requests.html',
    #     'Инструмент "Скидки': "https://example.com/discounts",
    #     'О нас': "https://example.com/about",
    # }

    #  reverse('site_map', args=['01_instrument_price_tags.html']),

    data_links = [
        # {'key': '/01_instrument_price_tags.html/', 'value': 'Инструмент "Ценники"'},
        # {'key': '/02_instrument_requests.html/', 'value': 'Инструмент "Обращения"'},

        {
            'key': reverse('site_map', args=['01_instrument_price_tags.html']),
            'value': 'Инструмент "Ценники"'
        },
        {
            'key': reverse('site_map', args=['02_instrument_requests.html']),
            'value': 'Инструмент "Обращения"'
        },

    ]
    return render(request, template_name, {'data_links': data_links})  #






class APItest(ListAPIView):
    # code = Users.objects
    serializer_class = UsersSerializer


def check_reg_form(request):
    form = CheckReg()  # Создаём экземпляр формы
    return render(request, 'index.html', {'form': form})  # Передаём форму в шаблон






# def get_site_map_links(request):
#     """
#         Формируем список ссылок "левого навигатора".
#     """
#     data_links = [
#         {"name": "Инструмент 'Ценники'", "url": "https://machinelearningworkshop.com"},
#         {"name": "Инструмент 'Обращения'", "url": "https://example.com/contact"},
#         {"name": "Инструмент 'Скидки'", "url": "https://example.com/discounts"},
#         {"name": "О нас", "url": "https://example.com/about"},
#     ]
#
#     # Передаём список в шаблон
#     # return render(request, 'page.html', {"links": links})
#     return JsonResponse(data, safe=False)














# Создаем новый объект Users
# new_user = Users(
#     code="ABC123",
#     session_type="Full-time",
#     full_name="John Doe",
#     post_id=1,
#     post_name="Manager",
#     branch_id=101,
#     branch_name="Headquarters",
#     rrs_name="Finance",
#     division_name="HR",
#     user_mail="john.doe@example.com",
#     is_deleted=False,
#     discussion_status=True,
#     discussion_number=5,
#     state_point=10,
#     start_message_id=12345,
#     employee_status=True,
#     holiday_status=False,
#     admin_status=False
# )
#
# # Сохраняем объект в базе данных
# new_user.save()