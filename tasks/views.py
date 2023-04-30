import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
import json
from drf_yasg.utils import swagger_auto_schema
# from drf_yasg import openapi
from rest_framework.permissions import IsAuthenticated


# Create your views here.

CAMUNDA_REST_API_URL = "http://localhost:8080/engine-rest"


class CamundaTasksList(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        operation_summary='List Tasks'
    )
    def get(self, request, userposition, itemoffset, itemsperpage, format=None):

       # Validate input parameters.
        try:
            itemoffset = int(itemoffset)
            itemsperpage = int(itemsperpage)
            assert itemoffset >= 0 and itemsperpage >= 0
        except (TypeError, ValueError, AssertionError):
            return Response({'error': 'Invalid input parameters.'}, status=status.HTTP_400_BAD_REQUEST)

        # Call Camunda REST API to get tasks.
        url = f'{CAMUNDA_REST_API_URL}/task?candidateGroup={userposition}&firstResult={itemoffset}&maxResults={itemsperpage}&sortBy=created&sortOrder=desc'
        try:
            response = requests.get(url)
            data = response.json()
            return Response(data, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            camunda_status_code = getattr(e.response, 'status_code', 500)
            return Response({'status': camunda_status_code}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


camunda_tasks_list = CamundaTasksList.as_view()


class CamundaTasksCount(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        operation_summary='Count Tasks'
    )
    def get(self, request, userposition, format=None):
        # userposition = request.query_params.get('userposition')
        url = f'{CAMUNDA_REST_API_URL}/task/count?candidateGroup={userposition}'
        try:
            response = requests.get(url)
            data = response.json()
            print(data)
            return Response(data, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            camunda_status_code = getattr(e.response, 'status_code', 500)
            return Response({'status': camunda_status_code}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

camunda_tasks_count = CamundaTasksCount.as_view()


class CamundaTasksVariable(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        operation_summary='Task Variable'
    )
    def get(self, request, taskid, format=None):

        url = f'{CAMUNDA_REST_API_URL}/task/{taskid}/form-variables'

        try:
            response = requests.get(url)
            data = response.json()
            return Response(data, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            camunda_status_code = getattr(e.response, 'status_code', 500)
            return Response({'status': camunda_status_code}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

camunda_tasks_variables = CamundaTasksVariable.as_view()


class CamundaTaskSearch(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        operation_summary='Search List Tasks',
        operation_description= "{\"taskVariables\":[{\"name\":\"varName\",\"value\":\"varValue\",\"operator\":\"eq\"},{\"name\":\"anotherVarName\",\"value\":30,\"operator\":\"neq\"}],\"processInstanceBusinessKeyIn\":[\"aBusinessKey\",\"anotherBusinessKey\"],\"assigneeIn\":[\"anAssignee\",\"anotherAssignee\"],\"priority\":10,\"sorting\":[{\"sortBy\":\"dueDate\",\"sortOrder\":\"asc\"},{\"sortBy\":\"processVariable\",\"sortOrder\":\"desc\",\"parameters\":{\"variable\":\"orderId\",\"type\":\"String\"}}]}"
    )
    def post(self, request, itemoffset, itemsperpage, format=None):

        url = f'{CAMUNDA_REST_API_URL}/task?firstResult={itemoffset}&maxResults={itemsperpage}'
        print(url)
        bodyrequest = request.data
        try:    
            response = requests.post(url, json=bodyrequest)
            data = response.json()

            return Response(data, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            camunda_status_code = getattr(e.response, 'status_code', 500)
            return Response({'status': camunda_status_code}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


camunda_tasks_search = CamundaTaskSearch.as_view()


class CamundaTaskCountSearch(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        operation_summary='Search Count Tasks',
        operation_description= "{\"taskVariables\":[{\"name\":\"varName\",\"value\":\"varValue\",\"operator\":\"eq\"},{\"name\":\"anotherVarName\",\"value\":30,\"operator\":\"neq\"}],\"processInstanceBusinessKeyIn\":[\"aBusinessKey\",\"anotherBusinessKey\"],\"assigneeIn\":[\"anAssignee\",\"anotherAssignee\"],\"priority\":10,\"sorting\":[{\"sortBy\":\"dueDate\",\"sortOrder\":\"asc\"},{\"sortBy\":\"processVariable\",\"sortOrder\":\"desc\",\"parameters\":{\"variable\":\"orderId\",\"type\":\"String\"}}]}"
    )
    def post(self, request, format=None):

        url = f'{CAMUNDA_REST_API_URL}/task/count'
        bodyrequest = request.data
        try:
           response = requests.post(url, json=bodyrequest)
           data = response.json()
           print(data)
           return Response(data, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            camunda_status_code = getattr(e.response, 'status_code', 500)
            return Response({'status': camunda_status_code}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


camunda_tasks_count_search = CamundaTaskCountSearch.as_view()


class CamundaCompleteTask(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        operation_summary='Complete Task Approve or Reject'
    )
    def post(self, request, taskid, format=None):

        bodyrequest = request.data
        print(bodyrequest)
        try:
           if bodyrequest :
             url = f'{CAMUNDA_REST_API_URL}/task/{taskid}/complete'
             response = requests.post(url, json=bodyrequest)
             data = response.json()
             return Response(data, status=status.HTTP_204_NO_CONTENT)
        except requests.exceptions.RequestException as e:
            camunda_status_code = getattr(e.response, 'status_code', None)
            return Response({'status': camunda_status_code})
        
camunda_complete_task = CamundaCompleteTask.as_view()


class CamundaTaskDetail(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        operation_summary='Task Detial'
    )
    def get(self, request, taskid, format=None):

        try:

             url = f'{CAMUNDA_REST_API_URL}/task/{taskid}'
             print(url)
             response = requests.get(url)
             data = response.json()
             return Response(data, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            camunda_status_code = getattr(e.response, 'status_code', None)
            return Response({'status': camunda_status_code})
        
        
camunda_task_detail = CamundaTaskDetail.as_view()