from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Input Text'}))
    last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Input Text'}))
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Input Email'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Input text'
        self.fields['username'].label = 'Username'
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Input password'
        self.fields['password1'].label = 'Password'
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Input password'
        self.fields['password2'].label = 'Confirm Password'
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	

class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Input text", "class":"form-control"}), label="First Name")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Input text", "class":"form-control"}), label="Last Name")
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Input text", "class":"form-control"}), label="Email")
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Input text", "class":"form-control"}), label="Phone Number")
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Input text", "class":"form-control"}), label="Address")
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Input text", "class":"form-control"}), label="City")
    state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Input text", "class":"form-control"}), label="State")
    zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Input text", "class":"form-control"}), label="Zipcode")

    class Meta:
        model = Record
        exclude = ("user",)
