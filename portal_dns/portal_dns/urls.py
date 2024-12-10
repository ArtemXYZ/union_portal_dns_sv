"""
URL configuration for portal_dns project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from origin_site_basic import views
# from portal_dns.origin_site_basic.views import index_p

from origin_site_basic.views import check_reg_form  # index_p,


urlpatterns = [
    # Страницы
    # path('admin/', admin.site.urls),
    path('', views.index, name='start_verification'),  # name='index'

    path('<str:template_name>/', views.site_map, name='site_map'),  # карта сайта




    path('01_instrument_price_tags.html/', views.price_tags_instrument, name='price_tags_instrument'),
    # name - алиас в джанго для указания точной ссылки
    path('02_instrument_requests.html/', views.instrument_requests, name='requests_instrument'),

    # path('01_instrument_price_tags.html/', views.price_tags_instrument, name='price_tags_instrument'),
    # path('01_instrument_price_tags.html/', views.price_tags_instrument, name='price_tags_instrument'),




    # Другое
    # path('api/v1/users_data/', views.APItest.as_view()),
    # path('', check_reg_form),  # Связываем путь с функцией представления  , name='check_reg_form'


    # path('admin/', admin.site.urls),
    # path('', include('frontend.urls')),

    # path('api/links/', get_site_map_links, name='get_site_map_links'),  # Django REST Framework
]
