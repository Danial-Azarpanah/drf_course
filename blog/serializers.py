from rest_framework import serializers

from .models import Article


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=70)
    last_name = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'text', 'status')

    def validate(self, attrs):
        if attrs["title"] == attrs["text"]:
            raise serializers.ValidationError("Title and text can not be the same")

