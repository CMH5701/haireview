from email.policy import default
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from review.forms import ReviewForm, r_commentForm
from django.utils import timezone
from review.models import Review, R_comment
from main.models import Hashtag
from django.http import request
from django.core.paginator import Paginator

# Create your views here.

#리뷰 작성
def r_write(request, review = None) :

    if not request.user.is_authenticated:
        return redirect('login') #로그인 하지 않고 작성하려고 할시 main으로 이동

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance = review)
        if form.is_valid():
            review = form.save(commit=False)
            review.r_date = timezone.now() 
            review.user = request.user
            review.save()
            form.save_m2m()
                
            return redirect('r_list')
    else:
        form = ReviewForm(instance = review)
        return render(request, 'r_write.html', {'form':form })

#리뷰 목록
def r_list(request):
    reviews = Review.objects
    r_sort = request.GET.get('sort', '') 
    if r_sort == 'r_clicks':
        reviews = Review.objects.all().order_by('-r_clicks','-r_date' , 'r_like_count')
    else:
        reviews = Review.objects.all().order_by('-r_date')

    #페이지
    paginator = Paginator(reviews, 4)
    page = request.GET.get('page')
    reviews = paginator.get_page(page)
    return render(request, 'r_list.html', {'reviews':reviews, 'sort':r_sort})

#리뷰 글 상세페이지
def r_detail(request, id):
    review = get_object_or_404(Review, id=id)
    r_commentform = r_commentForm()
    return render(request, 'r_detail.html', {'review':review, 'r_commentform':r_commentform})


#리뷰 수정
def r_edit(request, id):
    review = get_object_or_404(Review, id=id)

    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('r_list')
    else:
        form = ReviewForm(instance=review)
        return render(request, 'r_edit.html', {'form':form})

#리뷰 삭제
def r_delete(request, id):
    review = get_object_or_404(Review, id=id)
    review.delete()
    return redirect('r_list')

#좋아요 
def r_likes(request, id):
    like_r = get_object_or_404(Review, id= id)
    if request.user in like_r.r_like.all():
        like_r.r_like.remove(request.user)
        like_r.r_like_count -= 1
        like_r.save()
    else:
        like_r.r_like.add(request.user)
        like_r.r_like_count += 1
        like_r.save()
    return redirect('r_detail' , like_r.id)

#추천수 
def r_clip(request, r_id):
    like_b = get_object_or_404(Review, id=r_id)
    if request.name in like_b.r_clip.all():
        like_b.r_clip.remove(request.name)
        like_b.r_clips -= 1
        like_b.save()
    else:
        like_b.r_clip.add(request.name)
        like_b.r_clips += 1
        like_b.save()
    return redirect('/r_detail/' + str(r_id))

#검색
def r_search(request):
        if request.method == 'POST':
                r_searched = request.POST['r_searched']        
                r_serobj = Review.objects.filter(r_title__contains=r_searched)
                return render(request, 'r_search.html', {'r_searched': r_searched,'r_serobj':r_serobj})
        elif request.method == 'POST' :
                r_searched = request.POST['r_searched']        
                r_serobj = Review.objects.filter(r_body__contains=r_searched)
                return render(request, 'r_search.html', {'r_searched': r_searched,'r_serobj':r_serobj})
        else:       
                return render(request, 'r_search.html', {})

def r_commentwrite(request, review_id):
    review = get_object_or_404(Review,id=review_id)
    r_commentform = r_commentForm(request.POST ,request.FILES)
    if r_commentform.is_valid():
        r_comment = r_commentform.save(commit=False)
        r_comment.user = request.user
        r_comment.r_id = review
        r_comment.save()
        
    return redirect('r_detail',review_id)

def r_commentedit(request, r_comment_id ,review_id):
    review = get_object_or_404(Review, id = review_id)
    r_comment = get_object_or_404(R_comment, id = r_comment_id)

    if request.user != r_comment.user:
        return redirect('login')

    if request.method == 'POST':
        r_commentform = r_commentForm(request.POST, request.FILES, instance=r_comment)
        if r_commentform.is_valid():
            r_commentform.save()
        return redirect('r_detail',review_id)
    
    else:
        r_commentform = r_commentForm(instance=r_comment)
        return render(request, 'r_commentedit.html', {'review':review,'r_comment_form':r_commentform})

@require_http_methods(['GET', 'POST'])
def r_commentdelete(request, review_id, r_comment_id):

    review = get_object_or_404(Review, id=review_id)
    
    r_comment = get_object_or_404(R_comment, id=r_comment_id)
    
    if r_comment.user != request.user:
        return redirect('r_detail',review_id)

    r_comment.delete()

    return redirect('r_detail',review_id)