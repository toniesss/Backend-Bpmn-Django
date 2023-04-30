from django.urls import path
from . import views


urlpatterns = [
path('create',views.camunda_deploy_modeler)
]