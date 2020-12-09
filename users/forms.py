from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _

from .models import Profile, Applicant

GENDER_CHOICE=(
	("Male",_("Male")),
	("Female",_("Female"))
)

SCHOOL_YEAR = (
	('1', '1'),
	('2', '2'),
	('3', '3')
	)

User = get_user_model()

class UserResgiterForm(UserCreationForm):
	region = forms.CharField(label=_('Region'))
	date_of_birth = forms.DateField(label=_('Date of Birth'),
		 widget=forms.TextInput(attrs={'type': 'date'}))       
	phone_number = forms.FloatField(label=_('Phone Number'),
	widget=forms.TextInput(attrs={'placeholder':'ex: 01553057088'}),
	max_value=1599999999, min_value=101111111)
	national_id = forms.FloatField(label=_('National ID'),
	widget=forms.TextInput(attrs={'placeholder':'ex: 30001011801881'}),
	max_value=99999999999999, min_value=10000000000000)
	gender = forms.ChoiceField(label=_('Gender'), choices=GENDER_CHOICE)
	year = forms.ChoiceField(label=_('Grade'), choices=SCHOOL_YEAR)
	email = forms.EmailField(label=_('E-mail'))
	last_name = forms.CharField(label=_('Last Name'))
	first_name = forms.CharField(label=_('First Name'))

	class Meta:
		model = User
		fields = ['first_name', 'last_name' ,'username', 'region', 'email', 'phone_number', 'date_of_birth', 'gender', 'national_id', 'year', 'password1', 'password2']



class UserUpdateForm(forms.ModelForm):
	region = forms.CharField(label=_('Region'))
	date_of_birth = forms.DateField(label=_('Date of Birth'),
		 widget=forms.TextInput(attrs={'type': 'date'}))       
	phone_number = forms.FloatField(label=_('Phone Number'),
	max_value=1599999999, min_value=101111111)
	national_id = forms.FloatField(label=_('National ID'),
	max_value=99999999999999, min_value=10000000000000)
	gender = forms.ChoiceField(label=_('Gender'), choices=GENDER_CHOICE)
	year = forms.ChoiceField(label=_('Grade'), choices=SCHOOL_YEAR)
	email = forms.EmailField()
	last_name = forms.CharField(label=_('Last Name'))
	first_name = forms.CharField(label=_('First Name'))

	class Meta:
		model = User
		fields = ['first_name', 'last_name' ,'username', 'region', 'email', 'phone_number', 'date_of_birth', 'gender', 'national_id', 'year']



class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']


class ApplicantForm(forms.ModelForm):
	class Meta:
		model = Applicant
		fields = ['full_name', 'email', 'date_of_birth',
		'gender','position', 'available', 'personal_image',
		'address', 'phone_number','a_phone_number',
		'national_id', 'college', 'year',
		'how', 'what', 'why']