from rest_framework import serializers

from .models import Project, Pledge
from users.serializers import CustomUserSerializer

class PledgeSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    amount = serializers.IntegerField()
    comment = serializers.CharField()
    anonymous = serializers.BooleanField() 
    # supporter = serializers.CharField(max_length=200)
    supporter = serializers.ReadOnlyField(source='supporter.id')
    project_id = serializers.IntegerField()

    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)

    # class Meta:
    #     model = Pledge
    #     fields = ['id', 'amount', 'comment', 'anonymous', 'project', 'supporter']
    #     read_only_fields = ['id', 'supporter']

class PledgeDetailSerializer(PledgeSerializer):
    # pledges = PledgeSerializer(many=True, read_only=True)

    # class Meta:
    #     model = Pledge
    #     fields = ['id', 'amount', 'comment', 'anonymous', 'project', 'supporter']
    #     read_only_fields = ['id', 'supporter']

    def update(self, instance, validated_data):
        instance.amount = validated_data.get('amount', instance.amount)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.anonymous = validated_data.get('anonymous', instance.anonymous)
        instance.supporter = validated_data.get('supporter',instance.supporter)
        # instance.project = validated_data.get('project', instance.project)
        instance.save()
        return instance

class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    goal = serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    owner = serializers.ReadOnlyField(source='owner_id')
    total = serializers.ReadOnlyField()
    pledges = PledgeSerializer(many=True, read_only=True)
    

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

    # class Meta:
    #     model = Pledge
    #     fields = ['id', 'amount', 'comment', 'anonymous', 'project', 'supporter']

class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)
    liked_by = CustomUserSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance
