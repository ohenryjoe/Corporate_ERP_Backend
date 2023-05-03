"""pep8"""
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from accounts.models import User
from django.utils.translation import gettext_lazy as _




def get_file_full_url(self, file):
    """pep8"""
    request = self.context.get('request')
    #photo_url = obj.user.profile.profile_pic.url
    return request.build_absolute_uri(file)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Login using username(email) plus password to get the access and refresh tokens
    use the refresh token to renew the access token after expiry. You can decode the access token to get all use info
    """

    @classmethod
    def get_token(cls, user):
        """pep8"""
        token = super().get_token(user)
       
        # Add custom claims
        token['id'] = user.id
        token['email'] = user.email
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        try:
            token['avator'] = user.avatar.url
        except:
            token['avator'] = None
        token['gender'] = user.gender
        token['remarks'] = user.remarks
        token['personal_statement'] = user.personal_statement

        return token

    @classmethod
    def validate(self, attrs):
        """pep8"""
        email = attrs['email']
        password = attrs['password']

        if email and password:
            user = User.objects.filter(
                email=email).first()
         
          
            if user and user.is_active == False:
                msg = _('Please activate your account to login.')
                raise serializers.ValidationError(
                    {'error': msg}, code='authorization')
            if user and  not user.check_password(password):
                msg = _('The password entered is incorrect!.')
                raise serializers.ValidationError(
                    {'error': msg}, code='authorization')
            # checking whether a use has a token or not
            # users. (Assuming the default ModelBackend authentication
            # backend.)

            if not user:
                msg = _('User account not found.Please register.')
                raise serializers.ValidationError(
                    {'error': msg}, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(
                {'error': msg}, code='authorization')

        refresh = self.get_token(user)

        attrs['refresh'] = str(refresh)
        attrs['access'] = str(refresh.access_token)
        attrs.pop("password")
        attrs.pop("email")
        return attrs




class CustomAuthTokenSerializer(serializers.Serializer):
    """pep8"""
    email = serializers.CharField(label=_("email"))
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """pep8"""
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            # user = authenticate(request=self.context.get('request'),
            #                     username=username, password=password)
            user = User.objects.filter(
                email=email).first()
            # The authenticate call simply returns None for is_active=False
            if user and user.is_active == False:
                msg = _('Please activate your account to login.')
                raise serializers.ValidationError(
                    {'error': msg}, code='authorization')
            # checking whether a use has a token or not
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Check if your account exists.')
                raise serializers.ValidationError(
                    {'error': msg}, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(
                {'error': msg}, code='authorization')

        attrs['user'] = user
        return attrs

class UserSerializer(serializers.ModelSerializer):
    """Register a new user"""""   
    class Meta:
        model = User
        depth = 2
        fields = ('id','email','first_name','last_name', 'password','date_joined','avatar','gender','remarks','personal_statement','groups')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):

        # create user
        user = User.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name = validated_data['last_name'],
            password=validated_data['password'],
            avatar = validated_data['avatar'],
            gender = validated_data['gender'],
            remarks = validated_data['remarks'],
            personal_statement = validated_data['personal_statement'],
            is_active=True
        )


        return user