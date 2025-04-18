# 🐺 Chackal Surface Attack- Web Scraper & Surface Recon
#  ![image](https://github.com/user-attachments/assets/faffbd9d-d048-4732-b0f8-56ec0571a2e5)






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
🔮 **Futuro da Ferramenta**

**1.Busca de Leaks de Credenciais**

Integração com fontes públicas e privadas de vazamentos

Monitoramento contínuo e alertas de novas exposições

Suporte a múltiplos formatos de dumps (txt, json, pastebin, etc.)

**2.Busca de URLs na Deep Web**

Raspagem e indexação de serviços .onion

Detecção de menções a ativos da empresa (e-mails, domínios, IPs)

Utilização de proxies TOR e rotatividade de identidade

**3.Spider-Bot**

Varredura automática de sites para coleta de links e endpoints

Detecção de formulários e possíveis vetores de ataque

Suporte a autenticação e navegação dinâmica (JS-rendered)

**4.Filtros de Buscas**

Personalização dos parâmetros de varredura (por domínio, extensão, tipo de dado)

Filtros por data, reputação da fonte e tipo de conteúdo

Sistema de whitelist e blacklist

**5.Injeção de Payloads por Parâmetros**

Testes automáticos de injeção (XSS, SQLi, LFI, RCE)

Geração e execução de payloads customizados

Detecção de respostas vulneráveis com análise heurística



## 💻 Sobre

Script criado por **Yuri Assis** para auxiliar no mapeamento de superfície de aplicações web.  
Confira meu perfil: LinkedIn: https://www.linkedin.com/in/yuri-assis-074a66200/

---

## ⚠️ Aviso Legal

Este script é para **fins educacionais e de teste autorizado**.  
**Não use** em sistemas sem permissão. O uso indevido é de inteira responsabilidade do usuário.
---

## 💸Doações pro Projeto
**Chave Pix: 1d7cb377-c78d-46a8-9796-009170de6f56**
