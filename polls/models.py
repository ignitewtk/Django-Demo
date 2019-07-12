from django.db import models

# Create your models here.
import datetime
from django.db import models
from django.utils import timezone

# A Question has a question and a publication date
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # not only for your own convenience when dealing with interactive prompt,
    # but also because objects' representations are used through Django's
    # automatically-generated admin
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Publisheed recently?'

#  A Choice has two fields: the text of the choice and a vote tally.
# Each Choice is associated with a Question.
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text