from rest_framework import serializers
from news.models import (
    Attachment,
    Author,
    News,
    Tag,
)

# creating our model serializers

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

# news has attachments and tags, so we include them, one using related name and other using _set
class NewsSerializer(serializers.ModelSerializer):
    attachment_set = AttachmentSerializer(many=True)
    tags = TagSerializer(many=True)

    class Meta:
        model = News
        fields = '__all__'
