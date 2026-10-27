import fitz


def extract_pages(pdf_path):

    document = fitz.open(pdf_path)

    pages = []

    for page_number, page in enumerate(document):

        text = page.get_text()

        pages.append(
            {
                "page": page_number + 1,
                "text": text
            }
        )

    document.close()

    return pages


def chunk_pages(pages, chunk_size=500):

    chunks = []

    metadata = []

    for page in pages:

        text = page["text"]

        for i in range(0, len(text), chunk_size):

            chunks.append(text[i:i + chunk_size])

            metadata.append(
                {
                    "page": page["page"]
                }
            )

    return chunks, metadata