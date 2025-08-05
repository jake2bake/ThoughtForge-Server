from rest_framework import viewsets, serializers, status
from rest_framework.response import Response
from thoughtsapi.models import Share

# Serializer
class ShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Share
        fields = '__all__'

# ViewSet
class ShareViewSet(viewsets.ViewSet):
    def list(self, request):
        shares = Share.objects.all()
        serializer = ShareSerializer(shares, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            share = Share.objects.get(pk=pk)
            serializer = ShareSerializer(share)
            return Response(serializer.data)
        except Share.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = ShareSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            share = Share.objects.get(pk=pk)
        except Share.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ShareSerializer(share, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            share = Share.objects.get(pk=pk)
            share.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Share.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
