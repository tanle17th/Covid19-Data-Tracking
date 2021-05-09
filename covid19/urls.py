from django.urls import path
from . import views

urlpatterns = [
    path('', views.covid19_list, name='covid19_list'),
    path('add/', views.covid19_form, name='covid19_add'),
    path('update/<int:id>/', views.covid19_form, name='covid19_update'),
    path('delete/<int:id>/', views.covid19_delete, name='covid19_delete'),
    path('uploadCSV', views.upload_csv, name='covid19_upload')
]
