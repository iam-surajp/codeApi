from django.urls import path,include
from myapp.views import CompanyViewSet,ClientViewSet,ClientUserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'client-users', ClientUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
