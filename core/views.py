from rest_framework.views import APIView
from rest_framework.response import Response


class HelloView(APIView):
    def get(self, request):
        data = {"Message": "Hello World"}
        return Response(data)


