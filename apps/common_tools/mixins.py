from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response


class BulkDeleteMixin:
    @action(detail=False, methods=['POST', 'PATCH'])
    def bulk_delete(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)
        self.get_queryset(ids=serializer.validated_data['ids']).delete()
        return Response(serializer.validated_data, status=status.HTTP_200_OK, headers=headers)
