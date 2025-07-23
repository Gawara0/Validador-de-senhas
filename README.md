# 🔐 Validador de Força de Senhas (Python)

Este projeto é um validador de senhas desenvolvido em Python que avalia a força de uma senha fornecida pelo usuário com base em critérios essenciais de segurança. Ele retorna uma nota de **0 a 100** e classifica a senha como **Fraca**, **Média**, **Boa** ou **Forte**.

---

## 📌 Funcionalidades

✔️ Verificação de:
- Tamanho mínimo da senha (≥ 8 e ≥ 12 caracteres)
- Uso de letras maiúsculas e minúsculas
- Inclusão de números
- Inclusão de caracteres especiais
- Presença na lista de senhas mais comuns

✔️ Pontuação total de segurança (de 0 a 100)

✔️ Mensagem de alerta se a senha estiver entre as mais comuns

✔️ Classificação visual com emojis 🟥 🟨 🟩 ✅

---

## 🧪 Exemplo de uso

---Validador de senha---

Digite sua senha: Senha123

⚠️ Atenção: sua senha está entre as mais comuns e pode ser facilmente descoberta.

---Conclusão da validação:---

Senha fornecida: Senha123 Nota da senha: 65/100 Força da senha: Boa🟩

---

## 🎯 Classificação por nota

| Nota | Classificação |
|------|----------------|
| 0 a 30 | **Fraca** 🟥 |
| 31 a 60 | **Média** 🟨 |
| 61 a 80 | **Boa** 🟩 |
| 81 a 100 | **Forte** ✅ |

---

## 🚀 Como executar

1. Clone o repositório:
```bash
git clone https://github.com/Gawara0/Validador-de-senhas.git

2. Acesse a pasta:

cd Validador-de-senha


3. Execute o script:

python senha_checker.py



> 💡 Requer Python 3 instalado no sistema.




---

⚠️ Aviso

Este projeto é educacional e não armazena nenhuma senha.
Use apenas para fins de aprendizado e boas práticas de segurança.
