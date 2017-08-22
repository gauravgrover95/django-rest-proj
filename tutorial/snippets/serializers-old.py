from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100, allow_blank=True, required=True)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    lineos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """"
        Create and return a new 'Snippet' instance, given the validated data 
        """

        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return existing 'Snippet' instance, given the validated data
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.style = validated_data.get('style', instance.style)
        instance.language = validated_data.get('language', instance.language)
        instance.lineos = validated_data.get('lineos', instance.lienos)
        instance.save()
        return instance