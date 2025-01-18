from rest_framework import serializers
from .models import Chapter

# 为Chapter模型创建一个序列化器，用于将模型实例转化为 JSON 格式的数据
# 序列化器（Serializer）用于将Django的模型实例或查询集转换为JSON格式的数据。
class ChapterSerializer(serializers.ModelSerializer):
    # serializers.ModelSerializer这是 DRF 提供的一个快捷类，用于快速生成和模型相关的序列化器。
    sub_chapters = serializers.SerializerMethodField()
    class Meta: # 内部类
        model = Chapter # 告诉序列化器这个类对应的模型
        fields = ['id','title','content', 'sub_chapters'] # 指定需要序列化和反序列化的字段。

    def get_sub_chapters(self,obj):
        return ChapterSerializer(obj.sub_chapters.all(),many=True).data