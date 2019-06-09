'''vistas Usuarios '''
#from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.http import HttpResponse
from django.shortcuts import redirect, render
from apps.users.forms import PublicationForm
from apps.users.forms import ContractForm
from apps.users.models import Publication
from apps.users.models import User
from apps.users.models import Postulados
from apps.users.models import Contract
from apps.users.forms import RegisterForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from apps.users.models import sign_data
# Create your views here.
from django.http import HttpResponseRedirect

from base64 import b64encode, b64decode
from Crypto.Signature import PKCS1_v1_5
      
class RegisterView(CreateView):
   form_class = RegisterForm
   
   template_name = 'users/registrar.html'
   success_url = reverse_lazy('users:user_index')
   
   
   def form_valid(self,form_class):
      username = self.request.POST['username']
      password = self.request.POST['password1']
      user = form_class.save()
      #new_user = authenticate(username=username,password=password)
      login(self.request,user)
      return HttpResponseRedirect(self.success_url)

def get_user_profile(request,username):
   #current_user = User.objects.get(username=request.user.username)
   age = request.user.get_age()
   if request.user.type_of_user == 'C':
      publications = Publication.objects.filter(user_id = request.user.id)
  
      context = {
        'current_user': request.user,
        'publications':publications,
        'age': age,
        }
      return render(request, 'users/ClientProfile.html',context)
   else:
      print("----------->" + str(request.user.id))
      publications = Publication.objects.filter(freelancer_id = request.user.id)
      context = {
        'current_user': request.user,
        'publications':publications,
        'age': age,
        }
      return render(request,'users/FreelancerProfile.html', context)       

def user_index(request):
   age = request.user.get_age()
   publications = Publication.objects.all()
   publications_client = Publication.objects.filter(user_id = request.user.id)
   current_user = request.user
   #aux = Auxiliar()
   for p in publications:
          name_user = User.objects.get(pk=p.user_id)
          p.user_id = name_user
          
   context = {
      'current_user': current_user,
      'publications': publications,
      'aux': Auxiliar,
      'age': age,
   }
   if request.user.type_of_user == "F":
     
      print("ES FREELANCER")
      return render(request,'users/userIndex.html',context)
   else:
      context["publications"] = publications_client
      print("ES CLIENTE")
      return render(request, 'users/ClientProfile.html',context)
          
class Auxiliar(object):
      def get_user(self,id_u):
            return User.objects.filter(id = id_u)

def postularse(request,id_publication):
      #print(request.POST.get('id_publicatio '))
      print("------------>"+str(id_publication))
      print("------------>" + request.user.username)
      new_postulado = Postulados(user_id = request.user.id,publication_id = id_publication)
      p = Postulados.objects.filter(user_id = request.user.id, publication_id = id_publication)
      print(p);
      context = {
         'current_user': request.user,
         'publication': id_publication,
         'error': len(p),
      } 
      if len(p) > 0:
         return render(request,"users/postularse.html",context)
      else:
         new_postulado.save()
         return render(request,"users/postularse.html",context)

def aceptar_rechazar(request,id_publication,username,value):
       print(value)
       postulados = Postulados.objects.filter(publication_id = id_publication)
       user_postulado = User.objects.get(username = username)
       print(user_postulado.id)
       if value == 'aceptado':
              for p in postulados:
                     if(p.user_id != user_postulado.id):
                        p.state = "rechazado"
                        p.save()
                     
                     else:
                            p.state = "aceptado" 
                            p.save()
       elif value == 'rechazado':
         user_postulado = Postulados.objects.get(user_id = user_postulado.id,publication_id = id_publication)
         print(user_postulado)
         user_postulado.state = "rechazado"
         user_postulado.save()

       context = {
          'current_user':request.user,
          'publication': id_publication,
          'postulado': username,
          'state': value,
       }
       return render(request,"users/aceptar_rechazar.html",context)
      

def publication_show(request,id_publication):   
   publication = Publication.objects.get(pk=id_publication)
   publication.user_id = User.objects.get(pk = publication.user_id)
   skills = publication.skills.filter(publication=id_publication)
   postulados = Postulados.objects.filter(publication_id = id_publication)
   accepted = Postulados.objects.filter(publication_id = id_publication,state = "aceptado")
   flag = False
   if len(accepted) > 0:
      flag = True
   
   print("------------")
   print(accepted)
   for p in postulados:
      username = User.objects.get(pk=p.user_id)
      p.user_id = username.username
   #print(skills[0].name)

   context = {
      'current_user': request.user,
      'publication': publication,
      'skills':skills,
      'postulados': postulados,
      'flag': flag

   } 
   return render(request,'users/publication.html', context) 

def contract_client_sign(request, id_contrato,username,value):
       context = {
          'current_user' : request.user
       }
       contrato = Contract.objects.get(id = id_contrato)
       texto = (str(contrato.delivery) + str(contrato.payment)).encode()
       publication = Publication.objects.get(id = contrato.publication_id)
       cliente = User.objects.get(id = contrato.client_id)
       if value=="aceptar":
              contrato.id_freelancer = request.user.id
              #contrato.freelancer_signature = sign_data(request.user.private_key.encode(),b64encode(texto))
              contrato.freelancer_signature = sign_data(request.user.private_key.encode(),b64encode(texto)).decode()
              contrato.save()
              publication.freelancer_id = request.user.id
              publication.save()
      
       return render(request,'users/contract_signed.html', context)
       
def publication_new(request):
   context = {}
   #context['current_user'] = request.user
   if request.method == 'POST':
      form = PublicationForm(request.POST)
      context['form'] = form
      if form.is_valid():
         np = form.save(commit=False)
         np.user_id = request.user.id
         skills = request.POST.getlist('skills')
         print(skills)
         np.save()
         for i in skills:
            np.skills.add(i)    
      return HttpResponseRedirect(reverse('users:get_user_profile',kwargs={'username':request.user.username}))
   else:
      form = PublicationForm()
   return render(request,'users/publication_form.html/',{'form':form,'current_user':request.user})

def contract_new(request,id_publication,username):
      context = {}
      user_postulado = User.objects.get(username = username)
      publication = Publication.objects.get(id = id_publication)
      if request.method == 'POST':
         form = ContractForm(request.POST)
         context['form'] = form
         if form.is_valid():
            n = form.save(commit=False)
            texto = (str(n.delivery) + str(n.payment)).encode()
            #print(type(request.user.private_key))
            n.client_signature = sign_data(request.user.private_key.encode(),b64encode(texto)).decode()
            print(n.client_signature)
            n.client_id = request.user.id
            n.freelancer_id = user_postulado.id
            n.publication_id = id_publication
            n.save()
         return HttpResponseRedirect(reverse('users:get_user_profile',kwargs={'username':request.user.username}))
      else:
         form = ContractForm()
         for field in form:
                print(field.label_tag())
         context = {
            'form':form,
            'current_user':request.user,
            'd':field.label_tag(),
            'publication' : publication,

         }
      return render(request,'users/contract_form.html/',context)

def contract_show(request,id_publication,username):
       user_postulado = User.objects.get(username = username)
       publication = Publication.objects.get(id = id_publication)
       try:
          contrato = Contract.objects.get(publication_id = id_publication)
          client = User.objects.get(id=contrato.client_id)
          c = True
          context = {
          'contrato' : contrato,
          'publication':publication,
          'current_user':request.user,
          'client':client,
          'c' : c,
          }
       except Contract.DoesNotExist:
          contrato = None
          c = False   
          context = {
          'publication':publication,
          'current_user':request.user,
          'c':c,
          }    
       
       
       return render(request,'users/contract_show.html/',context)

def publication_list(request):
   publications = Publication.object.all()
   context =   {'publications':publications}
   return render(request, 'publicaciones/publicaciones_list.html', context)

def publication_edit(request,id_Publication):
   publication = Publication.object.get(id=id_Publication)
   if request.method == 'GET':
      form = PublicationForm()  
   else:
      form = PublicationForm(request.POST,instance=publication)
      if form.is_valid():
         form.save()
      return redirect('users:list_publication')
   return render(request,'users/publication_form.html',{'form':form})

def publication_delete(request, id_Publication):
   publication = Publication.object.get(id=id_Publication)
   if request.method == 'GET':
      publication.delete()  
      return redirect('users:list_publication')
   return render(request,'users/publication_delete.html',{'publication':publication})

def terminosycondiciones(request):
   return render(request,'users/terminosycondiciones.html')
