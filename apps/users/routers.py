from rest_framework import routers

from . import views


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
            url=r'^register/$',
            mapping={'post': 'create'},
            name='{basename}',
            detail=True,
            initkwargs={}
        ),
    ]


router = ProfileRouter()
router.register('', views.SignUpViewSet, base_name='SignUp')

urlpatterns = router.urls
