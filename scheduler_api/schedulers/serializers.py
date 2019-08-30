from rest_framework import serializers
from .models import Schedule, EmailList, DatesSkip
from .logic import AssesEmailDates


class EmailListSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmailList
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):

    email = serializers.StringRelatedField(many=True)
    dates_to_skip = serializers.StringRelatedField(many=True)

    class Meta:
        model = Schedule
        fields = '__all__'
        depth = 1

    def create(self, validated_data):
        """
        Customize creating Schedule
        """

        contacts = validated_data['contacts']
        days_to_skip = validated_data['days_to_skip']

        dispatcher = AssesEmailDates(contacts, days_to_skip)
        dispatches = dispatcher.assesing_datetime()

        schedule = Schedule()
        schedule.save()

        # save emails to scheduler with assigned dates
        for email in dispatches:
            email_instance = EmailList(email=email,
                                       dispatch_date=dispatches[email])
            email.save()
            schedule.contacts.add(email)

        # save skip dates to the schedule
        for date in days_to_skip:
            date_to_skip = DatesSkipList(date=date)
            schedule.days_to_skip.add(date_to_skip)

        return schedule
