from django.contrib import admin
from django.urls import path
from htmx_samples_app.views import show_info_view, ProfileUpdateView
app_name='htmx_samples_app'

urlpatterns = [
    # path("contact/<int:id>/", show_info_view, name = "show_info_view"),
    # path("contact/<int:id>/edit/", click_to_edit, name="click_to_edit"),
    path('contact/<int:pk>/edit/', ProfileUpdateView.as_view(), name='profile_update'),
    path('contact/<int:pk>/show_info_view/', show_info_view, name='show_info_view'),
    path('contact/<int:pk>/edit/show_info_view/', show_info_view, name='show_info_view'),


]
