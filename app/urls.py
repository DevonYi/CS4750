from django.conf.urls import url

from . import views
from app.views import *


urlpatterns = [
    url(r'^$', home, name='home'),
]