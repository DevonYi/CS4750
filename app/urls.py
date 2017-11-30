from django.conf.urls import url

from . import views
from app.views import *
from doctors.views import *
from patients.views import *
from appointments import *


urlpatterns = [
    url(r'^$', home, name='home'),
    #url(r'^$', appointments, name='create_apt'),
]