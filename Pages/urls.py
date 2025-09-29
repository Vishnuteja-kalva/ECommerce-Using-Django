from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet,UserViewSet,CartViewSet   # ✅ updated import

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'users',UserViewSet) 
router.register(r'cart',CartViewSet)  

urlpatterns = [
    path('', include(router.urls)),
]
