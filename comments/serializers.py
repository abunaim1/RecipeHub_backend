from rest_framework import serializers
from .models import Comment, Reaction

class CommentSerializers(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    title = serializers.CharField(source='kitchen.title', read_only=True)
    ingredients = serializers.CharField(source='kitchen.ingredients', read_only=True)
    flavour = serializers.CharField(source='kitchen.flavour', read_only=True)
    region = serializers.CharField(source='kitchen.region', read_only=True)
    image = serializers.ImageField(source='kitchen.image', read_only=True)
    creation_date = serializers.DateTimeField(source='kitchen.creation_date', read_only=True)
    seasonal = serializers.CharField(source='kitchen.seasonal', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'

class ReactionSerializers(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    
    title = serializers.CharField(source='kitchen.title', read_only=True)
    ingredients = serializers.CharField(source='kitchen.ingredients', read_only=True)
    flavour = serializers.CharField(source='kitchen.flavour', read_only=True)
    region = serializers.CharField(source='kitchen.region', read_only=True)
    image = serializers.ImageField(source='kitchen.image', read_only=True)
    creation_date = serializers.DateTimeField(source='kitchen.creation_date', read_only=True)
    seasonal = serializers.CharField(source='kitchen.seasonal', read_only=True)

    class Meta:
        model = Reaction
        fields = '__all__'