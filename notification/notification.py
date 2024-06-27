import datetime
import requests
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
from notification.utils import calculate_signature
from settings.models import Settings


def send_sms():
    smscenter_pbk = Settings.get_solo().sms_public_key
    smscenter_pvk = Settings.get_solo().sms_private_key
    smscenter_url = Settings.get_solo().smscenter_url
    username = Settings.get_solo().smscenter_username
    oper_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    signature = calculate_signature(oper_time, smscenter_pbk, smscenter_pvk)

    headers = {
        "Content-Type": "application/json",
        "Username": username,
        "Signature": signature,
    }
    payload = {
        "msisdn": "994709021220",
        "message": "Your SMS message content here",
        "oper_time": oper_time,
        "is_bulk": False,
    }
    try:
        response = requests.post(smscenter_url, headers=headers, json=payload)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error sending SMS: {e}")
        return False


def send_custom_mail(
    subject,
    message,
    recipient_list,
    fail_silently=False,
    connection=None,
    html_message=None,
):
    from_email = settings.EMAIL_HOST_USER

    sent = send_mail(
        subject,
        message,
        from_email,
        recipient_list,
        fail_silently=fail_silently,
        connection=connection,
        html_message=html_message,
    )

    return sent


def send_push_notification():
    pass
