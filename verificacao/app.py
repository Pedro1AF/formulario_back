from flask import Flask, render_template, redirect, request, flash, session
from flask_mail import Mail, Message
from config import email, senha
from aleatorio import gerar_codigo_verificacao
import os

app = Flask(__name__)
app.secret_key = 'monedas'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = email
app.config['MAIL_PASSWORD'] = senha
app.config['MAIL_DEFAULT_SENDER'] = email
app.config['MAIL_DEBUG'] = True

mail = Mail(app)

class Contato:
    def __init__(self, cpf, email, nome, senha):
        self.cpf = cpf
        self.email = email
        self.nome = nome
        self.senha = senha

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        formContato = Contato(
            request.form["cpf"],
            request.form["email"],
            request.form["nome"],
            request.form["senha"]
        )

        codigo = gerar_codigo_verificacao()
        session['codigo_verificacao'] = codigo
        session['email_usuario'] = formContato.email

        msg = Message(
            subject='Código de Verificação - Monedas',
            recipients=[formContato.email],
            body=f'''Olá {formContato.nome},

Seu código de verificação é: {codigo}

Use este código para completar seu registro.

Atenciosamente,
Equipe de Suporte'''
        )

        try:
            mail.send(msg)
            flash('Código de verificação enviado para seu email!', 'success')
        except Exception as e:
            flash(f'Falha ao enviar email: {str(e)}', 'error')
            app.logger.error(f'Erro no envio de email: {str(e)}')
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)