from django.db import models
from django.utils.translation import ugettext_lazy as _


GENDER_CHOICE=(
	("Male","Male"),
	("Female","Female")
)

SCHOOL_YEAR = (
	('1', '1'),
	('2', '2'),
	('3', '3')
	)

SUBJECT_CHOICE = (
	("Arabic",_("Arabic")),
	("English",_("English")),
	("biology",_("biology")),
	("Geology",_("Geology")),
	("Maths",_("Maths")),
	("science",_("science")),
	("Deutsch",_("Deutsch")),
	("French",_("French")),
	('Italian', _('Italian')),
	('Statistics', _('Statistics')),
	('Physics', _('Physics')),
	('Chemistry', _('Chemistry')),
	('philosophy', _('philosophy')),
	('psychology', _('psychology')),
	('Geography', _('Geography')),
	('history', _('history')),
	('Chinese', _('Chinese')),
	('Spanish', _('Spanish')),
	('Studies', _('Studies')),
	('None', 'None'),
	)

category_choice=(
	("أزهر","أزهر"),
	("لغات","لغات"),
	("عام","عام"),
	)

class Year(models.Model):
	name = models.CharField(max_length=255)
	slug = models.SlugField()

	def __str__(self):
		return self.name

class Teacher(models.Model):
	name = models.CharField(max_length=255)
	subject = models.CharField(choices=SUBJECT_CHOICE, max_length=255)
	address = models.CharField(_('Address'), max_length=512)
	slug = models.SlugField()
	rating = models.FloatField()
	years = models.ManyToManyField(Year)
	description = models.TextField(blank=True, null=True)
	image = models.ImageField(default='default.jpg', upload_to='NewTeacher')

	def __str__(self):
		return self.name


class Class(models.Model):
	uuid = models.CharField(max_length=10)
	name = models.CharField(max_length=255)
	number = models.IntegerField(default=0)
	start_at = models.DateTimeField()
	max_number = models.IntegerField()
	teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
	year = models.ForeignKey(Year, on_delete=models.CASCADE)
	is_privte = models.BooleanField(default=False)
	girls_only = models.BooleanField(default=False)
	
	semster = models.CharField(choices=SCHOOL_YEAR, max_length=255)
	is_online = models.BooleanField(default=False)

	def __str__(self):
		return self.name

	def has_place(self):
		if self.max_number > self.number:
			return True
		else:
			return False

	def remaining(self):
		num = self.max_number - self.number
		if num > 100:
			return 'Open'
		else:
			return num

	class Meta:
		verbose_name_plural = "classes"

class Applicant(models.Model):
	name = models.CharField(_('Full Name'), max_length=255)
	passcode = models.CharField(max_length=255)
	address = models.CharField(_('Address'), max_length=512)
	uuid = models.CharField(max_length=10)
	phone_number = models.FloatField(_('Phone Number'))
	a_phone_number = models.FloatField(_('Parent Phone Number'))
	timestamp = models.DateTimeField(auto_now_add=True)
	gender = models.CharField(_('Gender'), choices=GENDER_CHOICE, max_length=255)
	school_type = models.CharField(choices=category_choice, default="عام" ,max_length=255)
	classe = models.ForeignKey(Class, on_delete=models.CASCADE)
	email = models.EmailField()

	def __str__(self):
		return self.name