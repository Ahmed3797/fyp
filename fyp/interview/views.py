from django.shortcuts import redirect
from django.views.generic import TemplateView
from company.models import Question
from candidate.models import candidate
from company.models import Interview as inters,User_Answer,Report
from django.contrib import messages
from django.db import transaction

from sentence_transformers import SentenceTransformer, util

roberta_model = SentenceTransformer('roberta-base-nli-mean-tokens')
    
class Interview(TemplateView):
    template_name = 'interview.html'

    def get_context_data(self, **kwargs):
    
        context = super().get_context_data(**kwargs)
        current_user =self.request.user
        data=candidate.objects.get(user__email=current_user.email)
        context["user"]=data
        id=kwargs["id"]
        context["int_id"]=id
        inter=inters.objects.get(id=id)

        questions = Question.objects.filter(interview=inter)
        context["questions"] = questions
        context["interview"] = inter    
        return context

    def render_to_response(self, context, **response_kwargs):
        response = super().render_to_response(context, **response_kwargs)
        if hasattr(response, 'render') and callable(response.render):
            response.render()
        return response
  
    def dispatch(self, request, *args, **kwargs):

        response = super().dispatch(request, *args, **kwargs)
        
        return response
    


@transaction.atomic
def save_answers(request):
    if request.method == 'POST':
        question_ids = request.POST.getlist('question_ids[]')
        interview_id=request.POST.get('inters')
        spoofing=request.POST.get('spoofing_count')
        faces=request.POST.get('unique_faces_detected')
        tab_changing=request.POST.get('tab_changing')

        print(f"spoofing{spoofing} --------- faces{faces}------- tab_chnaging{tab_changing}")
        interview=inters.objects.get(id=interview_id)
        user = request.user
        report_instance = Report.objects.create(user=user,interview=interview,tab_changing=tab_changing,Spoofing_detection=spoofing,copy_pasting=faces)  # Create a report instance
        
        for question_id in question_ids:
            question_text = request.POST.get(f'question_{question_id}')
            try:
                question = Question.objects.get(pk=question_id)
                ques_text=question.answer
            except Question.DoesNotExist:
                messages.error(request, f"Question with ID {question_id} does not exist.")
                return redirect('/')

            # Get the answer for the current question
            answer = request.POST.get(f'question_{question_id}')
            
            # Save the user's answer and relate it to the report
            user_answer = User_Answer.objects.create(question_inter=question, user_answer=answer)

            predefined_answer = ques_text
            predefined_embedding = roberta_model.encode(predefined_answer, convert_to_tensor=True)
            user_answer_embedding = roberta_model.encode(answer, convert_to_tensor=True)
            cosine_similarity = util.pytorch_cos_sim(predefined_embedding, user_answer_embedding)
            similarity_score = cosine_similarity.item()
            
            # You can store the similarity score with the user's answer if needed
            user_answer.semantic_score = similarity_score
            user_answer.save()

            report_instance.user_answers.add(user_answer)
              # Add the user_answer to the report

        
        return redirect('/')
    else:
        # Handle GET request
        pass





