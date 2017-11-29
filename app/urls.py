from django.conf.urls import url

from . import views
from app.views import *
from doctors.views import *
from patients.views import *


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^$', doctor, name='doctor'),
    url(r'^patients$', patients, name='patients')
]