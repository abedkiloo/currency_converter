from django.conf.urls import url
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    url('api/(?P<version>(v1|v2))/', include('users.urls')),
    url('api/(?P<version>(v1|v2))/', include('currency_converter.urls')),
]
