from rest_framework import serializers
from .models import Schedule, EmailList, DatesSkip


class EmailListSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmailList
        fields = '__all__'


class DatesSkipSerializer(serializers.ModelSerializer):

    class Meta:
        model = DatesSkip
        fields = '__all__'


class ScheduleSerilizer(serializers.ModelSerializer):

    email = EmailListSerializer()
    dates_skip = DatesSkipSerializer()

    class Meta:
        model = Schedule
        fields = '__all__'

    def create(self, validated_data):
        """
        Customize creating Schedule
        """

        contacts = validated_data['contacts']
        days_to_skip = validated_data['days_to_skip']

        schedule = Schedule.objects.create(**validated_data)

        for contact in contacts:
            email.objects.create(contact, schedule)

        for day in days_to_skip:
            dates_skip.objects.create(day, schedule)

        return schedule



class EmailSendSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmailSend
        fields = '__all__'
