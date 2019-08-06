from rest_framework import generics
from .models import Auth
from .serializers import AuthSerializer

class AuthList(generics.ListAPIView): #Its ready template
   queryset = Auth.objects.all()
   serializer_class = AuthSerializer


class AuthDetail(generics.RetrieveAPIView):
   queryset = Auth.objects.all()
   serializer_class = AuthSerializer