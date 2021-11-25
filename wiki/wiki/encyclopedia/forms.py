from django import forms

class PageForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Title here'
            }
        )
    )
    content = forms.CharField(max_length=10240,
        widget=forms.Textarea(attrs={
            'class': 'form-control mb-2', 
            'rows': '10', 
            'placeholder': 'Write your content here'
        })
    nope = forms.BooleanField(required=False)
    def clean(self):
        cleaned_data = super(PagegForm, self).clean()
    title = cleaned_data.get('title')
    content = cleaned_data.get('content')
    if nope:
        raise forms.ValidationError('Not allowed to make this entry!')