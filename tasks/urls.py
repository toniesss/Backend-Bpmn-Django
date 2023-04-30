from django.urls import path
from . import views


urlpatterns = [
path('candidateGroup=<str:userposition>&firstResult=<int:itemoffset>&maxResults=<int:itemsperpage>/', views.camunda_tasks_list),
path('count/<str:userposition>',views.camunda_tasks_count),
path('<str:taskid>/form-variables',views.camunda_tasks_variables),
path('firstResult=<int:itemoffset>&maxResults=<int:itemsperpage>',views.camunda_tasks_search),
path('search/count/',views.camunda_tasks_count_search),
path('<str:taskid>/complete',views.camunda_complete_task),
path('<str:taskid>',views.camunda_task_detail),
]