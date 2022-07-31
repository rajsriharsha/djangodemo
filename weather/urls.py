from django.conf.urls import url
from weather import views
from .views import MainPage


urlpatterns = [
    url(r'^$', views.MainPage.as_view())
]