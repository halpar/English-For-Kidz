from rest_framework.serializers import ModelSerializer
from flashcards.models import Card , CardCategory , User

class CardCategorySerializer(ModelSerializer):
    class Meta:
        model = CardCategory
        fields = '__all__'


class CardSerializer(ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'        