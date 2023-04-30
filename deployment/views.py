import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
# Create your views here.

CAMUNDA_REST_API_URL = "http://localhost:8080/engine-rest"

class CamundaDeployModeler(APIView):
   permission_classes = [IsAuthenticated]
   @swagger_auto_schema(
        operation_summary='Deployment Modeler'
   )

   def post(self, request):
      
      deployment_name = request.POST.get('deployment-name')
      deployment_source = request.POST.get('deployment-source')
      data = request.FILES.get('data')
      if not deployment_name or not data :
            return Response({'error': 'Invalid input parameters.'}, status=status.HTTP_400_BAD_REQUEST)

        # Call Camunda REST API to deploy BPMN modeler.
      try:
          files = {'data': data}
          data = {
                'deployment-name': deployment_name,
                'deployment-source': deployment_source,
            }
          url = f"{CAMUNDA_REST_API_URL}/deployment/create"
          response = requests.post(url, data=data, files=files)

          print(files, data)

          return Response(response.json(), status=status.HTTP_201_CREATED)
      except requests.exceptions.RequestException as e:
          camunda_status_code = getattr(e.response, 'status_code', 500)
          return Response({'status': camunda_status_code}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

camunda_deploy_modeler = CamundaDeployModeler.as_view()











