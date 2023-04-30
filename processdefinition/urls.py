from django.urls import path
from . import views


urlpatterns = [ 
path('firstResult=<int:itemoffset>&maxResults=<int:itemsperpage>&sortBy=version&sortOrder=desc&latestVersion=true',views.camunda_workflow_list),
path('count/latestVersion=true',views.camunda_workflow_count),
path('nameLike=<str:workflowname>&firstResult=<int:itemoffset>&maxResults=<int:itemsperpage>&sortBy=version&sortOrder=desc&latestVersion=true', views.camunda_search_work_flow),
path('count/nameLike=<str:workflowname>&latestVersion=true', views.camunda_search_workflow_count),
path('delete/<str:workflowid>/',views.camunda_delete_workflow),
path('startform/<str:definitionid>',views.camunda_start_form),
path('<str:processdefinitionid>/xml',views.camunda_xml_modeler),

path('category',views.camunda_category_task),


path('formkey/<str:definitionid>',views.camunda_form_key),
path('',views.camunda_process_difinition),

]