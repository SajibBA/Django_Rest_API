from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'book', BookViewSet)
router.register(r'student', StudentViewSet)
router.register(r'checkout', CheckoutViewSet)

urlpatterns = [
    path('', include(router.urls)),
]