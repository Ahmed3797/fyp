from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.views.generic import TemplateView

from .models import candidate,Skill,Eduaction,CVSubmission

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from company.models import Interview,Report
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

# Create your views here.

@method_decorator(login_required, name='dispatch')
class Candidate(TemplateView):
    template_name="candidate.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user =self.request.user
        print(current_user)
        data=candidate.objects.get(user__email=current_user.email)
        context['candidate']=data
        context['image']=data.image
        reports=Report.objects.filter(user=data.user)
        context["reports"]=reports
        interviews = [report.interview for report in reports]
        context["inter"]=interviews
        skill_data=Skill.objects.filter(candidate=data)
        education_data=Eduaction.objects.filter(candidate=data)
        applied_interviews=CVSubmission.objects.filter(applied_candidate=data)
        context["applied_interviews"]=applied_interviews
        context['education_data']=education_data
        context['skill_data']=skill_data
        current_date = datetime.now()
       # Format the current date as "Month day, year"
        formatted_date = current_date.strftime("%B %d, %Y")
       # Pass the formatted date to the template context
        context["current_date"] = formatted_date
        
        print(data)
        context["data"]=data 
        return context


@method_decorator(login_required, name='dispatch')
class Search(TemplateView):
    template_name = "searchinterview.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user =self.request.user
        data=candidate.objects.get(user__email=current_user.email)
        cv_submissions=CVSubmission.objects.filter(applied_candidate=data)
        context['image']=data.image

        # Search interviews
        search_query = self.request.GET.get('search', '')
        interview_list = Interview.objects.filter(name__icontains=search_query).exclude(schedulded=True)
        for interview in interview_list:
            interview.applied = any(cv_submission.interview == interview for cv_submission in cv_submissions)


        # Paginate the results
        paginator = Paginator(interview_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            interviews = paginator.page(page)
        except PageNotAnInteger:
            interviews = paginator.page(1)
        except EmptyPage:
            interviews = paginator.page(paginator.num_pages)

        context['interviews'] = interviews

        return context

    def post(self, request, *args, **kwargs):
  
        current_user =self.request.user

        interview_id=request.POST.get('interview_id')
        print(interview_id)
        cv=request.FILES['cv']
        interview=Interview.objects.get(id=interview_id)
        
        print(interview_id)
        print(cv)
        obj=candidate.objects.get(user__email=current_user.email)
        new_obj=CVSubmission(cv=cv,applied_candidate=obj,interview=interview)
        new_obj.save()

        # If the form is not valid or if there was an error, update the context
        context = self.get_context_data()        
        return render(request, self.template_name, context)


def initial_data(request):
    current_user =request.user
    data=candidate.objects.get(user__email=current_user.email)
    skill_data=list(Skill.objects.filter(candidate=data).values())
    education_data=list(Eduaction.objects.filter(candidate=data).values())
    data=data.desc
    print(data)
    return JsonResponse({'skill_data': skill_data, 'education_data': education_data,'obj':data})


def add_skill_view(request):
    skill_name = request.POST.get('skill_name', '')

    if skill_name:
        current_user =request.user
        obj=candidate.objects.get(user__email=current_user.email)
        skill_obj=Skill(candidate=obj,name=skill_name)
        skill_obj.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'message': 'Skill name is required'})
    


def add_education_view(request):
    Eduaction_name = request.POST.get('education_name', '')
    print(Eduaction_name)

    if Eduaction_name:
        current_user =request.user
        obj=candidate.objects.get(user__email=current_user.email)
        skill_obj=Eduaction(candidate=obj,data=Eduaction_name)
        skill_obj.save()  
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'message': 'Education name is required'})
    


@csrf_exempt
def save_image(request):
    print("asdnaskns")
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        cmp_id = request.POST.get('cmp')
        try:
            comp =candidate.objects.get(id=cmp_id)
            comp.image = image
            comp.save()
            return JsonResponse({'message': 'Image saved successfully.', 'image_url': comp.image.url})
        except candidate.DoesNotExist:
            return JsonResponse({'error': 'Company not found.'}, status=404)
    else:
        return JsonResponse({'error': 'Failed to save image.'}, status=400)



@csrf_exempt
def save_company_name(request):
    if request.method == 'POST':
        candidate_id = request.POST.get('id')
        new_name = request.POST.get('name')

        try:
            company = candidate.objects.get(id=candidate_id)
            company.user.name = new_name
            company.user.save()
            company.save()
            return JsonResponse({'message': 'Company name saved successfully.'})
        except candidate.DoesNotExist:
            return JsonResponse({'error': 'Company not found.'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)
    

@csrf_exempt
def save_bio(request):
    if request.method == 'POST':
        bio = request.POST.get('bio')
        candidate_id = request.POST.get('id')
        try:
            company = candidate.objects.get(id=candidate_id)
            company.desc=bio
            company.save()
            return JsonResponse({'message': 'Company name saved successfully.'})
        except candidate.DoesNotExist:
            return JsonResponse({'error': 'Company not found.'}, status=404)  
        
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)