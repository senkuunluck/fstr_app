from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import *
from .serializers import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class CoordsViewSet(viewsets.ModelViewSet):
    queryset = Coords.objects.all()
    serializer_class = CoordsSerializer


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer


class PerevalViewSet(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer

    def create(self, request, *args, **kwargs):
        serializer = PerevalSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'status': status.HTTP_200_OK, 'message': None, 'id': serializer.data, })
        if status.HTTP_400_BAD_REQUEST:
            return Response({'status': status.HTTP_400_BAD_REQUEST, 'message': 'Bad Request', 'id': None, })
        if status.HTTP_500_INTERNAL_SERVER_ERROR:
            return Response(
                {'status': status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': 'Ошибка подключения к базе данных',
                 'id': None, })

    def partial_update(self, request, *args, **kwargs):
        cur_pass = self.get_object()
        if cur_pass.status == "new":
            serializer = PerevalSerializer(cur_pass, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "status": 1,
                    "message": "Запись изменена!"
                })
            else:
                return Response({
                    "status": 0,
                    "message": serializer.errors
                })
        else:
            return Response({
                "status": 0,
                "message": f"Отклонено: {cur_pass.get_status_display()}"
            })