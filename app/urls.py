from django.conf.urls import url

from . import views
from app.views import *
from doctors.views import *
from patients.views import *

urlpatterns = [
    url(r'^home$', home, name='home'),
    url(r'^doctor$', doctor, name='doctor'),
    url(r'^patients$', patients, name='patients'),
]