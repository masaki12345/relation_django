from django.shortcuts import render

# Create your views here.
from .models import multi, jobs
from .serializers import multiSerializer, jobSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework import generics


class multiViewSet(viewsets.ModelViewSet):
    serializer_class = multiSerializer
    queryset = multi.objects.all()

    # @action(methods=['get'], detail=True)
    # def fullnames(self, request):
    #     return Response([
    #         '{user.first_name} {user.last_name}'.format(user=user)
    #         for user in self.get_queryset()
    #     ])

    @action(methods=['get'], detail=True)
    def fullname(self, request, pk=None):
        user = self.get_object()
        print(user)
        return Response('{user.first_name} {user.last_name}'.format(user=user))


class jobViewSet(viewsets.ModelViewSet):
    serializer_class = jobSerializer
    queryset = jobs.objects.all()


class JobListCreateApiView(APIView):
    def get(self, request):
        job = jobs.objects.all()
        serializer = jobSerializer(job, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = jobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class jobViewSet(viewsets.ModelViewSet):
#     queryset = jobs.objects.all()
#     serializer_class = jobSerializer(many=True)


class multi2ViewSet(generics.ListCreateAPIView):
    serializer_class = multiSerializer
    queryset = multi.objects.all()


class multi3ViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = multiSerializer
    queryset = multi.objects.all()


class multi4ViewSet(
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        mixins.ListModelMixin,
        viewsets.GenericViewSet):

    queryset = multi.objects.all()
    serializer_class = multiSerializer
