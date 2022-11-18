from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Record(models.Model):
    date = models.DateField(null=True, blank=True)
    weight = models.FloatField(null=True)
    calories_consumed=models.FloatField(null=True)
    average_weekly_weight=models.FloatField
    average_weekly_calories_consumed=models.FloatField
    calorie_increases=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.calories_consumed) + "- by -" + self.user.username
