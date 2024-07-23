import firebase_admin
from firebase_admin import credentials, messaging

# Path to your service account key file
cred = credentials.Certificate("api/serviceAccountKey.json")
firebase_admin.initialize_app(cred)


def send_push_notification(registration_token, title, body, data_object=None):
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body,
        ),
        data=data_object,
        token=registration_token,
    )
    response = messaging.send(message)
    return response
