from datetime import datetime, timedelta

import jwt
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import views
from rest_framework.response import Response


class GetToken(views.APIView):
    def post(self, request):

        user = User.objects.filter(username=request.data['username']).first()
        if user is None or not user.check_password(request.data['password']):
            return Response({'message': 'Login failed.'}, status=400)

        dt = datetime.now() + timedelta(days=1)

        token = jwt.encode({
            'id': user.pk,
            'is_admin': user.is_superuser,
            'exp': int(dt.strftime('%s')),
        }, settings.SECRET_KEY, algorithm='HS256')

        return Response({'jwt': token}, status=200)


class RetrieveUser(views.APIView):
    def get(self, request, pk):
        user = User.objects.filter(pk=pk).first()
        if user is None:
            return Response({'message': 'User not found'}, status=404)

        return Response({'id': user.pk,
                         'name': f'{user.first_name} {user.last_name}'},
                        status=200)
