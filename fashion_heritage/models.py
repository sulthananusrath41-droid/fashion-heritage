from django.db import models

# Create your models here.
class Gown(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gowns/')
    history = models.TextField()
    country_of_origin = models.CharField(max_length=200)
    era = models.CharField(max_length=200)
    designer = models.CharField(max_length=200)
    materials = models.TextField()
    cultural_significance = models.TextField()
    added_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='gowns')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return(f"{self.name}, {self.country_of_origin}")

class Comment(models.Model):
    gown = models.ForeignKey(Gown, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return(f"{self.author}, {self.gown}")

class Like(models.Model):
    gown = models.ForeignKey(Gown, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["user", "gown"]

class Save(models.Model):
    gown = models.ForeignKey(Gown, on_delete=models.CASCADE, related_name='saves')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='saves')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return(f"{self.user}, {self.gown}")

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)

    def __str__(self):
        return self.user.username