from django.urls import path, include
from rest_framework import routers
from .views import SpendStatisticListCreateView

router = routers.DefaultRouter()
router.register('', SpendStatisticListCreateView)

urlpatterns = [
    path('', include(router.urls)),
]