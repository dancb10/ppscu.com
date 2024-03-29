from django.shortcuts import render

# Create your views here.

# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.decorators import api_view
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# from rest_framework import status
# from rest.models import Game
# from rest.serializers import GameSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest.models import Game
from rest.serializers import GameSerializer

# class JSONResponse(HttpResponse):
#     def __init__(self,data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse, self).__init__(content,**kwargs)

#@csrf_exempt
@api_view(['GET','POST'])
def game_list(request):
    if request.method == "GET":
        games = Game.objects.all()
        games_serializer = GameSerializer(games, many=True)
        #return JSONResponse(games_serializer.data)
        return Response(games_serializer.data)

    elif request.method == "POST":
        #game_data = JSONParser().parse(request)
        #games_serializer = GameSerializer(data=game_data)
        games_serializer = GameSerializer(data=request.data)
        if games_serializer.is_valid():
            games_serializer.save()
            #return JSONResponse(games_serializer.data, status=status.HTTP_201_CREATED)
            return Response(games_serializer.data, status=status.HTTP_201_CREATED)
        #return JSONResponse(games_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(games_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#@csrf_exempt
@api_view(['GET','POST','PUT'])
def game_detail(request, pk):
    try:
        game=Game.objects.get(pk=pk)
    except Game.DoesNotExist:
        #return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        game_serializer = GameSerializer(game)
        #return JSONResponse(game_serializer.data)
        return Response(game_serializer.data)
    elif request.method == 'PUT':
        # game_data = JSONParser().parse(request)
        # game_serializer = GameSerializer(game, data=game_data)
        game_serializer = GameSerializer(game, request.data)
        if game_serializer.is_valid():
            game_serializer.save()
            #return JSONResponse(game_serializer.data)
            return Response(game_serializer.data)
        #return JSONResponse(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        game.delete()
        #return HttpResponse(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_204_NO_CONTENT)
