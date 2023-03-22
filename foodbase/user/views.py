from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from .serializers import ProfileSerializer, OtpSerializer
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import MyProfile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from sms import send_sms
from twilio.rest import Client
from django.core.mail import send_mail

class GoogleLogin(SocialLoginView): 
    adapter_class = GoogleOAuth2Adapter
    #callback_url = CALLBACK_URL_YOU_SET_ON_GOOGLE
    client_class = OAuth2Client


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class ProfileView(RetrieveUpdateAPIView):

    queryset= MyProfile.objects.all()
    #permission_classes=(IsAuthenticated,)
    serializer_class = ProfileSerializer
    

class OtpVerify(APIView):
    
    #serializer_class = OtpSerializer

    def post(self,request): 
        

        send_mail(
            'Email from foodbase',
            'here is your email',
            'from@example.com',
            ['untamed737@gmail.com'],
            fail_silently=False,
        )
        

        return Response("200 ok")
        
