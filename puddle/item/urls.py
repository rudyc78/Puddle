from django.urls import path

from . import views


app_name = 'item'


urlpatterns = [
    path('', views.items, name='items'),
    path('new/', views.new, name="new"),
    path('<int:pk>/', views.detail, name='detail'), ##This should include an interger pk as we did under views.py
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),


]