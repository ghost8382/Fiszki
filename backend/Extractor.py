def extract_text(file):
    from PyPDF2 import PdfReader
    reader = PdfReader(file)
    text = "\n".join(page.extract_text() or "" for page in reader.pages)
    return text


def extract_text(file):
    from PyPDF2 import PdfReader
    reader = PdfReader(file)
    text = "\n".join(page.extract_text() or "" for page in reader.pages)

    # Dodajemy logowanie, żeby sprawdzić, czy tekst jest poprawnie wyciągany
    print("Extracted Text:\n", text)
    return text