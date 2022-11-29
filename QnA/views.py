from django.shortcuts import render , redirect ,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from .forms import QuestionForm, AnswerForm
from main.forms import HashtagForm 
from django.utils import timezone
from QnA.models import Question, Answer 
from main.models import Hashtag
from django.http import request
from django.core.paginator import Paginator
# Create your views here.

#질문 작성
def q_write(request, qna = None  , hashtag = None):
        if not request.user.is_authenticated:
            return redirect('login')
        if request.method == 'POST':
            form = QuestionForm(request.POST, request.FILES,instance = qna)
            if form.is_valid():
                    qna = form.save(commit=False)
                    qna.q_date = timezone.now()
                    qna.user = request.user
                    qna.save()
                    form.save_m2m()
                    return redirect('q_list')
        else:
            form = QuestionForm (instance= qna)
            return render(request, 'q_write.html' , {'form':form})

#질문 목록
def q_list(request):
    qnaobj = Question.objects
    q_sort = request.GET.get('q_sort','') #정렬
    if q_sort == 'q_clicks' :
        qnaobj = Question.objects.all().order_by('-q_clicks')#모델 오브젝트 templates에서 받고 싶은 요소만 추가
    else :
        qnaobj = Question.objects.all().order_by('-q_date')
    
    #페이지
    paginator = Paginator(qnaobj, 4)
    page = request.GET.get('page')
    qnaobj = paginator.get_page(page)
    return render(request, 'q_list.html' , {'qnaobj':qnaobj, 'q_sort':q_sort})

#질문글 상세페이지
def q_detail(request, id):
    qna = get_object_or_404(Question, id=id)
    answer_form = AnswerForm()
    return render(request, 'q_detail.html' , {'qna' : qna , 'answer_form':answer_form})

def q_edit(request , id):
        qna = get_object_or_404(Question, id=id)
        if request.method == "POST":
            form = QuestionForm(request.POST, request.FILES, instance=qna)
            if form.is_valid():
                    form.save(commit=False)
                    form.save()
                    return redirect('q_list')
        else:
            form = QuestionForm(instance=qna)
            return render(request, 'q_edit.html' , {'form':form})

#질문 삭제
def q_delete(request, id):
    qna = get_object_or_404(Question, id=id)           
    qna.delete()
    return redirect('q_list')

#좋아요 
def q_likes(request, id):
    like_q = get_object_or_404(Question, id=id)
    if request.user in like_q.q_like.all(): 
        like_q.q_like.remove(request.user)
        like_q.q_like_count -= 1
        like_q.save()
    else:
        like_q.q_like.add(request.user)
        like_q.q_like_count += 1
        like_q.save()
    return redirect('q_detail' , like_q.id) #redurect로 전달 하기 때문에 조회수 올라감..
#검색하기
def q_search(request):
        if request.method == 'POST':
                q_searched = request.POST['q_searched']        
                q_serobj = Question.objects.filter(question__contains=q_searched)
                return render(request, 'q_search.html', {'q_searched': q_searched,'q_serobj':q_serobj})
        else:
                return render(request, 'q_search.html', {})
#댓글 입력
def answer_write(request, question_id):
    qna = get_object_or_404(Question,id=question_id)
    answer_form = AnswerForm(request.POST ,request.FILES)
    if answer_form.is_valid():
        answer = answer_form.save(commit=False)
        answer.user = request.user
        answer.qna_id = qna
        answer.save()
        
    return redirect('q_detail',question_id)

def answer_edit(request, answer_id , question_id):
    qna = get_object_or_404(Question, id = question_id)
    answer = get_object_or_404(Answer, id = answer_id)

    if request.user != answer.user:
        return redirect('login')

    if request.method == 'POST':
        answer_form = AnswerForm(request.POST, request.FILES, instance=answer)
        if answer_form.is_valid():
            answer_form.save()
        return redirect('q_detail',question_id)
    
    else:
        answer_form = AnswerForm(instance=answer)
        return render(request, 'answer_edit.html', {'qna':qna,'answer_form':answer_form})

@require_http_methods(['GET', 'POST'])
def answer_delete(request, question_id, answer_id):
    qna = get_object_or_404(Question, id=question_id)
    answer = get_object_or_404(Answer, id=answer_id)
    
    if answer.user != request.user:
        return redirect('q_detail',question_id)

    answer.delete()

    return redirect('q_detail',question_id)
