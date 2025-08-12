from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.http import HttpResponseServerError
from thoughtsapi.models import Entry
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action  
from thoughtsapi.models import Tag
from django.db.models import Q




class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')

class EntrySerializer(serializers.ModelSerializer):
        tags = TagSerializer(many=True, read_only=True)
        tag_ids = serializers.ListField(
            child=serializers.IntegerField(), write_only=True, required=False
        )

        class Meta:
            model = Entry
            fields = ('id', 'user', 'title', 'reflection', 'created_at', 'updated_at', 'isPrivate', 'topic', 'tags', 'tag_ids')
            depth = 1

        def create(self, validated_data):
            tag_ids = validated_data.pop('tag_ids', [])
            entry = Entry.objects.create(**validated_data)
            if tag_ids:
                entry.tags.set(tag_ids)
            return entry

        def update(self, instance, validated_data):
            tag_ids = validated_data.pop('tag_ids', None)
            for attr, value in validated_data.items():
                setattr(instance, attr, value)
            instance.save()
            if tag_ids is not None:
                instance.tags.set(tag_ids)
            return instance

class Entries(ViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def list(self, request):
        user = request.user
        print("user in list:", user)
        if user and user.is_authenticated:
            entries = Entry.objects.filter(
                Q(isPrivate=False) | Q(user=user)
            )
        else: entries = Entry.objects.filter(isPrivate=False)
        print(f"User: {user}, entries count: {entries.count()}")
        for e in entries:
            print(f"Entry {e.id}: isPrivate={e.isPrivate}, user{e.user}")
        serializer = EntrySerializer(entries, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            entry = Entry.objects.get(pk=pk)
            serializer = EntrySerializer(entry, context={'request': request})
            return Response(serializer.data)
        except Entry.DoesNotExist:
            return Response({'message': 'Entry not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def create(self, request):
        serializer = EntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.auth.user)  # associate the authenticated user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            entry = Entry.objects.get(pk=pk)
        except Entry.DoesNotExist:
            return Response({'message': 'Entry not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = EntrySerializer(entry, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            entry = Entry.objects.get(pk=pk)
            entry.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Entry.DoesNotExist:
            return Response({'message': 'Entry not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['get'], url_path='myentries')
    def my_entries(self, request):
        user = request.auth.user
        entries = Entry.objects.filter(user=user)
        serializer = EntrySerializer(entries, many=True, context={'request': request})
        return Response(serializer.data)
