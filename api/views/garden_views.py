from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.garden import Garden
from ..serializers import GardenSerializer

# Create your views here.
class Gardens(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = GardenSerializer
    def get(self, request):
        """Index request for future use"""
        # Get all the gardens:
        # Filter the gardens by owner, so you can only see your owned gardens
        gardens = Garden.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = GardenSerializer(gardens, many=True).data
        return Response({ 'gardens': data })

    def post(self, request):
        """Create request for future use"""
        # Add user to request data object
        print('in create')
        request.data['garden']['owner'] = request.user.id
        # Serialize/create garden
        garden = GardenSerializer(data=request.data['garden'])
        # If the garden data is valid according to our serializer...
        if garden.is_valid():
            # Save the created garden & send a response
            garden.save()
            return Response({ 'garden': garden.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(garden.errors, status=status.HTTP_400_BAD_REQUEST)

class GardenDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the garden to show
        garden = get_object_or_404(Garden, pk=pk)
        # Only want to show owned gardens?
        if request.user != garden.owner:
            raise PermissionDenied('Unauthorized, not your garden.')

        # Run the data through the serializer so it's formatted
        data = GardenSerializer(garden).data
        return Response({ 'garden': data })

    def delete(self, request, pk):
        """Delete request for later use"""
        # Locate garden to delete
        garden = get_object_or_404(Garden, pk=pk)
        # Check the garden's owner against the user making this request
        if request.user != garden.owner:
            raise PermissionDenied('Unauthorized, not your garden.')
        # Only delete if the user owns the  garden
        garden.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Locate garden
        # get_object_or_404 returns a object representation of our garden
        garden = get_object_or_404(Garden, pk=pk)
        # Check the garden's owner against the user making this request
        if request.user != garden.owner:
            raise PermissionDenied('Unauthorized, not your garden.')

        # Ensure the owner field is set to the current user's ID
        request.data['garden']['owner'] = request.user.id
        # Validate updates with serializer
        data = GardenSerializer(garden, data=request.data['garden'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
