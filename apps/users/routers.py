from django.urls import path, re_path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from . import views

app_name = 'users'


class ProfileRouter(routers.SimpleRouter):
    routes = [
        routers.Route(
            url=r'^google/$',
            mapping={'post': 'google'},
            name='{basename}-google',
            detail=True,
            initkwargs={}
        ),
        routers.Route(
            url=r'^facebook/$',
            mapping={'post': 'facebook'},
            name='{basename}-facebook',
            detail=True,
            initkwargs={}
        ),
        routers.Route(
            url=r'^instagram/$',
            mapping={'post': 'instagram'},
            name='{basename}-instagram',
            detail=True,
            initkwargs={}
        ),
        routers.Route(
            url=r'^$',
            mapping={'post': 'create'},
            name='{basename}',
            detail=True,
            initkwargs={}
        ),
    ]


router = ProfileRouter()
router.register('', views.SignUpViewSet, base_name='SignUp')

urlpatterns = router.urls

urlpatterns += [
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('activate/<uuid:uidb64>/<str:token>/', views.activate, name='activate'),
]
