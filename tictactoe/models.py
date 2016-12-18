from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import Concat
from django.utils import timezone

class Game(models.Model):
    id = models.AutoField(primary_key=True)
    user1 = models.ForeignKey('auth.User', related_name='+')
    user2 = models.ForeignKey('auth.User', related_name='+')
    user1_turn = models.BooleanField(default=True)
    state = models.CharField(max_length=36)
    created_date = models.DateTimeField(default=timezone.now)
    finished_date = models.DateTimeField(blank=True, null=True)
    outcome = models.IntegerField(default=-2)
    
    def finish(self, winner):
        if winner == self.user1:
            self.outcome = 1
        elif winner == self.user2:
            self.outcome = 2
        else:
            self.outcome = 0
        self.finished_date = timezone.now()
        self.save()
        
    def winner(self):
        switch = {
            0: null,
            1: self.user1,
            2: self.user2,
        }
        return switch.get(self.outcome, null)

    def __str__(self):
        return self.user1 + " vs " + self.user2
