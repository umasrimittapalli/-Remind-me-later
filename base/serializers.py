from rest_framework import serializers
from .models import *

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields= ['id','message','date','time' ,'Reminder_method',
                 'created_at', 'is_sent']
        read_only_fields =['id', 'created_at', 'is_sent','sent_at']

        def validate(self, data):
            """
            Validate that the reminder date and time are in the future
            """
            from django.utils import timezone
            import datetime

            reminder_datetime = timezone.make_aware(
                datetime.datetime.combine(data['date'], data['time'])
            )
           
            if reminder_datetime < timezone.now():
                raise serializers.ValidationError(
                    "Reminder date and time must be in the future"
                )
            return data
        def validate_method(self, value):
            """
            Validate that the method is one of the allowed choices
            """
            valid_methods = [method[0] for method in Reminder.REMINDER_METHODS]
            if value not in valid_methods:
                raise serializers.ValidationError(
                    f"Method must be one of {', '.join(valid_methods)}"
                )
            return value