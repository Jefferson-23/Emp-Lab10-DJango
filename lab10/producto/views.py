from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Producto
from .serializers import ProductoSerializer

# Create your views here.
class IndexView(APIView):
    
    def get(self,request):
        context = {'mensaje':'servidor activo'}
        return Response(context)

class ProductoView(APIView):

    def get(self, request):
        dataProducto = Producto.objects.all()
        serProducto = ProductoSerializer(dataProducto, many=True)
        return Response(serProducto.data)

    def post(self, request):
        serProducto = ProductoSerializer(data=request.data)
        serProducto.is_valid(raise_exception=True)
        serProducto.save()
        return Response(serProducto.data)

class ProductoDetailView(APIView):

    def get(self, request, p_id):
        dataProducto = Producto.objects.get(pk=p_id)
        serProducto = ProductoSerializer(dataProducto)
        return Response(serProducto.data)

    def put(self, request, p_id):
        dataProducto = Producto.objects.get(pk=p_id)
        serProducto = ProductoSerializer(dataProducto, data=request.data)
        serProducto.is_valid(raise_exception=True)
        serProducto.save()
        return Response(serProducto.data)

    def delete(self, request, p_id):
        dataProducto = Producto.objects.get(pk=p_id)
        serProducto = ProductoSerializer(dataProducto)
        dataProducto.delete()
        return Response(serProducto.data)