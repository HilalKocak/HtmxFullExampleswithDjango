from django.contrib import admin
from django.urls import path
from htmx_samples_app.views import show_info_view, ProfileUpdateView, show_list


app_name='htmx_samples_app'

urlpatterns = [
    path('', show_list, name='show_list'),
    path('edit/<int:pk>/', ProfileUpdateView.as_view(), name='profile_update'),
    path('edit/<int:pk>/show_info_view/', show_info_view, name='show_info_view'),
    

]
