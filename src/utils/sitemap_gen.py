import os
from datetime import date

SITE_URL = "https://gracerubyfrain.github.io"
PAGES_DIR = "src/pages"
OUTPUT_FILE = "public/sitemap.xml"
PAGE_EXTENSIONS = (".tsx", ".jsx", ".html")

def get_urls():
	def page_to_url(file):
		name = os.path.splitext(file)[0].lower()
		if name == "home":
			return f"/"
		return f"/{name}"

	pages = [p for p in os.listdir(PAGES_DIR) if p.endswith(PAGE_EXTENSIONS)]
	urls = [f"{SITE_URL}{page_to_url(p)}" for p in pages]
	return urls

page_urls = get_urls()

xml_urls = [f"""
	<url>
		<loc>{u}</loc>
		<lastmod>{date.today()}</lastmod>
		<changefreq>monthly</changefreq>
		<priority>1.0</priority>
	</url>
""" for u in page_urls]

urlset = "".join(xml_urls)

sitemap = f"""
<?xmlns version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urlset}</urlset>
"""

os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
	try :
		f.write(sitemap)
	except:
		print(f"🔴 Sitemap generation errored!")
	 
print(f"🟢 Sitemap generated at {OUTPUT_FILE}")
print(f"{page_urls}")