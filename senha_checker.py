import re
nota = 0
print ("\n---Validador de senha---\n")
while True:
	senha = input("Digite sua senha:\n")
	if senha.strip() == "":
		print("Senha em branco não é valida.\n")
	else:
		break
if len (senha) >=8:
	nota +=20
if len (senha) >= 12:
	nota +=10
if re.search(r"[A-Z]", senha):
	nota += 15
if re.search(r"[a-z]", senha):
	nota +=15
if re.search(r"[0-9]", senha):
	nota +=15
if re.search(r"[^A-Za-z0-9]", senha):
	nota += 15
senhas_comuns = ["123456","password","12345678","qwerty","123456789","12345","1234","111111","1234567","dragon","123123","baseball","abc123","football","monkey","letmein","696969","shadow","master","666666","qwertyuiop","123321","mustang","1234567890","michael","654321","superman","1qaz2wsx","7777777","121212","000000","qazwsx","123qwe","killer","trustno1","jordan","jennifer","zxcvbnm","asdfgh","hunter","buster","soccer","harley","batman","andrew","tigger","sunshine","iloveyou","2000","charlie"]
if senha.lower() not in senhas_comuns:
    nota += 10
else:
	print ("\n⚠️ Atenção: sua senha está entre as mais comuns e pode ser facilmente descoberta.\n")
if nota <= 30:
	classificacao = "Fraca🟥"
elif nota <= 60:
	classificacao = "Média🟨"
elif nota <= 80:
	classificacao = "Boa🟩"
else:
	classificacao = "Forte✅"
print ("\n---Conclusão da validação:---\n")
print (f"Senha fornecida: {senha}")
print (f"Nota da senha: {nota}/100")
print (f"Força da senha: {classificacao}")
