# from django.db import models


from django.db.models import Model
from django.db.models import (

    AutoField,  # Автоматически увеличиваемое поле
    ForeignKey,  # Внешний ключ

    ForeignObject,
    ForeignObjectRel,

    ManyToOneRel,

    CharField,  # Текст
    TextField,  # Большие тексты
    IntegerField,
    BooleanField,
    DateField,  # Дата

    NullBooleanField,
    ImageField,
    BinaryField,
    JSONField,

    Case, OrderBy, Subquery, Value, ValueRange, Expression
)

from django.db.models import Manager

# blank=True - поле может быть пустым, False - не может быть пустым !
#  default=значение_по_умолчанию.


# class Verification(Model):
#     """
#         Проверка регистрации пользователя.
#     """
#


class Users(Model):
    """
        Данные о пользователях.
    """

    # # телеграмм id сотрудника
    id_tg = AutoField(primary_key=True)  # , autoincrement=False, blank=False, unique=True
    # # id сотрудника в 1С и первичный ключ в этой таблице.
    code = CharField(max_length=50)  #,  unique=True
    #  session_type_id: 0 - ритейл, 1 - Оаит, 2 -
    session_type = CharField(max_length=100, blank=True)  # под запрос в SQL CASE !
    full_name = CharField(max_length=100, blank=False)  # ФИО сотрудника
    post_id = IntegerField(blank=False)  # id Должности
    post_name = TextField(blank=False)  # Text()
    branch_id = IntegerField(blank=False)  # + для фильтрации отделов.
    branch_name = CharField(max_length=200, blank=False)
    rrs_name = CharField(max_length=100, blank=False)
    division_name = CharField(max_length=100, blank=False)
    user_mail = CharField(max_length=100, blank=False)
    is_deleted = BooleanField(blank=True)  # в базе есть пустые значения, по этому True
    # Статус человек находится в статусе дискуссии (ему в этом состоянии не должны приходить уведомления по замыслу)
    discussion_status= BooleanField(blank=False, default='False')
    # Номер обращения по которому юзер находится в дискусии (если нет ничего то None) # server_default='NULL'
    discussion_number = IntegerField(blank=True, default='0')   # , unique=False
    # Для числовых значений, по умолчанию на уровне сервера нужно использовать строку
    # (SQLAlchemy ожидает строковое представление значения)
    # Номер уровня (level_id в кнопках мульти меню) с помощью которого работает кнопка назад
    state_point = IntegerField(blank=False, default='0')  # , unique=False
    # ID Стартового сообщения (что бы можно было удалять/изменять терминал (базовое меню управления).
    start_message_id = IntegerField(blank=False, default='0')  # , unique=False
    # статус сотрудника (занят ли или свободен)  # free = True, job = False (ри добавлении из бд - пусто, после апдейт
    employee_status = BooleanField(blank=False, default='False')  # activity , server_default='Null'
    # (, server_default='False' -  базе данных Нон стоит, по этому nullable=True)
    holiday_status = BooleanField(blank=True)  # Если в отпуске, то тру.
    admin_status = BooleanField(blank=False, default='False')  # Если админ, то тру.

    # Явно указываем, что objects — это менеджер
    # objects: Manager["Users"] = Manager()

    def __str__(self):
        return self.code

