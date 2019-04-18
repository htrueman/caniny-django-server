from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from . import views

app_name = 'users'


class ProfileRouter(routers.SimpleRouter):
    routes = [
        routers.Route(
            url=r'^register/google/$',
            mapping={'post': 'google'},
            name='{basename}-google',
            detail=True,
            initkwargs={}
        ),
        routers.Route(
            url=r'^register/facebook/$',
            mapping={'post': 'facebook'},
            name='{basename}-facebook',
            detail=True,
            initkwargs={}
        ),
        routers.Route(
            url=r'^register/instagram/$',
            mapping={'post': 'instagram'},
            name='{basename}-instagram',
            detail=True,
            initkwargs={}
        ),
        routers.Route(
            url=r'register/^$',
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
    path('register/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/activate/<uuid:uidb64>/<str:token>/', views.activate, name='activate'),
    path('login/', views.LoginView.as_view(), name='token_obtain_pair'),
]
