# import feeder
# print 'memeha'
# print feeder.__file__
from rest_framework import serializers
from distribution.models import D_OverheadLine,\
D_OverheadLineConfig,\
D_LineSpacing,\
D_OverheadLineConductor


class DOverheadLineConductorSerializer(serializers.ModelSerializer):
    class Meta:
        # depth = 1
        model = D_OverheadLineConductor
        fields = '__all__'

class DLineSpacingSerializer(serializers.ModelSerializer):
    class Meta:
        # depth = 1
        model = D_LineSpacing
        fields = '__all__'

class LineSpacingField(serializers.RelatedField):
    queryset = D_LineSpacing.objects.all()
    def to_representation(self, value):
        print 'customer-kj', type(value)
        return {
            'id': value.id,
            'name': value.name
        }
    def to_internal_value(self, data):
        return None


class DOverheadLineConfigSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=500)
    # spacing = LineSpacingField()
    # spacing = DLineSpacingSerializer(
    #     # many=True,
    #     read_only=True,
    #     # slug_field='name'
    #  )
    # conductor_A = serializers.SlugRelatedField(
    #     # many=True,
    #     read_only=True,
    #     slug_field='name'
    #  )
    # conductor_B = serializers.SlugRelatedField(
    #     # many=True,
    #     read_only=True,
    #     # queryset = DOverheadLineConductor.objects.all(),
    #     slug_field='name'
    #  )
    # conductor_C = serializers.SlugRelatedField(
    #     # many=True,
    #     read_only=True,
    #     slug_field='name'
    #  )
    # conductor_N = serializers.SlugRelatedField(
    #     # many=True,
    #     read_only=True,
    #     slug_field='name'
    #  )
    # def create(self, validated_data):
    #     print validated_data
    #     d_ovheadline_config = DOverheadLineConfig.objects.create(name=validated_data['name'])
    #     return d_ovheadline_config
    class Meta:
        # depth = 1
        model = D_OverheadLineConfig
        fields = '__all__'

class DOverheadLineSerializer(serializers.ModelSerializer):
    # configuration = DOverheadLineConfigSerializer(read_only=True)
    feeder = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    fromWhere = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    toWhere = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    class Meta:
        # depth = 2
        model = D_OverheadLine
        fields = '__all__'
