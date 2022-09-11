from rest_framework import serializers

from .models import Article


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=70)
    last_name = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)


def check_title(value):
    if value["title"] == "html":
        raise serializers.ValidationError({"title": "Title can't be html"})


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'text', 'status')
        validators = [check_title]

    def validate(self, attrs):
        if attrs["title"] == attrs["text"]:
            raise serializers.ValidationError("Title and text can not be the same")
        return attrs

