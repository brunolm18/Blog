from rest_framework import serializers
from blog.models import Author, AuthorProfile, Category, Post, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'image']


class AuthorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorProfile
        fields = ['website', 'phone_number']


class AuthorSerializer(serializers.ModelSerializer):
    profile = AuthorProfileSerializer(read_only=True)
   
    profile_data = AuthorProfileSerializer(write_only=True, required=False)

    class Meta:
        model = Author
        fields = [
            'id', 'username', 'first_name', 'last_name', 'email', 'biography',
            'image', 'experience', 'social_media_url', 'profile', 'profile_data'
        ]

    def create(self, validated_data):
        profile_data = validated_data.pop('profile_data', None)
        author = Author.objects.create(**validated_data)
        if profile_data:
            AuthorProfile.objects.create(author=author, **profile_data)
        return author

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile_data', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if profile_data:
            profile, created = AuthorProfile.objects.get_or_create(author=instance)
            for attr, value in profile_data.items():
                setattr(profile, attr, value)
            profile.save()
        return instance


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), write_only=True)
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True)
    tags = TagSerializer(many=True, read_only=True)
    tags_ids = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True, write_only=True)

    class Meta:
        model = Post
        fields = [
            'id', 'author', 'author_id', 'category', 'category_id', 'tags', 'tags_ids',
            'title', 'description', 'content', 'footer', 'image', 'pub_date', 'status',
            'created_at', 'updated_at'
        ]

    def create(self, validated_data):
        tags = validated_data.pop('tags_ids', [])
        post = Post.objects.create(**validated_data)
        post.tags.set(tags)
        return post

    def update(self, instance, validated_data):
        tags = validated_data.pop('tags_ids', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if tags is not None:
            instance.tags.set(tags)
        instance.save()
        return instance
