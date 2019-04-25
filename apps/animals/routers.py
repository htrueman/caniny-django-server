from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('', views.AnimalViewSet, base_name='Animal')

urlpatterns = router.urls
