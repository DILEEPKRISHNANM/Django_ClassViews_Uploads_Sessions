from django import forms

from .models import Review


# class ReviewForm(forms.Form):
#     user_name = forms.CharField(max_length=8,label="Your Name",error_messages={
#         "required":"Everbody Has A name!!!",
#         "max_length":"How On earth Any One call U with that name "
#     })


#     review_text = forms.CharField(label="Pls Give A Review!!",widget=forms.Textarea,max_length=200)

#     rating = forms.IntegerField(label="Give Rating",min_value=1,max_value=5)




class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields ="__all__"

        labels ={
            "user_name":"Your Name:",
            "review_text":"You Review"
        }

