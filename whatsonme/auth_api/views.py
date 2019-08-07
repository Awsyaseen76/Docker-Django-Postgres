from rest_framework import generics
from .models import Auth
from .serializers import AuthSerializer


class AuthList(generics.ListCreateAPIView):  # Its ready template
   queryset = Auth.objects.all()
   serializer_class = AuthSerializer


# the power of generics is the templates
# RetrieveAPIView -> allow just view one record
# RetrieveUpdateDestroyAPIView -> view update delete

class AuthDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = Auth.objects.all()
   serializer_class = AuthSerializer
