import argparse
import requests
import csv
import threading
import sys
import logging
import os
from bs4 import BeautifulSoup

# Banner
print("\033[92m")
print(r"""
██████╗██╗  ██╗ █████╗  ██████╗██╗  ██╗ █████╗ ██╗
██╔════╝██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔══██╗██║
██║     ███████║███████║██║     █████╔╝ ███████║██║
██║     ██╔══██║██╔══██║██║     ██╔═██╗ ██╔══██║██║
╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗██║  ██║███████╗
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═════╝╚═╝  ╚═╝╚═╝  ╚══════╝
""")
print("LinkedIn: https://www.linkedin.com/in/yuri-assis-074a66200/")
print("\033[0m")

# Logger setup
def setup_logger(verbose=False):
    handlers = [logging.StreamHandler(sys.stdout)]
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format='[%(asctime)s] %(levelname)s: %(message)s', handlers=handlers)

# Wayback search
def search_waybackurls(domain):
    logging.info(f"Buscando no Wayback Machine para {domain}")
    url = f"https://web.archive.org/cdx/search/cdx?url={domain}/*&output=text&fl=original&collapse=urlkey"
    try:
        response = requests.get(url, timeout=15)
        return list(set(response.text.splitlines())) if response.status_code == 200 else []
    except Exception as e:
        logging.error(f"Erro Wayback: {e}")
        return []

# Google search
def search_google(domain, keyword=None):
    headers = {'User-Agent': 'Mozilla/5.0'}
    query = f"site:{domain}" if not keyword else f"site:{domain} {keyword}"
    url = f"https://www.google.com/search?q={requests.utils.quote(query)}"
    links = []
    try:
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')
        for g in soup.find_all('a'):
            href = g.get('href')
            if href and href.startswith('/url?q='):
                link = href.split('&')[0].replace('/url?q=', '')
                links.append(link)
        return links
    except Exception as e:
        logging.error(f"Erro Google: {e}")
        return []

# DuckDuckGo search
def search_duckduckgo(domain, keyword=None):
    headers = {'User-Agent': 'Mozilla/5.0'}
    query = f"site:{domain}" if not keyword else f"site:{domain} {keyword}"
    url = f"https://html.duckduckgo.com/html/?q={requests.utils.quote(query)}"
    links = []
    try:
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')
        for a in soup.find_all('a', {'class': 'result__url'}):
            link = a.get('href')
            if link:
                links.append(link)
        return links
    except Exception as e:
        logging.error(f"Erro DuckDuckGo: {e}")
        return []

# CRT.sh search
def search_crtsh(domain):
    url = f"https://crt.sh/?q=%25{domain}&output=json"
    try:
        response = requests.get(url, timeout=15)
        data = response.json()
        subdomains = {entry['name_value'].replace('*.','') for entry in data}
        for sub in subdomains:
            logging.info(f"CRT.sh encontrou: {sub}")
        return list(subdomains)
    except Exception as e:
        logging.error(f"Erro CRT.sh: {e}")
        return []

# Forced paths discovery
def forced_paths(domain, wordlist):
    found = []
    if not domain.startswith("http"):
        domain = "http://" + domain

    def worker(path):
        full_url = f"{domain.rstrip('/')}/{path}"
        try:
            response = requests.get(full_url, timeout=5)
            if response.status_code < 400:
                logging.info(f"FORCED: {full_url} [{response.status_code}]")
                found.append(full_url)
        except Exception:
            pass

    threads = []
    for path in wordlist:
        t = threading.Thread(target=worker, args=(path,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    return found

# Filtering URLs
def filter_strict_domain(urls, domain):
    filtered = [url for url in urls if domain in url]
    for url in filtered:
        logging.info(f"MANTIDO: {url}")
    return filtered

# Save results
def save_results(urls, output_name):
    ext = os.path.splitext(output_name)[1].lower()
    try:
        if ext == ".csv":
            with open(output_name, 'w', newline='') as csvf:
                writer = csv.writer(csvf)
                writer.writerow(['URL'])
                for url in urls:
                    writer.writerow([url])
        else:
            if ext != ".txt":
                output_name += ".txt"
            with open(output_name, 'w') as txt:
                for url in urls:
                    txt.write(url + '\n')
        logging.info(f"Resultados salvos em {output_name}")
    except Exception as e:
        logging.error(f"Erro ao salvar os arquivos: {e}")

# Main logic
def main():
    parser = argparse.ArgumentParser(description="Chackal Attack - Web Scraper Surface e APIs.")
    parser.add_argument('-u', '--url', required=True, help="Domínio alvo para busca.")
    parser.add_argument('-k', '--keyword', help="Palavra-chave opcional.")
    parser.add_argument('-o', '--output', help="Arquivo de saída para salvar resultados.")
    parser.add_argument('--strict-domain', action='store_true', help="Filtrar apenas URLs do domínio.")
    parser.add_argument('--api', nargs='+', help="Lista de APIs públicas: crtsh, wayback, google, duckduckgo.")
    parser.add_argument('-v', '--verbose', action='store_true', help="Exibir progresso detalhado.")
    args = parser.parse_args()

    setup_logger(args.verbose)

    wordlist = ['admin', 'backup', 'old', 'login', 'test', '.git', '.env', 'config', 'db', 'tmp']
    domain = args.url
    all_urls = []

    try:
        if args.api:
            if 'crtsh' in args.api:
                subdomains = search_crtsh(domain)
                for sub in subdomains:
                    all_urls.extend(search_waybackurls(sub))
                    all_urls.extend(search_google(sub, args.keyword))
                    all_urls.extend(search_duckduckgo(sub, args.keyword))
            if 'wayback' in args.api:
                all_urls.extend(search_waybackurls(domain))
            if 'google' in args.api:
                all_urls.extend(search_google(domain, args.keyword))
            if 'duckduckgo' in args.api:
                all_urls.extend(search_duckduckgo(domain, args.keyword))
        else:
            all_urls.extend(search_waybackurls(domain))
            all_urls.extend(search_google(domain, args.keyword))
            all_urls.extend(search_duckduckgo(domain, args.keyword))

        forced = forced_paths(domain, wordlist)
        all_urls.extend(forced)
        all_urls = list(set(filter(lambda x: x.startswith(('http', 'https', 'ftp', 'ftps', 'ssh')), all_urls)))

        if args.output:
            save_results(all_urls, args.output)

        filtered_urls = all_urls
        if args.strict_domain:
            filtered_urls = filter_strict_domain(filtered_urls, domain)

        for url in filtered_urls:
            print(url)

        logging.info(f"{len(filtered_urls)} URLs exibidas após filtros.")
        logging.info("Script finalizado.")

    except Exception as e:
        logging.error(f"Erro geral: {e}")

if __name__ == '__main__':
    main()
