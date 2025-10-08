from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """ Serializers do change the json response from the web to the required python data types, works as files """
    """ take care of the validations"""

    name = serializers.CharField(max_length=10)
    