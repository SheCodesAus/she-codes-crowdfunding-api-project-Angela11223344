from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404, JsonResponse
from rest_framework import status, generics, permissions, filters

from .models import Project, Pledge
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer, PledgeDetailSerializer

from .permissions import IsOwnerOrReadOnly, IsSupporterOrReadOnly


# Create your views here.

class ProjectList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [filters.SearchFilter]

    search_fields = ['title', 'description']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)


# class ProjectList(APIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def get(self, request):
#         projects = Project.objects.all()
#         serializer = ProjectSerializer(projects, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ProjectSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(owner=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try:
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(self.request, project)
            return project
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)
    
    def put(self, request, pk):
        project = self.get_object(pk)
        data = request.data
        serializer = ProjectDetailSerializer(
            instance=project, data=data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        project = self.get_object(pk)
        data = request.data
        serializer = ProjectDetailSerializer(
            instance=project, data=data
        )
        if serializer.is_valid():
            project.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors)

class PledgeList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSupporterOrReadOnly]
    queryset = Pledge.objects.all()
    serializer_class = PledgeSerializer
    filter_backends = [filters.SearchFilter]

    search_fields = ['comment']

    def perform_create(self, serializer):
        serializer.save(supporter=self.request.user)

    def perform_update(self, serializer):
        serializer.save(supporter=self.request.user)
        
# class PledgeList(APIView):

#     def get(self, request):
#         pledges = Pledge.objects.all()
#         serializer = PledgeSerializer(pledges, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         pledges = PledgeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(supporter=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST
#         )

class PledgeDetail(APIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSupporterOrReadOnly]

    def get_object(self, pk):
        try:
            pledges = Pledge.objects.get(pk=pk)
            self.check_object_permissions(self.request, pledges)
            return pledges
        except Pledge.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        pledges = self.get_object(pk)
        serializer = PledgeDetailSerializer(pledges)
        return Response(serializer.data)

    def put(self, request, pk):
        pledges = self.get_object(pk)
        data = request.data
        serializer = PledgeDetailSerializer(
            instance=pledges, data=data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        pledges = self.get_object(pk)
        data = request.data
        serializer = PledgeSerializer(instance=pledges, data=data)

        if serializer.is_valid:
            pledge.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors)