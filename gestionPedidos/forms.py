from django import forms

class Formulario(forms.Form):
    
    asunto=forms.CharField()
    emai=forms.EmailField()
    mensaje=forms.CharField()


