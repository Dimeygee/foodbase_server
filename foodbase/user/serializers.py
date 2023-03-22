from rest_framework import serializers
from .models import MyProfile
from twilio.rest import Client



class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model=MyProfile
        fields="__all__"


class OtpSerializer(serializers.Serializer):

    #email = serializers.EmailField(max_length=None, min_length=None, allow_blank=True)
    phonenumber = serializers.IntegerField()


    def create(self, validated_data):
            account_sid = 'AC820a5e8499497d540bd273a63be58702'
            auth_token = '9600d54ecde96d7a1a8cbed4bdb6fbc1'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f'your otp is: 9890',from_="+15076205495",to=f'+2349052669790'
            )

            print(message)

            return message

