from django.contrib import admin
from django.urls import path
from htmx_samples_app.views import click_to_edit_view

urlpatterns = [
    path("", click_to_edit_view, name = "click_to_edit_view"),
]
