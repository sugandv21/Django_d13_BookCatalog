from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, books_list

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('api/', include(router.urls)), 
    path('', books_list, name='books_list'),  
]
