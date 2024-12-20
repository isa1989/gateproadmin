import datetime
import requests
from django.views.decorators.csrf import csrf_exempt
from onesignal_sdk.client import Client
from django.core.mail import send_mail
from django.conf import settings
from notification.utils import calculate_signature
from settings.models import Settings


def send_sms(phone_number, otp_code, is_bulk=False):
    smscenter_pbk = Settings.get_solo().smscenter_pbk
    smscenter_pvk = Settings.get_solo().smscenter_pvk
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
        "msisdn": phone_number,
        "message": f"OTP: {otp_code}",
        "oper_time": oper_time,
        "is_bulk": is_bulk,
    }
    response = requests.post(smscenter_url, headers=headers, json=payload)


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


# def send_push_notification(contents, include_player_ids):
#     headers = {
#         "Content-Type": "application/json; charset=utf-8",
#         "Authorization": f"Basic {settings.ONE_SIGNAL_API_KEY}",
#     }

#     payload = {
#         "app_id": settings.ONE_SIGNAL_APP_ID,
#         "contents": {"en": contents},
#         "include_player_ids": include_player_ids,
#     }

#     response = requests.post(
#         "https://onesignal.com/api/v1/notifications", headers=headers, json=payload
#     )

#     if response.status_code == 200:
#         print("Notification sent successfully!")
#     else:
#         print(f"Failed to send notification: {response.status_code} - {response.text}")

#     return response.json()
