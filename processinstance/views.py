import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

# Create your views here.

CAMUNDA_REST_API_URL = "http://localhost:8080/engine-rest"

class CamundaForm(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        operation_summary='List Processinstance',
        operation_description= "{\"finishedAfter\":\"2013-01-01T00:00:00.000+0200\",\"finishedBefore\":\"2013-04-01T23:59:59.000+0200\",\"executedActivityAfter\":\"2013-03-23T13:42:44\",\"variables\":[{\"name\":\"myVariable\",\"operator\":\"eq\",\"value\":\"camunda\"},{\"name\":\"mySecondVariable\",\"operator\":\"neq\",\"value\":124}],\"sorting\":[{\"sortBy\":\"businessKey\",\"sortOrder\":\"asc\"},{\"sortBy\":\"startTime\",\"sortOrder\":\"desc\"}]}"
    )
    def post(self, request, itemoffset, itemsperpage, format=None):

        bodyrequestform = request.data

        try:
            itemoffset = int(itemoffset)
            itemsperpage = int(itemsperpage)
            assert itemoffset >= 0 and itemsperpage >= 0
        except (TypeError, ValueError, AssertionError):
            return Response({'error': 'Invalid input parameters.'}, status=status.HTTP_400_BAD_REQUEST)
                
        url = f'{CAMUNDA_REST_API_URL}/history/process-instance?firstResult={itemoffset}&maxResults={itemsperpage}'
        
        try:
             response = requests.post(url, json=bodyrequestform)
             data = response.json()
             return Response(data, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            camunda_status_code = getattr(e.response, 'status_code', 500)
            return Response({'status': camunda_status_code}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except PermissionDenied as e:
            return Response({'error': 'Permission denied.'}, status=status.HTTP_403_FORBIDDEN)

camunda_form = CamundaForm.as_view() 

class CamundaFormCount(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        operation_summary='Count Processinstance'
    )
    def post(self, request, format=None):

        bodyrequestform = request.data

        url = f'{CAMUNDA_REST_API_URL}/history/process-instance/count'
        try:
            response = requests.post(url, json=bodyrequestform)
            data = response.json()
            return Response(data, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            camunda_status_code = getattr(e.response, 'status_code', 500)
            return Response({'status': camunda_status_code}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


camunda_form_count = CamundaFormCount.as_view()

class CamundaSearchForm(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        operation_summary='Search List Processinstance',
        responses={
            200: 'OK',
            400: 'Bad Request',
            500: 'Internal Server Error'
        },
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'usersender_id': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='The ID of the user sender.'
                ),
                'processDefinitionName': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='The name of the process definition to filter by.'
                ),
                'processDefinitionNameLike': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='The name of the process definition to partially match by.'
                ),
                'startedBefore': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='The maximum start date of the process instances to filter by.'
                ),
                'startedAfter': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='The minimum start date of the process instances to filter by.'
                ),
                'finishedBefore': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='The maximum end date of the process instances to filter by.'
                ),
                'finishedAfter': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='The minimum end date of the process instances to filter by.'
                ),
                'active': openapi.Schema(
                    type=openapi.TYPE_BOOLEAN,
                    description='Whether to filter for active process instances.'
                ),
                'completed': openapi.Schema(
                    type=openapi.TYPE_BOOLEAN,
                    description='Whether to filter for completed process instances.'
                ),
                'externallyTerminated': openapi.Schema(
                    type=openapi.TYPE_BOOLEAN,
                    description='Whether to filter for externally terminated process instances.'
                ),
                'itemoffset': openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description='The offset of the first item to return in the result set.'
                ),
                'itemsperpage': openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description='The maximum number of items to return in the result set.'
                )
            }
        )
    )
    def post(self, request, itemoffset, itemsperpage , format=None):

        try:
            itemoffset = int(itemoffset)
            itemsperpage = int(itemsperpage)
            assert itemoffset >= 0 and itemsperpage >= 0
        except (TypeError, ValueError, AssertionError):
            return Response({'error': 'Invalid input parameters.'}, status=status.HTTP_400_BAD_REQUEST)
        
        url = f'{CAMUNDA_REST_API_URL}/history/process-instance?firstResult={itemoffset}&maxResults={itemsperpage}'
        bodyrequest = request.data
        
        try: 
           response = requests.post(url, json=bodyrequest)
           data = response.json()
           return Response(data, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            camunda_status_code = getattr(e.response, 'status_code', 500)
            return Response({'status': camunda_status_code}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  


camunda_search_form = CamundaSearchForm.as_view()


class CamundaSearchCount(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        operation_summary='Search count Processinstance'
    )
    def post(self, request, format=None):

        url = f'{CAMUNDA_REST_API_URL}/history/process-instance/count'
        bodyrequest = request.data
        print(bodyrequest)

        try:   
           response = requests.post(url, json=bodyrequest)
           response.raise_for_status()
           data = response.json()
           return Response(data,status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            camunda_status_code = getattr(e.response, 'status_code', 500)
            return Response({'status': camunda_status_code}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)   


camunda_search_count = CamundaSearchCount.as_view()

class CamundaDeleteProcessinstance(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        operation_summary='Delete Processinstance'
    )
    def delete(self, request, processinstanceid, format=None):

        url = f'{CAMUNDA_REST_API_URL}/process-instance/{processinstanceid}'

        try:   
           response = requests.delete(url)
           data = response.json()
           return Response(datastatus=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            camunda_status_code = getattr(e.response, 'status_code', 500)
            return Response({'status': camunda_status_code}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)   

camunda_delete_processinstance = CamundaDeleteProcessinstance.as_view()

class CamundaAllCountProcessinstance(APIView):
     permission_classes = [IsAuthenticated]
     @swagger_auto_schema(
        operation_summary='All Count Processinstance'
    )
     def post(self, request, format=None):

        bodyrequest = request.data

        url = f'{CAMUNDA_REST_API_URL}/history/process-instance/count'

        try:   
           response = requests.post(url,json=bodyrequest)
           data = response.json()
           return Response(data, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            camunda_status_code = getattr(e.response, 'status_code', 500)
            return Response({'status': camunda_status_code}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)   

camunda_all_count_processinstanc = CamundaAllCountProcessinstance.as_view()


class CamundaActiveProcessinstance(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        operation_summary='Get Processinstance'
    )
    def get(self, request, processinstanceid, format=None):

        url = f'{CAMUNDA_REST_API_URL}/process-instance/{processinstanceid}'

        try:   
           response = requests.get(url)
           data = response.json()
           return Response(data, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            camunda_status_code = getattr(e.response, 'status_code', 500)
            return Response({'status': camunda_status_code}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

camunda_avtive_processinstance = CamundaActiveProcessinstance.as_view()


class CamundaHistoryProcessInsyance(APIView) :
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        operation_summary='Get history Processinstance'
    )
    def get(self, request, processinstanceid, format=None):

        url = f'{CAMUNDA_REST_API_URL}/history/process-instance/{processinstanceid}'

        try:   
           response = requests.get(url)
           data = response.json()
           return Response(data, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            camunda_status_code = getattr(e.response, 'status_code', 500)
            return Response({'status': camunda_status_code}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

camunda_history_processinstance = CamundaHistoryProcessInsyance.as_view()


class CamundaHistoryVariableProcessInsyance(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        operation_summary='Get history variable Processinstance'
    )
    def get(self, request, processinstanceid, format=None):

        url = f'{CAMUNDA_REST_API_URL}/history/variable-instance/?processInstanceId={processinstanceid}'

        try:   
           response = requests.get(url)
           data = response.json()
           return Response(data, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            camunda_status_code = getattr(e.response, 'status_code', 500)
            return Response({'status': camunda_status_code}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

camunda_history_variable_processinstance = CamundaHistoryVariableProcessInsyance.as_view()