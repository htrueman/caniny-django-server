from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('animals', views.AnimalViewSet, base_name='Animal')

urlpatterns = router.urls

urlpatterns += [
    path('breeds/', views.BreedListView.as_view())
]
