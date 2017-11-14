from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=250, min_length=3, widget = forms.TextInput(attrs={'placeholder':'Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email'}))
    phone = forms.CharField(max_length=10, min_length=10, widget = forms.TextInput(attrs={'placeholder':'Phone'}))
    city = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'City'}), required=False)
    message = forms.CharField(max_length=1000, min_length=10, widget=forms.Textarea(attrs={'placeholder':'Message'}))

class CommentForm(forms.Form):
    name = forms.CharField(max_length=250, min_length=10, widget=forms.TextInput(attrs={'placeholder':'Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email'}))
    phone = forms.IntegerField(max_value=9999999999, min_value=1000000000, widget = forms.NumberInput(attrs={'placeholder':'Phone'}))
    message = forms.CharField(max_length=1000, min_length=10, widget=forms.Textarea(attrs={'placeholder':'Message'}))

class ArticleForm(forms.Form):
    status_choices = (
        ('D', 'Draft'),
        ('P', 'Published'),
    )
    status = forms.ChoiceField(choices= status_choices)
    title = forms.CharField(max_length=250, min_length=10, widget=forms.TextInput(attrs={'placeholder':'Title'}))
    content = forms.CharField(max_length=5000, min_length=50,widget=forms.Textarea(attrs={'placeholder':'Content'}))
    tags = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'placeholder':'Tags separated by Comma(,)'}), required=False)
    image = forms.ImageField(label='Image: ', required = False)