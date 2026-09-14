import re
import sys
import pathlib
import markdown

src = pathlib.Path(sys.argv[1])
out = pathlib.Path(sys.argv[2])

text = src.read_text(encoding="utf-8")


def github_slugify(value, separator):
    slug = value.strip().lower()
    slug = re.sub(r'[^\w\- ]+', '', slug, flags=re.UNICODE)
    return slug.replace(' ', separator)


html_body = markdown.markdown(
    text,
    extensions=["tables", "toc", "fenced_code", "sane_lists"],
    extension_configs={"toc": {"slugify": github_slugify}},
)

html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>G-Force Skiing — руководство пользователя</title>
<style>
body {{ font-family: -apple-system, Segoe UI, Arial, sans-serif; max-width: 900px; margin: 0 auto; padding: 32px 24px; line-height: 1.55; color: #1a1a1a; }}
h1, h2, h3 {{ line-height: 1.25; }}
h1 {{ border-bottom: 2px solid #ddd; padding-bottom: 8px; }}
h2 {{ border-bottom: 1px solid #eee; padding-bottom: 6px; margin-top: 2.2em; }}
img {{ max-width: 100%; width: 100%; height: auto; display: block; margin: 14px 0; border: 1px solid #ddd; border-radius: 6px; }}
blockquote {{ border-left: 4px solid #bbb; margin: 1em 0; padding: 0.2em 1em; color: #444; background: #f7f7f7; }}
code {{ background: #f2f2f2; padding: 2px 5px; border-radius: 4px; }}
hr {{ border: none; border-top: 1px solid #ddd; margin: 2em 0; }}
a {{ color: #1a5fb4; }}
table {{ border-collapse: collapse; }}
td, th {{ border: 1px solid #ccc; padding: 6px 10px; }}
</style>
</head>
<body>
{html_body}
</body>
</html>
"""
out.write_text(html, encoding="utf-8")
print("OK", out)
