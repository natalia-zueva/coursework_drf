from rest_framework import generics

from habits.models import Habit
from habits.serializers import HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    """
    Контроллер для создания привычки
    """
    serializer_class = HabitSerializer


class HabitListAPIView(generics.ListAPIView):
    """
    Контроллер для вывода списка привычек
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """
    Контроллер для вывода привычки
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitUpdateAPIView(generics.UpdateAPIView):
    """
    Контроллер для изменения привычки
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitDestroyAPIView(generics.DestroyAPIView):
    """
    Контроллер для удаления привычки
    """
    queryset = Habit.objects.all()


class PublicHabitListAPIView(generics.ListAPIView):
    """
    Контроллер для вывода списка публичных привычек
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)
