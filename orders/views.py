from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Order

from orders import serializers

class OrderViewSet(viewsets.GenericViewSet, 
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializer

    def get_queryset(self):
        try:
            ''' return objects for the authenticate user only '''
            return self.queryset.filter(user=self.request.user).order_by('-name')
        except:
            res = {"code": 404, "message": "Data not Found!"}
            return Response(data=json.dumps(res), status=status.HTTP_404_NOT_FOUND)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.OrderDetailSerializer

        return self.serializer_class