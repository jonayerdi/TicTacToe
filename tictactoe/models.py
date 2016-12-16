from django.db import models
from django.utils import timezone

class Game(models.Model):
	id = models.AutoField(primary_key=True)
    user1 = models.ForeignKey('auth.User')
	user2 = models.ForeignKey('auth.User')
    created_date = models.DateTimeField(default=timezone.now)
    finished_date = models.DateTimeField(blank=True, null=True)
	is_finished = models.BooleanField(default=0)
	outcome = models.IntegerField(default=-1)
	
    def finish(self, winner):
		if winner == self.user1:
			self.outcome = 1
		elif winner == self.user2:
			self.outcome = 2
		else:
			self.outcome = 0
        self.finished_date = timezone.now()
		self.is_finished = 1
        self.save()
		
	def winner(self):
		switch = {
			0: null,
			1: user1,
			2: user2,
		}
		return switch.get(self.outcome, null)

    def __str__(self):
        return self.id
