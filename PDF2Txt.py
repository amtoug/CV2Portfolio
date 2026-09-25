import pymupdf


def PyMyPDF(cv_file_bytes):
    doc = pymupdf.open(stream=cv_file_bytes, filetype="pdf")

    text = "\n".join(page.get_text() for page in doc)

    doc.close()
    return text

