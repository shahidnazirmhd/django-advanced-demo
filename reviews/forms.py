from django import forms


from .models import Review


# class ReviewForm(forms.Form):
#     full_name = forms.CharField(max_length=100, min_length=2, error_messages={
#         "required": "Your name must not be empty!",
#         "max_length": "Please enter a shorter name!",
#         "min_length": "Please enter a valid name",
#     })
#     email = forms.EmailField(error_messages={
#         "required": "Email is required",
#     })
#     rating = forms.IntegerField(min_value=1, max_value=5, error_messages={
#         "required": "Rating is required",
#         "min_value": "Please rate correctly (1 t0 5)!",
#         "max_value": "Please rate correctly (1 t0 5)!",
#     })
#     message = forms.CharField(widget=forms.Textarea, max_length=500, min_length=3, error_messages={
#         "required": "Feedback message must not be empty!",
#         "max_length": "Please give a short feedback message!",
#         "min_length": "Please give valid feedback message",
#     })
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        