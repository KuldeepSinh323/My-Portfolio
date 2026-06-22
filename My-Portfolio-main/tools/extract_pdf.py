import sys
import subprocess

try:
    import PyPDF2
except Exception:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PyPDF2"])
    import PyPDF2

from PyPDF2 import PdfReader
pdf_path = r"K:\\Resume\\BE IT\\Resume for It support\\Kuldeep IT Sup Resume .pdf"
reader = PdfReader(pdf_path)
texts = []
for p in reader.pages:
    txt = p.extract_text() or ""
    texts.append(txt)

print("---PDF-START---")
print("\n\n".join(texts))
print("---PDF-END---")
