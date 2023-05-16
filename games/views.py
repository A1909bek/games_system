# from rest_framework.parsers import JSONParser 
# from rest_framework import status 
# from rest_framework.decorators import api_view 
# from rest_framework.response import Response 
# from .models import Game
# from .serializers import GameSerializer

# @api_view(['GET','POST'])
# def game_list(request):
#     if request.method=='GET':
#         games = Game.objects.all()
#         serializer = GameSerializer(games,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     elif request.method=='POST':
#         serializer = GameSerializer(request.data)
#         if serializer.is_valid():
#             serializer.data
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['GET','PUT','DELETE'])
# def game_detail(request,pk):
#     if request.method=='GET':
#         games = Game.objects.get(pk=pk)
#         serializer = GameSerializer(games,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     if request.method=='PUT':
#         game = Game.objects.get(pk=pk)
#         serializer = GameSerializer(game)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method=='DELETE':
#         game = Game.objects.get(pk=pk)
#         game.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

from games.models import GameCategory 
from games.models import Game 
from games.models import Player 
from games.models import PlayerScore 
from games.serializers import GameCategorySerializer 
from games.serializers import GameSerializer 
from games.serializers import PlayerSerializer 
from games.serializers import PlayerScoreSerializer 
from rest_framework import generics 
from rest_framework.response import Response 
from rest_framework.reverse import reverse

class GameCategoryList(generics.ListCreateAPIView):
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer
    name = 'gamecategory-list'

class GameCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer
    name = 'gamecategory-detail'

class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer 
    name = 'game-list'

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer 
    name = 'game-detail'

class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer()
    name = 'player-list'

class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer()
    name = 'player-detail'

class PlayerScoreList(generics.ListCreateAPIView):
    queryset = PlayerScore.objects.all()
    serializer_class = PlayerScoreSerializer
    name = 'playerscore-list'

class PlayerScoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlayerScore.objects.all()
    serializer_class = PlayerScoreSerializer
    name = 'playerscore-detail'  