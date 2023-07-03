"""
File for functions to perform in the event of plant record
state changes
"""
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


def planted_actions(plant_record):
    """
    Actions to be taken on plant records
    entering 'planted' state
    """
    if plant_record.order is not None:
        cust_email = plant_record.order.email
        print(cust_email)
        subject = render_to_string(
            'plants/certificate_email/certificate_email_subject.txt',
            {'plant_record': plant_record})
        body = render_to_string(
            'plants/certificate_email/certificate_email_body.txt',
            {'plant_record': plant_record,
             'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )
