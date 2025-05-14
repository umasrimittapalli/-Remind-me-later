from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'reminders', ReminderView,basename='reminder')

urlpatterns = [
    path('', include(router.urls)),
]
