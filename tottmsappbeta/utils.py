from rest_framework_jwt.utils import jwt_payload_handler

def jwt_response_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': user.username,
        'user_id': user.id,
        # Add other user details as needed
    }
