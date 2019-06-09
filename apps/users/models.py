''' Model user '''
from django.db import models
#import birthday
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)
from Crypto.PublicKey import RSA
from base64 import b64encode, b64decode
from Crypto.Signature import PKCS1_v1_5

def generate_RSA(bits=2048):
    '''
    Generate an RSA keypair with an exponent of 65537 in PEM format
    param: bits The key length in bits
    Return private key and public key
    '''

    new_key = RSA.generate(bits, e=65537)
    public_key = new_key.publickey().exportKey("PEM")
    private_key = new_key.exportKey("PEM")
    return private_key.decode(), public_key.decode()
def sign_data(private_key, data):
    '''
    param: private_key in PEM format
    param: Data to be signed in base64
    return: base64 encoded signature
    '''
    from Crypto.PublicKey import RSA

    from Crypto.Hash import SHA256
    rsakey = RSA.importKey(private_key)
    signer = PKCS1_v1_5.new(rsakey)
    digest = SHA256.new()
    # It's being assumed the data is base64 encoded, so it's decoded before updating the digest
    digest.update(b64decode(data))
    sign = signer.sign(digest)
    return b64encode(sign)

class UserManager(BaseUserManager):
    def create_user(self, username,birthday,first_name,last_name, email, address,city,country,postal_code, password=None, is_active=True, is_staff=False, is_admin=False, choices="C"):
        if not email:
            raise ValueError("Users must have an email account")
        if not password:
            raise ValueError("Users must have a password")
        if not username:
            raise ValueError("Users must have username") 
        user_obj = self.model(
            email=self.normalize_email(email)
        )
        user_obj.type_of_user = choices
        user_obj.username = username
        user_obj.first_name = first_name
        user_obj.last_name = last_name
        user_obj.address = address
        user_obj.city = city
        user_obj.country = country
        user_obj.postal_code = postal_code
        user_obj.birthday = birthday
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self,username,birthday,first_name,last_name, email, address,city, country,postal_code, password=None):
        user = self.create_user(username,birthday,first_name,last_name, email, address,city,country,postal_code, password=password, is_admin=True)
        return user
    
    def create_staffuser(self, username,birthday,first_name,last_name, email, address,city,country,postal_code, password=None):
        user = self.create_user(username,birthday,first_name,last_name, email, address,city,country,postal_code, password=password, is_staff=True)
        return user

# Create your models here.
class User(AbstractBaseUser):
    ''' Client model '''
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50,blank = True)
    last_name = models.CharField(max_length=50, blank = True)
    address = models.CharField(max_length=100, blank = True)
    city = models.CharField(max_length=50, blank = True)
    country = models.CharField(max_length=50,blank=True)
    #profile_picture = models.ImageField(blank=True)
    postal_code = models.IntegerField(default=0)
    birthday = models.DateField(null=True, blank=True)
    calification = models.IntegerField(default=5)
    about_me = models.CharField(max_length=200,blank=True)
    degree = models.CharField(max_length=50,blank=True)
    #overview =  models.TextField(blank = True,max_length=200)
    #birthday = birthday.fields.BirthdayField()CDMX

    #objects = birthday.managers.BirthdayManager()

    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # staff user non superuser
    admin = models.BooleanField(default=False)
    TYPE_CHOICES = (
        ("C", "Cliente"),
        ("F", "Freelancer"),
    )
    type_of_user = models.CharField(max_length=1, choices=TYPE_CHOICES)
    public_key = models.CharField(max_length=500)
    private_key = models.CharField(max_length=2000,blank=True)
    education = models.CharField(max_length=100,blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','type_of_user','first_name','last_name','address','city','postal_code','birthday','country']
    objects = UserManager()

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.first_name + self.last_name

    def get_short_name(self):
        return self.first_name

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
    def get_age(self):
        from datetime import datetime 
        #born = datetime.strptime(self.birthday, '%Y-%m-%d').date()
        born = self.birthday
        today = datetime.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))



class Skills(models.Model):
    '''skills model '''
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Publication(models.Model):
    '''publication model'''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    freelancer = models.ForeignKey(User,related_name='freelancer_hired', null=True, on_delete = models.SET_NULL)
    name = models.CharField(max_length=50)
    overview = models.CharField(max_length=300)
    date = models.DateField(auto_now=True)
    BUDGET_CHOICES = (
        ('Small project ($250-750 USD)', 'Small project ($250-750 USD)'),
        ('Medium project ($750-1500 USD)', 'Medium project ($750-1500 USD)'),
        ('Big project ($1500-30000 USD)', 'Big project($1500-30000 USD)'),
    )
    budget = models.CharField(max_length=50, choices=BUDGET_CHOICES)
    skills = models.ManyToManyField(Skills)
    progress =  models.IntegerField(default=0)
    

class Postulados(models.Model):
    publication = models.ForeignKey(Publication,related_name='publication',on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    TYPE_CHOICES = (
        ("rechazado", "rechazado"),
        ("aceptado", "aceptado"),
        ("en revision","en revision"),
    )
    state = models.CharField(max_length = 25,choices = TYPE_CHOICES,default = "en revision")

class Contract(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    freelancer = models.ForeignKey(User,related_name='freelancer', null=True, on_delete = models.SET_NULL)
    publication = models.ForeignKey(Publication,related_name='publication2',null=True, on_delete = models.CASCADE)
    delivery = models.DateField(auto_now=False)
    payment = models.IntegerField(default=0)
    client_signature = models.CharField(max_length=500,blank = True)
    freelancer_signature = models.CharField(max_length=500,blank= True)