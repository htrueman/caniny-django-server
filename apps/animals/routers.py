from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('animals', views.AnimalViewSet, base_name='Animal')
# router.register('table_metadata', views.AnimalTableMetadataViewSet, base_name='AnimalTableMetadata')

urlpatterns = router.urls

urlpatterns += [
    path('breeds/', views.BreedListView.as_view()),
    path('table_metadata/', views.AnimalTableMetadataView.as_view()),
]
