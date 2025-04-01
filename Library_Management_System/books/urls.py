from .urls import path, include
from .views import BookViewSet
from rest_framework . routers import DefaultRouter

router = DefaultRouter()
router.register(r'', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
