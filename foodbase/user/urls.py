from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    FacebookLogin,
    GoogleLogin
)
from .views import (ProfileView, OtpVerify)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('dj-rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('dj-rest-auth/google/', GoogleLogin.as_view(), name='google_login'),
    path('myprofile/<int:pk>', ProfileView.as_view(), name='myprofile'),
    path('otp/', OtpVerify.as_view(), name='otp')
]
