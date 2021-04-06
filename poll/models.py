from django.db import models

class PollModel(models.Model):
    question            =   models.TextField()
    option_one          =   models.CharField(max_length=30)
    option_two          =   models.CharField(max_length=30)
    option_three        =   models.CharField(max_length=30)
    option_one_count    =   models.IntegerField(default=0)
    option_two_count    =   models.IntegerField(default=0)
    option_three_count  =   models.IntegerField(default=0)

    def total(self):
        sum = int(self.option_one_count) + int(self.option_two_count) + int(self.option_three_count)
        return sum

    def __str__(self):
        return self.question
