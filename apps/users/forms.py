'''forms'''
from django import forms
from apps.users.models import Publication
from apps.users.models import User
from apps.users.models import Contract
from apps.users.models import generate_RSA
from django.contrib.auth import authenticate, login
class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication

        fields = [
            'name',
            'overview',
            'budget',
            'skills',
        ]
        labels = {
            'name' : 'Nombre',
            'overview' : 'Descripción',
            'budget' : 'Presupuesto',
            'skills' : 'Habilidades requeridas',
        }
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control '}),
            'overview' : forms.TextInput(attrs={'class':'form-control'}),
            'budget' : forms.Select(attrs={'class':'form-control'}),
            'skills' : forms.CheckboxSelectMultiple(),
        }

class ContractForm(forms.ModelForm):
    '''delivery = forms.DateTimeField(label="Fecha de entrega",
        input_formats=['%Y/%m/%d'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )'''
    class Meta:
        model = Contract

        fields = [
            'delivery',
            'payment',
        ]
        labels = {
            'delivery' : 'Fecha de entrega',
            'payment' : 'Pago',
        }
        widgets = {
            'Fecha de entrega' : forms.DateInput(attrs={'class':'form-control'}),
            'Pago' : forms.NumberInput(attrs={'class':'form-control'}),
        }


class RegisterForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control '}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'class':'form-control '}))

    class Meta:
        model = User
        fields = ('username', 'email','type_of_user','first_name','last_name','address','city','country','postal_code','birthday') #'full_name',)
        labels = {
            'username' : 'Nombre de usuario',
            'email': 'Email',
            'type_of_user': 'Tipo de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'address' : 'Direccion',
            'city' : 'Ciudad',
            'country': 'Pais',
            'postal_code': 'Codigo Postal',
            'birthday': 'Fecha de nacimiento',
            'education': 'Educacion',
            'about_me': 'Sobre mi',
            'degree': 'Carrera'
        }
        
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control '}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'type_of_user' : forms.Select(attrs={'class':'form-control '}),
            'first_name' : forms.TextInput(attrs={'class':'form-control '}),
            'last_name' : forms.TextInput(attrs={'class':'form-control '}),
            'address' : forms.TextInput(attrs={'class':'form-control '}),
            'city' : forms.TextInput(attrs={'class':'form-control'}),
            'country' : forms.TextInput(attrs={'class':'form-control'}),
            'birthday': forms.DateInput(attrs={'class' : 'form-control'}), 
            'education': forms.TextInput(attrs={'class':'form-control'}),
            'degree': forms.TextInput(attrs={'class':'form-control'}),
            'about_me': forms.TextInput(attrs={'class':'form-control'})
        }
        

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.active = True # send confirmation email
        keys = generate_RSA()
        user.public_key = keys[1]
        user.private_key = keys[0]
        if commit:
            user.save()
        return user