from django.db import models

class Show_Manager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}

        if len(post_data['title']) < 2:
            errors['title'] = "Title should be at least 2 characters"

        if len(post_data['network']) < 3:
            errors['network'] = "Network should be at least 3 characters"

        if len(post_data['desc']) < 10:
            errors['desc'] = "Description should be at least 10 characters"

        return errors


class Show(models.Model):
    title = models.CharField(max_length=30)
    network = models.CharField(max_length=10)
    release_date = models.DateTimeField()
    desc = models.TextField()
    objects = Show_Manager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)