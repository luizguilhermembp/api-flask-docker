# api-flask-docker

# 🚀 Flask API - Soma & Multiplicação

API simples construída com Flask, documentada com Swagger, containerizada com Docker e implantada automaticamente via GitHub Actions em uma VM no Azure.

---

## 📌 Endpoints disponíveis

| Método | Rota              | Descrição                           |
|--------|-------------------|-------------------------------------|
| POST   | `/soma`           | Retorna a soma de dois números      |
| POST   | `/multiplicacao`  | Retorna o produto de dois números   |

🧪 Teste via Swagger UI:  
**[http://20.150.222.135/apidocs/](http://20.150.222.135/apidocs/)**

---

## 🛠️ Tecnologias utilizadas

- **Python 3.10**
- **Flask**
- **Flasgger (Swagger UI)**
- **Gunicorn**
- **Docker**
- **GitHub Actions**
- **VM Ubuntu (Azure)**

---

## 🐳 Como rodar localmente

> Requer Docker instalado.

```bash
# Build da imagem
docker build -t flask-api .

# Executar na porta 80
docker run -d -p 80:80 flask-api
```
## ⚙️ CI/CD - Deploy automático

Sempre que um push for feito na branch main, o GitHub Actions:
	1.	Conecta via SSH na VM (Azure)
	2.	Executa git pull
	3.	Para e remove o container anterior (se existir)
	4.	Faz o build do novo container
	5.	Executa o container atualizado na porta 80

Workflow localizado em: .github/workflows/deploy.yml

## 📁 Estrutura do projeto

	•	app.py: Código da API Flask
	•	requirements.txt: Dependências do projeto
	•	Dockerfile: Container configurado com Gunicorn
	•	.github/workflows/deploy.yml: Pipeline de deploy com GitHub Actions

### ✨ Autor

Luiz Guilherme – linkedin.com/in/luizguilhermembp

### 🧠 Observações

✔️ Projeto desenvolvido em ambiente com restrições (macOS sem Docker)

✔️ Deploy real utilizando infraestrutura do Azure for Students

✔️ Pipeline 100% funcional usando GitHub Actions + SSH
