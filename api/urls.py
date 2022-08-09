

from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.views import SendingViewSet, ClientViewSet, MassageViewSet

router = SimpleRouter()

router.register('sending', SendingViewSet, basename='sending')
router.register('client', ClientViewSet, basename='client')
router.register('massage', MassageViewSet, basename='massage')


urlpatterns = [
    path('s/', include(router.urls)),
]