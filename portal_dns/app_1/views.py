"""
    Модуль предназначен для храннеия представлений (функций обеспечивающих передачу данных во фронтенд для страниц HTML.
"""

# _________________________________________

from django.shortcuts import render
from rest_framework.generics import ListAPIView

from django import forms
from app_1.forms import CheckReg
# _________________________________________
from app_1.models import Users
# from .models import Users
from app_1.serializers import UsersSerializer

# from django.db.models import Manager
# objects = Manager()


# ======================================================================================================================
# Create your views here.
# def index_p(request):
#     # Users
#     # code = Users.objects.all()
#     return render(request, 'index.html', {'data': 5, })  # 'code': code


class APItest(ListAPIView):
    # code = Users.objects
    serializer_class = UsersSerializer



def check_reg_form(request):
    form = CheckReg()  # Создаём экземпляр формы
    return render(request, 'index.html', {'form': form})  # Передаём форму в шаблон


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