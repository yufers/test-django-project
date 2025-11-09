from my_app.models import *
from rest_framework import serializers


class SchoolSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = School
       fields = ['id', 'name', 'address', ]


class SClassSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = SClass
       fields = ['id', 'grade', 'school_id']


class StudentSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Student
       fields = ['id', 'name', ]