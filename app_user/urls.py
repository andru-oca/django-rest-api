from django.urls import path, include
from rest_framework.routers import DefaultRouter # Router de rest 
from . import views # traigo las views del mismo app
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView,
) # para obtener los tokens por medio de jwt (seguridad por medio de jwt)

router = DefaultRouter()
router.register('', views.UserViewSet, basename="user")

urlpatterns=[
    path('api/', include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="get_token"),
    path('refresh-token/', TokenRefreshView.as_view(), name="refresh_view"),
]
