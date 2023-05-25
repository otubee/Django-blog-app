from django import forms

class ArticleForm(forms.Form):
  title = forms.CharField()
  content = forms.CharField()
  category = forms.CharField()
  author = forms.CharField()
  date_published = forms.CharField()
  date_updated = forms.CharField()