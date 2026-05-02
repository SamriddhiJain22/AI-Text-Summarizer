from transformers import pipeline

# Lightweight, deployment-friendly model
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")


def chunk_text(text, max_words=400):
    words = text.split()
    chunks = []

    for i in range(0, len(words), max_words):
        chunk = " ".join(words[i:i+max_words])
        chunks.append(chunk)

    return chunks


def summarize_text(text, max_len=120, min_len=40):
    if not text.strip():
        return "No input provided."

    chunks = chunk_text(text)
    final_summary = []

    for chunk in chunks:
        summary = summarizer(
            chunk,
            max_length=max_len,
            min_length=min_len,
            do_sample=False
        )
        final_summary.append(summary[0]['summary_text'])

    return " ".join(final_summary)


# For testing in terminal
if __name__ == "__main__":
    text = input("Enter text:\n")
    print("\nSummary:\n")
    print(summarize_text(text))
