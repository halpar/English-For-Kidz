from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from flashcards.serializers import CardCategorySerializer,CardSerializer ,UserSerializer
from flashcards.models import Card , CardCategory , User


class CardCategoryCreateAPIView(CreateAPIView):
    serializer_class = CardCategorySerializer
    queryset = CardCategory.objects.all()



class CardCategoryListAPIView(ListAPIView):
    serializer_class = CardCategorySerializer
    queryset = CardCategory.objects.all()


class CardCategoryUpdateAPIView(UpdateAPIView):
    serializer_class = CardCategorySerializer
    queryset = CardCategory.objects.all()



class CardCategoryDeleteAPIView(DestroyAPIView):
    serializer_class = CardCategorySerializer
    queryset = CardCategory.objects.all()

class CardCreateAPIView(CreateAPIView):
    serializer_class = CardSerializer
    queryset = Card.objects.all()


class CardListAPIView(ListAPIView):
    serializer_class = CardSerializer
    queryset = Card.objects.all()


class CardUpdateAPIView(UpdateAPIView):
    serializer_class = CardSerializer
    queryset = Card.objects.all()

class CardDeleteAPIView(DestroyAPIView):
    serializer_class = CardSerializer
    queryset = Card.objects.all()

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = Card.objects.all()


class UserListAPIView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserDeleteAPIView(DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()