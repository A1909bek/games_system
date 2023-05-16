from django.urls import path
from .views import GameList,GameDetail,GameCategoryList,GameCategoryDetail,PlayerList,PlayerDetail,PlayerScoreDetail,PlayerScoreList

urlpatterns = [
    path('',GameList.as_view(),name=GameList.name),
    path('<int:pk>/',GameDetail.as_view(),name=GameDetail.name),
    path('category/',GameCategoryList.as_view(),name=GameCategoryList.name),
    path('category/<int:pk>/',GameCategoryDetail.as_view(),name=GameCategoryDetail.name),
    path('player/',PlayerList.as_view(),name=PlayerList.name),
    path('player/<int:pk>/',PlayerDetail.as_view(),name=PlayerDetail.name),
    path('playerscore/<int:pk>/',PlayerScoreDetail.as_view(),name=PlayerScoreDetail.name),
    path('playerscore/',PlayerScoreList.as_view(),name=PlayerScoreList.name),
]