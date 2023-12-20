from rest_framework import serializers
from .models import Namelist

class NamelistSerializers(serializers.ModelSerializer):
    class Meta:
        model= Namelist
        fields=["id","name","classnumber","studentnumber",]

