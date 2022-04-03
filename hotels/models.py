from django.db import models
from django.utils.text import Truncator
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Hotel(models.Model):
    name = models.CharField(max_length=250)
    address = models.TextField(null=True, blank=True)
    stars = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Category(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"


class Room(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=250)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    options = models.TextField(max_length=250, null=True)
    picture = models.ImageField(upload_to="images/")
    picture_thumbnail = ImageSpecField(
        source="picture",
        processors=[ResizeToFill(100, 50)],
        format="JPEG",
        options={"quality": 60},
    )
    size = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "room"
        verbose_name_plural = "rooms"


class Picture(models.Model):
    picture = models.ImageField(upload_to="images/")
    room = models.ForeignKey(
        Room, on_delete=models.SET_NULL, null=True, related_name="pictures"
    )


class Review(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    def __str__(self):
        return self.short_comment

    class Meta:
        verbose_name = "review"
        verbose_name_plural = "reviews"

    @property
    def short_comment(self):
        truncator = Truncator(self.comment)
        return truncator.chars(20)


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
