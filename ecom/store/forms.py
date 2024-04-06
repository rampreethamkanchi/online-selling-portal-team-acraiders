# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Product, Category, Address,User
from django.forms import ModelForm
# from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.formfields import PhoneNumberField

from phonenumber_field.widgets import PhoneNumberPrefixWidget



class SignUpForm(UserCreationForm, forms.Form):
	# email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	# first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	# last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
	# city = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}))
	# phone= PhoneNumberField(attrs={"size": 10, "title": "Your name"})
	phone = PhoneNumberField(region="IN", widget=PhoneNumberPrefixWidget(
		country_choices=[("IN", "+91")],
		attrs={'class':'form-control', 'placeholder':'Phone number'}
	))
 	# phone = PhoneNumberField(region="IN",

    #     widget=PhoneNumberPrefixWidget(

    #         country_choices=[

    #              ("IN", "+91"),

    #         ],
	# 		attrs={'class':'form-control', 'placeholder':'Phone number'}
    #     ),)
	# phone = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}))
    # phone = PhoneNumberField()
	class Meta:
		model = User
		fields = ('username','first_name', 'last_name', 'password1', 'password2','email')
		# fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		# self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['email'].widget.attrs['class'] = 'form-control'
		self.fields['email'].widget.attrs['placeholder'] = 'Email'
		self.fields['email'].label = ''

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		# self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
		self.fields['first_name'].widget.attrs['class'] = 'form-control'
		self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
		self.fields['first_name'].label = ''
		self.fields['last_name'].widget.attrs['class'] = 'form-control'
		self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
		self.fields['last_name'].label = ''
		self.fields['phone'].widget.attrs['class'] = 'form-control'
		self.fields['phone'].widget.attrs['placeholder'] = 'Phone'
		self.fields['phone'].label = ''
		# self.fields['city'].widget.attrs['class'] = 'form-control'
		# self.fields['city'].widget.attrs['placeholder'] = 'City'
		# self.fields['city'].label = ''

class ProductForm(ModelForm):
	# p_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Product Name'}))
	# price = forms.DecimalField(label="", max_digits=6, decimal_places=2, widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Maximum Retail Price'}))
	# category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Select Category", widget=forms.Select(attrs={'class':'form-control'}))
	# description = forms.CharField(label="", widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}))
	# image = forms.ImageField(label="Upload JPG Image", widget=forms.FileInput(attrs={'class':'form-control'}))
	# city = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}))
	# age = forms.DurationField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Age of Item'}))
	# qunatity = forms.IntegerField(label="", widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Quantity'}))
	# sale_price = forms.DecimalField(label="", max_digits=6, decimal_places=2, widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Sale Price'}))
	class Meta:
		model = Product
		fields = ('p_name','m_name','quantity', 'price','sale_price','city','is_light', 'category', 'description', 'image1','image2','image3','image4','image5', 'age' )
		exclude = ["seller"]

class AddressForm(ModelForm):
	class Meta:
		model= Address
		exclude = ["customer"]