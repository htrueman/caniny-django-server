from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('', views.OrganizationViewSet, base_name='Organization')

urlpatterns = router.urls
