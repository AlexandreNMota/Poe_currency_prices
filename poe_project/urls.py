from django.urls import include, path
from rest_framework import routers
from poe_app.views import CurrencyViewSet

router = routers.DefaultRouter()
router.register(r'poe_app', CurrencyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
