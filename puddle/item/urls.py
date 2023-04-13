from django.urls import path

from . import views

app_name = 'item'


urlpatterns = [

    path('<int:pk>/', views.detail, name='detail'), ##This should include an interger pk as we did under views.py



]