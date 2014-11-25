from marshmallow import Serializer, fields

class UserSerializer(Serializer):
  class Meta:
    felds = ('id','email')

class PostSerializer(Serializer):
  user = fields.Nested(UserSerializer)

  class Meta:
    fields = 'id','title','body','uder','created_at')
