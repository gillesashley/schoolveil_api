from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.serializers import SchoolLoginSerializer


class SchoolLoginView(APIView):
    def post(self, request):
        serializer = SchoolLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            school = authenticate(email=email, password=password)
            if school:
                # TODO: Generate and return a token here
                return Response({'message': 'Success'})
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
