import win32com.client as win32

# criar integração com outlook
outlook = win32.Dispatch('outlook.application')

# criar um e-mail
email = outlook.CreatItem(0)

faturamento = 1500
qtde_produtos = 10
ticket_medio = faturamento / qtde_produtos

# configurar as informações do seu e-mail
email.To = "richardpenido@live.com; richard_rp007@yahoo.com.br"
email.Subject = "E-mail automático do Python"
email.HTMLBody = f"""
<p> Olá Usuário, aqui é o código Python</p>

<p>O faturamento da loja foi de R$ {faturamento}</p>
<p>Vendemos {qtde_produtos} produtos</p>
<p>O ticket Médio foi de R$ {ticket_medio}</p>

<p>Abs,</p>
<p>Código Python</p>
"""

# anexo = "C://Users/richa/Downloads/arquivo.xlsx"
# e-mail.Attachments.Add(anexo)

email.Send()
print("Email Enviado")
