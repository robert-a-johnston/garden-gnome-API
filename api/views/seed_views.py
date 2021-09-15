from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.seed import Seed
from ..serializers import SeedSerializer

# Create your views here.
class Seeds(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = SeedSerializer
    def get(self, request):
        """Index request"""
        # Get all the seeds:
        # Filter the seeds by owner, so you can only see your owned seeds
        seeds = Seed.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = SeedSerializer(seeds, many=True).data
        return Response({ 'seeds': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['seed']['owner'] = request.user.id
        # Serialize/create seed
        seed = SeedSerializer(data=request.data['seed'])
        # If the seed data is valid according to our serializer...
        if seed.is_valid():
            # Save the created seed & send a response
            seed.save()
            return Response({ 'seed': seed.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(seed.errors, status=status.HTTP_400_BAD_REQUEST)

class SeedDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the seed to show
        seed = get_object_or_404(Seed, pk=pk)
        # Only want to show owned seeds?
        if request.user != seed.owner:
            raise PermissionDenied('Unauthorized, not your seed.')

        # Run the data through the serializer so it's formatted
        data = SeedSerializer(seed).data
        return Response({ 'seed': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate seed to delete
        seed = get_object_or_404(Seed, pk=pk)
        # Check the seed's owner against the user making this request
        if request.user != seed.owner:
            raise PermissionDenied('Unauthorized, not your seed.')
        # Only delete if the user owns the  seed
        seed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Locate seed
        # get_object_or_404 returns a object representation of our seed
        seed = get_object_or_404(Seed, pk=pk)
        # Check the seed's owner against the user making this request
        if request.user != seed.owner:
            raise PermissionDenied('Unauthorized, not your seed.')

        # Ensure the owner field is set to the current user's ID
        request.data['seed']['owner'] = request.user.id
        # Validate updates with serializer
        data = SeedSerializer(seed, data=request.data['seed'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
