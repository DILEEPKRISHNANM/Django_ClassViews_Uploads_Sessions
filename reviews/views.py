from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View #to implement views
from django.views.generic.base import TemplateView
from django.views.generic import ListView,DetailView
from django.views.generic.edit import FormView
# Create your views here.




# class ReviewView(View):
#     def get(self,request):
#         form = ReviewForm()
#         return render(request, "reviews/review.html", {
#         "form": form
#         })
        






#     def post(self,request):




#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             # review = Review(user_name=form.cleaned_data['user_name'],review_text=form.cleaned_data['review_text'],rating=form.cleaned_data['rating'])
#             form.save()
#             name = form.cleaned_data['user_name']
#             username = Review.user_name
            
#             return HttpResponseRedirect("/thank-you")




class ReviewView(FormView):
    form_class=ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)


        



def review(request):


    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            # review = Review(user_name=form.cleaned_data['user_name'],review_text=form.cleaned_data['review_text'],rating=form.cleaned_data['rating'])
            review.save()
            name = form.cleaned_data['user_name']
            username = Review.user_name
            
            return HttpResponseRedirect("/thank-you")
    else:
        form = ReviewForm() 
        print(form.errors) # Create a new form instance for GET requests

    return render(request, "reviews/review.html", {
        "form": form
    })



# def thankyou(request):
#     return render(request,"reviews/thank_you.html")



class ThankyouView(TemplateView):
    template_name = "reviews/thank_you.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This Works!!!"
        return context
    



class ReviewlistView(ListView):
    template_name = "reviews/reviewlisting.html"
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["reviews"] = Review.objects.all()
    #     return context


    model = Review

    context_object_name = "reviews"

    def get_queryset(self):
        base_query=super().get_queryset()
        data = base_query.filter(rating__gt=4)
        return data
    





# class DetailView(TemplateView):
#     template_name="reviews/detail.html"
#     def get_context_data(self, **kwargs):
#         review_id = kwargs["id"]
#         context = super().get_context_data(**kwargs)
#         context["data"] = Review.objects.get(pk=review_id)
#         return context
    
    



class DetailsView(DetailView):
    template_name = "reviews/detail.html"
    model = Review
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request=self.request
        favourite_id = request.session.get("favourite_key")
        context["is_favourite"] = favourite_id == str(loaded_review.id)
        return context
    




class AddfavouriteView(View):
    def post(self,request):
        review_id=request.POST['review_id']
        #fav_review = Review.objects.get(pk=review_id)         #Sessions Cant store objects...Make it simple store as single value
        request.session["favourite_key"]=review_id
        return HttpResponseRedirect("/listing/"+review_id)


