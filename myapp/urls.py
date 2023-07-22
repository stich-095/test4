from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path("", views.index, name="index"),
    path("statusRegister", views.statusRegister, name="statusRegister"),
    path("pwa", views.pwa, name="pwa"),
    path( "sw.js", TemplateView.as_view(template_name="sw.js", content_type='application/javascript'), name="sws")
]   
