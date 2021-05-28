from django import forms
from django.core.mail.message import EmailMessage
from .models import Produto


class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'imagem']



class EmailContato(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email',max_length=100)
    assunto = forms.CharField(label='Assunto',max_length=120)
    mensagem = forms.CharField(label='Mensagem',widget= forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

    conteudo = f' Nome: {nome}\n Email:{email}\n Asssunto: {assunto}\n Mensagem:{mensagem}'

    mail = EmailMessage(
        subject= f'Email enviado por {email}',
        body= conteudo,
        from_email='eduardomichael1@gmail.com',
        to=['contato@gmail.com'],
        headers={'Reply-To': email}
    )
    mail.send()
