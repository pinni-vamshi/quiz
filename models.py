from django.db import models

# Create your models here.


class Questions(models.Model):
	question = models.CharField(max_length = 200)
	option1 = models.CharField(max_length = 50)
	option2 = models.CharField(max_length = 50)
	option3 = models.CharField(max_length = 50)
	option4 = models.CharField(max_length = 50)
	correct_option = models.CharField(max_length = 50)

	def __str__(self):
		return self.question
		return self.option1
		return self.option2
		return self.option3
		return self.option4
		return self.correct_option
