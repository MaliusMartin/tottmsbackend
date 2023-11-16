from datetime import timedelta
from rest_framework_simplejwt.tokens import RefreshToken

def jwt_response_handler(token, user=None, request=None):
    return {
        'token': str(token),
        'user': {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'nin': user.nin,  # Add the National Identification Number
            # Add other user details as needed
        },
        # Add other details from the token if needed
    }
