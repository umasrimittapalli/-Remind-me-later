from django.shortcuts import render
# Create your views here.
from .serializers import  *
from .models import *
from rest_framework.response import Response
from rest_framework import viewsets,status


class ReminderView(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            
            return Response(
                {
                    'status': 'success',
                    'message': 'Reminder created successfully',
                    'data': serializer.data
                },
                status=status.HTTP_201_CREATED,
                headers=headers
            )
        return Response(
            {
                'status': 'error',
                'message': 'Failed to create reminder',
                'errors': serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )