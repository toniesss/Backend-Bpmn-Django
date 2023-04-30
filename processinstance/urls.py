from django.urls import path
from . import views


urlpatterns = [
path('firstResult=<str:itemoffset>&maxResults=<str:itemsperpage>',views.camunda_form),
path('count/',views.camunda_form_count),
path('search&firstResult=<str:itemoffset>&maxResults=<str:itemsperpage>',views.camunda_search_form),
path('search/count/',views.camunda_search_count),
path('<str:processinstanceid>',views.camunda_delete_processinstance),
path('allcount/',views.camunda_all_count_processinstanc),
path('active/<str:processinstanceid>', views.camunda_avtive_processinstance),

path('history/<str:processinstanceid>', views.camunda_history_processinstance),

path('history/variable/<str:processinstanceid>', views.camunda_history_variable_processinstance)

]