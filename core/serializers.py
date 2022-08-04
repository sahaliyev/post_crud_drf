from .models import News, Comments
from rest_framework import serializers


class NewSerializer(serializers.ModelSerializer):
    comments = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='comment-detail'
    )

    class Meta:
        model = News
        fields = '__all__'



class CommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = '__all__'