🐍 Chackal Attack - Web Scraper & Surface Recon

Chackal Attack é uma ferramenta de automação para descoberta de URLs e subdomínios utilizando buscas em fontes públicas como:Wayback Machine, Google, DuckDuckGo, CRT.sh e força bruta de caminhos.

Ideal para uso em pentest, bug bounty ou footprinting.

🚀 Pré-requisitos

Python 3.8 ou superior

Instale as dependências:

pip install -r requirements.txt

⚡ Como usar

python script.py -u <domínio> [opções]

📌 Argumentos principais

Argumento

Descrição

-u, --url

(obrigatório) Domínio alvo. Ex: -u example.com

-k, --keyword

Palavra-chave opcional para buscas refinadas.

-o, --output

Arquivo de saída para salvar resultados. Suporta .txt e .csv.

--strict-domain

Mantém apenas URLs que contenham o domínio exato.

--api

Lista as fontes: crtsh, wayback, google, duckduckgo. Pode usar múltiplos.

-v, --verbose

Ativa modo detalhado de log.

💡 Exemplos de uso

1️⃣ Buscar URLs de um domínio usando todas as APIs:

python script.py -u example.com

2️⃣ Buscar apenas no Wayback Machine e DuckDuckGo:

python script.py -u example.com --api wayback duckduckgo

3️⃣ Usar uma palavra-chave específica:

python script.py -u example.com -k login

4️⃣ Salvar resultados em um arquivo .csv:

python script.py -u example.com -o resultado.csv

5️⃣ Filtrar apenas URLs que contenham o domínio exato:

python script.py -u example.com --strict-domain

6️⃣ Modo detalhado (debug):

python script.py -u example.com -v

💻 Sobre

Este script foi criado por Yuri Assis para auxiliar no mapeamento de superfície de aplicações web.Confira meu perfil:https://www.linkedin.com/in/yuri-assis-074a66200/

⚠️ Aviso Legal

Este script é para fins educacionais e de teste autorizado.Não use em sistemas sem permissão. O uso indevido é de inteira responsabilidade do usuário.


