import json
from django.http import JsonResponse, HttpResponseNotAllowed
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token

@csrf_exempt
def login_user(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    body = json.loads(request.body.decode('utf-8'))
    username = body.get('username')
    password = body.get('password')
    
    user = authenticate(username=username, password=password)

    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return JsonResponse({
            "valid": True,
            "token": token.key,
            "id": user.id,
            "username": user.username,
            'email': user.email,
            'role': user.role,
        })

    return JsonResponse({"valid": False})
