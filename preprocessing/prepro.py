from bs4 import BeautifulSoup

with open('preprocessing/sample.html', 'r', encoding='utf-8') as f:
    sample_html = f.read()

def clean_html(html, strip=False):
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text(strip=strip)
    return text

print(clean_html(sample_html))
