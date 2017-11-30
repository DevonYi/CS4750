from django.conf.urls import url

from . import views


urlpatterns = [
url(r'^$', views.doctor, name='doctor'),
# url(r'^$', views.queryDoctors, name='query_submit'),

]