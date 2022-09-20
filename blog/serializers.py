from rest_framework import serializers

from .models import Article


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=70)
    last_name = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)


def check_title(value):
    """
    Function based validator to prevent the title from being "html"
    """
    if value["title"] == "html":
        raise serializers.ValidationError({"title": "Title can't be html"})


class CheckTitle:
    """
    Class based validator to prevent the title from being "html"
    """
    def __call__(self, value):
        if value["title"] == "html":
            raise serializers.ValidationError("This title is invalid")


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'text', 'status', 'user')
        validators = [CheckTitle()]

    def validate(self, attrs):
        # Prevent title and text being the same
        if attrs["title"] == attrs["text"]:
            raise serializers.ValidationError("Title and text can not be the same")
        return attrs

    # Save new article with user data
    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["user"] = request.user
        return Article.objects.create(**validated_data)

