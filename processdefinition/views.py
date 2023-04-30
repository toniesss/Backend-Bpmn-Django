import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.permissions import IsAuthenticated
# Create your views here.

CAMUNDA_REST_API_URL = "http://localhost:8080/engine-rest"

class CamundaWorkflowList(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        operation_summary='List Workflow'
    )
    def get(self, request, itemoffset, itemsperpage, format=None):

        try:
            itemoffset = int(itemoffset)
            itemsperpage = int(itemsperpage)
            assert itemoffset >= 0 and itemsperpage >= 0
        except (TypeError, ValueError, AssertionError):
            return Response({'error': 'Invalid input parameters.'}, status=status.HTTP_400_BAD_REQUEST)
        
        url = f'{CAMUNDA_REST_API_URL}/process-definition?firstResult={itemoffset}&maxResults={itemsperpage}&sortBy=deployTime&sortOrder=desc&latestVersion=true'
        try:    
            response = requests.get(url)
            data = response.json()
            return Response(data, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            camunda_status_code = getattr(e.response, 'status_code', 500)
            return Response({'status': camunda_status_code}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

camunda_workflow_list = CamundaWorkflowList.as_view()

class CamundaWorkflowCount(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        operation_summary='Workflow Count'
    )
    def get(self, request, format=None):

        url = f'{CAMUNDA_REST_API_URL}/process-definition/count?latestVersion=true'

        try:
           response = requests.get(url)
           data = response.json()
           return Response(data, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            camunda_status_code = getattr(e.response, 'status_code', 500)
            return Response({'status': camunda_status_code}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

camunda_workflow_count = CamundaWorkflowCount.as_view()    


class CamundaSearchWorkflow(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        operation_summary='Search List Workflow'
    )
    def get(self, request, workflowname, itemoffset, itemsperpage, format=None):

        try:
            itemoffset = int(itemoffset)
            itemsperpage = int(itemsperpage)
            assert itemoffset >= 0 and itemsperpage >= 0
        except (TypeError, ValueError, AssertionError):
            return Response({'error': 'Invalid input parameters.'}, status=status.HTTP_400_BAD_REQUEST)
    
        url = f'{CAMUNDA_REST_API_URL}/process-definition?nameLike=%{workflowname}%&firstResult={itemoffset}&maxResults={itemsperpage}&sortBy=deployTime&sortOrder=desc&latestVersion=true'
        print(url)
        try:
           response = requests.get(url)
           data = response.json()
           print(data)
           return Response(data, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            camunda_status_code = getattr(e.response, 'status_code', 500)
            return Response({'status': camunda_status_code}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

camunda_search_work_flow = CamundaSearchWorkflow.as_view()  


class CamundaSearchWorkflowCount(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        operation_summary='Search Count List Workflow'
    )
    def get(self, request, workflowname, format=None):
    
        url = f'{CAMUNDA_REST_API_URL}/process-definition/count?nameLike=%{workflowname}%&latestVersion=true'
        print(url)
        try:
           response = requests.get(url)
           data = response.json()
           return Response(data, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            camunda_status_code = getattr(e.response, 'status_code', 500)
            return Response({'status': camunda_status_code}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

camunda_search_workflow_count = CamundaSearchWorkflowCount.as_view()

class CamundaDeleteWorkflow(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        operation_summary='Delete Workflow'
    )
    def delete(self, request, workflowid, format=None):
        # workflow_id = request.query_params.get('workflowid')
        # print(workflowid)
        url = f'{CAMUNDA_REST_API_URL}/process-definition/{workflowid}'
        try:
           response = requests.delete(url)
           data = response
           return Response(data, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            camunda_status_code = getattr(e.response, 'status_code', 500)
            return Response({'status': camunda_status_code}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
        
camunda_delete_workflow = CamundaDeleteWorkflow.as_view()

class CamundaStartForm(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        operation_summary='Start Workflow',
         request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['requestdata'],
        properties={
            'requestdata': openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'variables': openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'aVariable': openapi.Schema(type=openapi.TYPE_STRING,
                             description = "\"aVariable\":{\"value\":\"aStringValue\",\"type\":\"String\",\"valueInfo\":{\"transient\":\"true\"}},\"anotherVariable\":{\"value\":\"true\",\"type\":\"Boolean\"}"
                          )      
                        },
                    ),
                    'businessKey': openapi.Schema(type=openapi.TYPE_STRING),
                },
            ),
        },
    ),
    )
    def post(self, request, definitionid, format=None):  
        # headers = { "Content-Type": "application/json" }
        variables = request.data
        print(variables)
        url = f'{CAMUNDA_REST_API_URL}/process-definition/{definitionid}/start'
        try:
           response = requests.post(url, json=variables)
           data = response.json()
           return Response(data, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            camunda_status_code = getattr(e.response, 'status_code', 500)
            return Response({'status': camunda_status_code}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
        
camunda_start_form =  CamundaStartForm.as_view()   

class CamundaFormKey(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, definitionid, format=None):

        url = f'{CAMUNDA_REST_API_URL}/process-definition/{definitionid}/startForm'
        try:
           response = requests.get(url)
           data = response.json()
           return Response(data, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            camunda_status_code = getattr(e.response, 'status_code', 500)
            return Response({'status': camunda_status_code}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
        
camunda_form_key = CamundaFormKey.as_view()        
 

class CamundaProcessdifinition(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):

        url = f'{CAMUNDA_REST_API_URL}/process-definition?sortBy=version&sortOrder=desc&latestVersion=true'
        try:
           response = requests.get(url)
           data = response.json()
           return Response(data, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            camunda_status_code = getattr(e.response, 'status_code', 500)
            return Response({'status': camunda_status_code}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
        
camunda_process_difinition = CamundaProcessdifinition.as_view()    

class CamundaXmlProcessdefinition(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        operation_summary='Get xml'
    )
    
    def get(self, request, processdefinitionid, format=None):

        # if not processdefinition_id:
        #     return Response({'error': 'No process definition ID provided.'}, status=status.HTTP_400_BAD_REQUEST)
        
        url = f'{CAMUNDA_REST_API_URL}/process-definition/{processdefinitionid}/xml'
        
        try:
            response = requests.get(url)           
            # Return data
            data = response.json()
            return Response(data, content_type='application/่json', status=status.HTTP_200_OK)
        
        except requests.exceptions.RequestException as e:
                camunda_status_code = getattr(e.response, 'status_code', 500)
                return Response({'error': e.response.text, 'status': camunda_status_code}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

camunda_xml_modeler = CamundaXmlProcessdefinition.as_view()


# Categry Task 
class CamundaCategoryTask(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        operation_summary='Category Task'
    )
    def get(self, request, format=None):

        url = f'{CAMUNDA_REST_API_URL}/process-definition?sortBy=deployTime&sortOrder=desc&latestVersion=true'
        try:    
            response = requests.get(url)
            data = response.json()
            return Response(data, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            camunda_status_code = getattr(e.response, 'status_code', 500)
            return Response({'status': camunda_status_code}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
camunda_category_task = CamundaCategoryTask.as_view()    


        

