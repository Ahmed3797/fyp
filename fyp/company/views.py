from typing import Any
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .models import company as Comp, Interview, Question
from .forms import InterviewForm, QuestionFormSet,InterviewDateForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from candidate.models import CVSubmission
from candidate.models import candidate as CANDIDATE
from .models import Interview,company as Company,Report
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
# Create your views here.

@method_decorator(login_required, name='dispatch')
class company(TemplateView):
    template_name="company.html"

    def get_context_data(self, **kwargs: Any):
        context= super().get_context_data(**kwargs)
        current_user=self.request.user
        compan = Comp.objects.get(user__email=current_user.email)
        context["company"]=compan
        context["image"]=compan.image
        interviews=Interview.objects.filter(company=compan)
        context["interview"]=interviews
        current_date = datetime.now()
       # Format the current date as "Month day, year"
        formatted_date = current_date.strftime("%B %d, %Y")
       # Pass the formatted date to the template context
        context["current_date"] = formatted_date
        return context

    
@method_decorator(login_required, name='dispatch')
class AddInterview(TemplateView):
    template_name="addinterview.html"

    def get_context_data(self, **kwargs):     
        context = super().get_context_data(**kwargs)
        current_user=self.request.user
        compan = Comp.objects.get(user__email=current_user.email)
        context["image"]=compan.image
        context['interview_form'] = InterviewForm()
        context['formset'] = QuestionFormSet(queryset=Question.objects.none())
        return context

    def post(self, request, *args, **kwargs):
        interview_form = InterviewForm(request.POST,request.FILES)
        formset = QuestionFormSet(request.POST, queryset=Question.objects.none())

        if interview_form.is_valid() and formset.is_valid():
          
            current_user=self.request.user
            compan = Comp.objects.get(user__email=current_user.email)

            interview = interview_form.save(commit=False)
            interview.company = compan
            interview.save()

            questions = formset.save(commit=False)
            for question in questions:
                question.interview = interview
                question.save()

            return redirect('/company', pk=interview.pk)
        
        return render(request, self.template_name, {'interview_form': interview_form, 'formset': formset})
    

class View_CVS(TemplateView):
    template_name="csd.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user=self.request.user
        compan = Comp.objects.get(user__email=current_user.email)
        context["image"]=compan.image
        id = kwargs['id']
        interview=Interview.objects.get(id=id)
        context['id'] = id
        context["name"]=interview.name
        context['app_end']=interview.application_end_date
        candidates=CVSubmission.objects.filter(interview__id=id)
        context['candidates']=candidates 
        interview_date_form = InterviewDateForm(instance=interview)
        context['interview_date_form'] = interview_date_form
        return context
    
    def post(self, request, *args, **kwargs):
    
        interview_id = kwargs['id']
        interview=Interview.objects.get(id=interview_id)
        if 'appr' in request.POST:
            candidate_id = request.POST.get("approve")
            candidate = CANDIDATE.objects.get(id=candidate_id)
            CVSubmission.objects.filter(applied_candidate=candidate, interview=interview).update(status='Approved')
            return redirect("cvs", interview_id)

        elif 'rgt' in request.POST:
            candidate_id = request.POST.get("reject")
            candidate = CANDIDATE.objects.get(id=candidate_id)
            CVSubmission.objects.filter(applied_candidate=candidate, interview=interview).update(status='Pending')
            return redirect("cvs", interview_id)
          
       
        interview_date_form = InterviewDateForm(request.POST, instance=interview)
        if interview_date_form.is_valid():
            interview_date_form.save()
            interview.schedulded=True
            interview.save()
            return redirect("company")
        else:
            # If form is not valid, re-render the template with form errors
            return render(request, self.template_name, {'interview_date_form': interview_date_form, 'id': interview_id})
            
        return redirect("cvs",interview_id)



@csrf_exempt
def save_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        cmp_id = request.POST.get('cmp')
        try:
            comp = Company.objects.get(id=cmp_id)
            comp.image = image
            comp.save()
            return JsonResponse({'message': 'Image saved successfully.', 'image_url': comp.image.url})
        except Company.DoesNotExist:
            return JsonResponse({'error': 'Company not found.'}, status=404)
    else:
        return JsonResponse({'error': 'Failed to save image.'}, status=400)



@csrf_exempt
def save_company_name(request):
    if request.method == 'POST':
        company_id = request.POST.get('id')
        new_name = request.POST.get('name')

        try:
            company = Company.objects.get(id=company_id)
            company.user.name = new_name
            company.user.save()
            company.save()
            return JsonResponse({'message': 'Company name saved successfully.'})
        except Company.DoesNotExist:
            return JsonResponse({'error': 'Company not found.'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)



@csrf_exempt
def save_bio(request):
    if request.method == 'POST':
        bio = request.POST.get('bio')
        company_id = request.POST.get('id')
        try:
            company = Company.objects.get(id=company_id)
            company.desc=bio
            company.save()
            return JsonResponse({'message': 'Company name saved successfully.'})
        except Company.DoesNotExist:
            return JsonResponse({'error': 'Company not found.'}, status=404)  
        
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)


class Reports_view(TemplateView):
    template_name="reports_view.html"

    def get_context_data(self, **kwargs: Any):
        context=super().get_context_data(**kwargs)
        interview_id = kwargs['id']
        interview=Interview.objects.get(id=interview_id)
        context["name"]=interview.name
        data=Report.objects.filter(interview=interview)
        context["reports"]=data
        return context
    

class Reports(TemplateView):
    template_name="report.html"

    def get_context_data(self, **kwargs: Any):
        context=super().get_context_data(**kwargs)
        report_id = kwargs['id']
        data=Report.objects.get(id=report_id)

        answers=data.user_answers.all()
        context["answers"]=answers
        context["report"]=data
        return context