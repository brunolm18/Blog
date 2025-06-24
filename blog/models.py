from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


class TimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    biography = models.TextField()
    image = models.ImageField(upload_to='author_images/', blank=True, null=True)
    experience = models.PositiveIntegerField()
    social_media_url = models.URLField(blank=True, null=True)

    def clean(self):
        errors = {}
        if not self.email.endswith(('@gmail.com', '@hotmail.com')):
            errors['email'] = "Only Gmail or Hotmail are allowed."
        if self.experience <= 0:
            errors['experience'] = "Experience must be greater than 0."
        if errors:
            raise ValidationError(errors)

    def __str__(self):
        return self.username


class AuthorProfile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE, related_name='profile')
    website = models.URLField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.author.username}"


class Post(TimestampMixin):
    class Status(models.TextChoices):
        ACTIVE = 'ACTIVE', 'Active'
        INACTIVE = 'INACTIVE', 'Inactive'

    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')  # 1-N
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')  # 1-N
    tags = models.ManyToManyField(Tag, related_name='posts')  # N-N

    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()
    footer = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    pub_date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.ACTIVE)

    def clean(self):
        if self.pub_date > timezone.now():
            raise ValidationError({'pub_date': "Publication date can't be in the future."})

    def __str__(self):
        return self.title
