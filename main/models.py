from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image


status = (
			("Accepted", "Accepted"),
			("Rejected", "Rejected"),	
			("Pending", "Pending")		
		)
completed = (
	("Yes", "Yes"),
	("No", "No"),
	)

# Create your models here.
class Supervisor(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.user}'

chapters = (
	("Chapter One", "Chapter One"),
	("Chapter Two", "Chapter Two"), 
	("Chapter Three", "Chapter Three"),
	("Chapter Four", "Chapter Four"),
	("Chapter Five", "Chapter Five"),
	)

class Chapter(models.Model):
	chapter_number = models.CharField(max_length=100, null=True, choices=chapters)
	file = models.FileField(upload_to="files")
	student = models.ForeignKey(User, on_delete=models.CASCADE)
	supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
	supervisor_remarks = models.TextField(null=True, blank=True, default="--")
	status = models.CharField(max_length=100, choices=status, default="Pending")

	def __str__(self):
		return f'{self.chapter_number} - {self.student}'


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)		
	image = models.ImageField(upload_to='profile', default='default.jpg')
	project_title = models.CharField(max_length=200, null=True, default="--")
	project_summary = models.TextField(blank=True, null=True, default="--")

	def __str__(self):
		return f'{self.user}'

	def super(self, *args, **kwargs):
		super.save()
		img = Image.open(self.image.path)
		img_size = (300, 300)
		img.thumbnail(img_size)
		img.save(self.image.path)

def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)	

post_save.connect(create_profile, sender=User)

# def save_profile(sender, instance, **kwargs):
# 	instance.profile.save()

# post_save.connect(save_profile, sender=User)


class RequestMeeting(models.Model):
	date = models.DateTimeField(auto_now_add=True)
	additional_informaton = models.CharField(max_length=200, null=True)
	student = models.ForeignKey(User, on_delete=models.CASCADE)
	supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.date} - {self.supervisor}'


class ProjectStatus(models.Model):
	status = (
			("Accepted", "Accepted"),
			("Rejected", "Rejected"),	
			("Pending", "Pending")		
		)
	status = models.CharField(max_length=50, choices=status, default="Pending")
	complete = models.CharField(max_length=100, choices=completed, default="No")
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

	def __str__(self) -> str:
		return f'{self.profile} - {self.status}'


def create_project_status(sender, instance, created, *args, **kwargs):
	if created:
		ProjectStatus.objects.create(profile=instance)

post_save.connect(create_project_status, sender=Profile)
