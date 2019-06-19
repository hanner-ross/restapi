from usuarios.models import Usuarios, Tableros, Ideas
from usuarios.serializers import UsuariosSerializer, TablerosSerializer, IdeasSerializer
from rest_framework import generics


class UsuariosList(generics.ListCreateAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer


class UsuariosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer


class TablerosList(generics.ListCreateAPIView):
    queryset = Tableros.objects.all()
    serializer_class = TablerosSerializer


class TablerosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tableros.objects.all()
    serializer_class = TablerosSerializer

class IdeasList(generics.ListCreateAPIView):
    queryset = Ideas.objects.all()
    serializer_class = IdeasSerializer


class IdeasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ideas.objects.all()
    serializer_class = IdeasSerializer
    def get_queryset(self, pk):
        try:
            ideas = Ideas.objects.get(pk=pk)
        except Ideas.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return ideas

    # Get a ideas
    def get(self, request, pk):

        ideas = self.get_queryset(pk)
        serializer = IdeasSerializer(ideas)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update a ideas
    def put(self, request, pk):
        
        ideas = self.get_queryset(pk)

        if(request.user == ideas.creator): # If creator is who makes request
            serializer = IdeasSerializer(ideas, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    # Delete a ideas
    def delete(self, request, pk):

        ideas = self.get_queryset(pk)

        if(request.user == ideas.creator): # If creator is who makes request
            ideas.delete()
            content = {
                'status': 'NO CONTENT'
            }
            return Response(content, status=status.HTTP_204_NO_CONTENT)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)