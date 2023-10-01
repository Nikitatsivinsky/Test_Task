from django.urls import path, include
from rest_framework import routers
from .views import RevenueStatisticListCreateView

router = routers.SimpleRouter()
router.register('', RevenueStatisticListCreateView)

urlpatterns = [
    path('', include(router.urls)),
]