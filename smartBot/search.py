import requests
from bs4 import BeautifulSoup

def search_web(query):
    print("SmartBot: Pretražujem internet...")
    try:
        url = f"https://html.duckduckgo.com/html/?q={query}"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=5)

        soup = BeautifulSoup(response.text, "html.parser")
        results = soup.find_all("div", class_="result__body")

        if results:
            first = results[0]
            title = first.find("a", class_="result__a").text.strip()
            snippet_tag = first.find("a", class_="result__snippet")
            snippet = snippet_tag.text.strip() if snippet_tag else "Nema sažetka."
            return f"📚 {title}\n🔎 {snippet}"
        else:
            return "Nisam pronašao ništa korisno."
    except Exception as e:
        return f"⚠️ Greška pri pretrazi: {e}"

def extract_link(query):
    try:
        url = f"https://html.duckduckgo.com/html/?q={query}"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        link_tag = soup.find("a", class_="result__a")
        if link_tag and "href" in link_tag.attrs:
            return link_tag["href"]
    except:
        return None
