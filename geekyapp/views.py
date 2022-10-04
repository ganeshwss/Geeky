from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from geekyapp.models import Transformer
from geekyapp.serializers import TransformerSerializer


class TransformerList(APIView):
	"""
	List all Transformers, or create a new Transformer
	"""

	def get(self, request, format=None):
		transformers = Transformer.objects.all()
		serializer = TransformerSerializer(transformers, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = TransformerSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TransformerDetail(APIView):
	"""
	Retrieve, update or delete a transformer instance
	"""
	def get_object(self, pk):
		# Returns an object instance that should
		# be used for detail views.
		try:
			return Transformer.objects.get(pk=pk)
		except Transformer.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		transformer = self.get_object(pk)
		serializer = TransformerSerializer(transformer)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		transformer = self.get_object(pk)
		serializer = TransformerSerializer(transformer, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def patch(self, request, pk, format=None):
		transformer = self.get_object(pk)
		serializer = TransformerSerializer(transformer,data=request.data,partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		

	def delete(self, request, pk, format=None):
		transformer = self.get_object(pk)
		transformer.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
