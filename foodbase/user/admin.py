from django.contrib import admin
from .models import (User, MyProfile ,OtpVerifier)

admin.site.register(User)
admin.site.register(MyProfile)
admin.site.register(OtpVerifier)
