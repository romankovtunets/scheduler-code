from django.db import models
from .logic import AssesEmailDates


class EmailList(models.Model):

    email = EmailField()


class DatesSkipList(models.Model):

    day_skip = DateTimeField()


class Schedule(models.Model):

    contacts = models.ForeignKey(
        'EmailList',
        on_delete=models.CASCADE)

    days_to_skip = models.ForeignKey(
        'DatesSkipList',
        on_delete=CASCADE)


class EmailSend(AssesEmailDates, models.Model):

    email = EmailField()
    scheduled_date = DateTimeField()

