from rest_framework import routers

from . import views


class OrganizationRouter(routers.SimpleRouter):
    extra_routes = [
        routers.Route(
            url=r'^{prefix}/manage{trailing_slash}$',
            mapping={
                'put': 'update',
                'patch': 'partial_update',
                'get': 'retrieve',
                'delete': 'destroy',
            },
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Instance'}
        ),
    ]

    def get_routes(self, viewset):
        routers = super().get_routes(viewset)
        return routers + self.extra_routes


router = OrganizationRouter()
router.register('organizations', views.OrganizationViewSet, base_name='Organization')

urlpatterns = router.urls
