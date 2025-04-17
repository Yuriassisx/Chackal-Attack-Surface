# 🐺 Chackal Surface Attack- Web Scraper & Surface Recon
   ![image](https://github.com/user-attachments/assets/a3f00282-a4d9-473f-b4b4-792aeb5881be)


**Chackal Attack** é uma ferramenta de automação para descoberta de **URLs** e **subdomínios**, utilizando buscas em fontes públicas como:

- Wayback Machine  
- Google  
- DuckDuckGo  
- CRT.sh  
- Força bruta de caminhos

Ideal para **pentest**, **bug bounty** ou **footprinting**.

---

## 🚀 Pré-requisitos

- Python **3.8** ou superior

Instale as dependências com:

```bash
pip install -r requirements.txt
```

---

## ⚡ Como usar

```bash
python script.py -u <domínio> [opções]
```

---

## 📌 Argumentos principais

| Argumento           | Descrição                                                                 |
|---------------------|------------------------------------------------------------------------------|
| `-u`, `--url`       | (**obrigatório**) Domínio alvo. Ex: `-u example.com`                       |
| `-k`, `--keyword`   | Palavra-chave opcional para buscas refinadas.                                |
| `-o`, `--output`    | Arquivo de saída para salvar resultados. Suporta `.txt` e `.csv`.           |
| `--strict-domain`  | Mantém apenas URLs que contenham o domínio exato.                            |
| `--api`             | Lista as fontes: `crtsh`, `wayback`, `google`, `duckduckgo`. Múltiplos aceitos. |
| `-v`, `--verbose`   | Ativa modo detalhado de log.                                                  |

---

## 💡 Exemplos de uso

1. Buscar URLs de um domínio usando todas as APIs:
   ```bash
   python script.py -u example.com
   ```

2. Buscar apenas no Wayback Machine e DuckDuckGo:
   ```bash
   python script.py -u example.com --api wayback duckduckgo
   ```

3. Usar uma palavra-chave específica:
   ```bash
   python script.py -u example.com -k login
   ```

4. Salvar resultados em um arquivo `.csv`:
   ```bash
   python script.py -u example.com -o resultado.csv
   ```

5. Filtrar apenas URLs que contenham o domínio exato:
   ```bash
   python script.py -u example.com --strict-domain
   ```

6. Ativar modo detalhado (debug):
   ```bash
   python script.py -u example.com -v
   ```

---

## 💻 Sobre

Script criado por **Yuri Assis** para auxiliar no mapeamento de superfície de aplicações web.  
Confira meu perfil: LinkedIn: https://www.linkedin.com/in/yuri-assis-074a66200/

---

## ⚠️ Aviso Legal

Este script é para **fins educacionais e de teste autorizado**.  
**Não use** em sistemas sem permissão. O uso indevido é de inteira responsabilidade do usuário.
