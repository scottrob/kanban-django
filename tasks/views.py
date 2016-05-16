from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, renderers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from tasks.models import Cards
from tasks.serializers import CardsSerializer


class Board(generics.ListCreateAPIView):
    queryset = Cards.objects.all()
    serializer_class = CardsSerializer
    renderer_classes = (renderers.TemplateHTMLRenderer,)
    template_name = 'tasks/index.html'


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def card_list(request):
    """
    List all cards, or create a new card.
    """
    if request.method == 'GET':
        card = Cards.objects.all()
        serializer = CardsSerializer(card, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CardsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def card_detail(request, pk):
    """
    Retrieve, update or delete a card.
    """
    try:
        card = Cards.objects.get(pk=pk)
    except Cards.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CardsSerializer(card)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CardsSerializer(card, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        card.delete()
        return HttpResponse(status=204)
