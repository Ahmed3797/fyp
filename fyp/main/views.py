from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .forms import MyForm
from candidate.models import candidate
from company.models import company
from django.contrib.auth import get_user_model,authenticate,login
from django.http import HttpResponse
from  . models import CustomUser
from django.contrib.auth import logout
from django.shortcuts import redirect

class signup(TemplateView):
    template_name='Signup.html'

    def  post(self, request, *args, **kwargs):
        form = MyForm(request.POST)
        if form.is_valid():
            user_type = form.cleaned_data['user_type']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
          
            user=CustomUser(name=name,email=email,password=password,position=user_type)
            if user_type =='candidate':
              oks=candidate(user=user)
            elif user_type=='company':
                oks=company(user=user)
            user.save()
            oks.save()
            user = authenticate(request, email=email, password=password)
            print(user)
                   
            login(request, user)
            if user.position=='candidate':
                return redirect("candidate")
            elif user.position=='company':
                return redirect("company")
           

        return self.render_to_response({'form': form})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MyForm()
        return context
    

    
class Login(TemplateView):
    template_name="login.html"

    def get(self, request):
        return render(request, 'login.html')

    def post(self,request):
        print("Hello I am in")
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,password)
        user = authenticate(request, email=email, password=password)
        print(user)
        if user is not None:       
            login(request, user)
            if user.position=='candidate':
                return redirect("candidate")
            elif user.position=='company':
                return redirect("company")
            return HttpResponse("Succesfully login")
        else: 
            return render(request, self.template_name,{'Error': 'Invalid email or password'} )
        

class Home(TemplateView):
    template_name="index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            user=self.request.user
            entity=""
            img=""
            if user :
                if user.position=='candidate':
                   entity=candidate.objects.get(user=user)
                   img=entity.image
                elif user.position=='company':
                   entity=company.objects.get(user=user)
                   img=entity.image
                context["image"]=img
                return context
            else:
                context["image"]="no"

        except:          
           return context


def logout_view(request):
    logout(request)
    # Redirect to a success page or homepage
    return redirect('/')


def goto(request):
    try:
        user=request.user
        if user is not None:
            if user.position=='candidate':
              return redirect("candidate")
            elif user.position=='company':
              return redirect("company")
    except:
          return 

