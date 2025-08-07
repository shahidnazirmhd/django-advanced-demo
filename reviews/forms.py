from django import forms


class ReviewForm(forms.Form):
    full_name = forms.CharField(max_length=100, min_length=2)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea, max_length=500, min_length=3)