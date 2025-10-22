from django.urls import path
from rest_framework import routers, generics
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamList(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityList(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardList(generics.ListCreateAPIView):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutList(generics.ListCreateAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('teams/', TeamList.as_view(), name='team-list'),
    path('activities/', ActivityList.as_view(), name='activity-list'),
    path('leaderboard/', LeaderboardList.as_view(), name='leaderboard-list'),
    path('workouts/', WorkoutList.as_view(), name='workout-list'),
]
