from transformers import pipeline

# Load model (fast + stable)
summarizer = pipeline("text2text-generation", model="google/flan-t5-base")


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
        prompt = "Summarize this text: " + chunk

        result = summarizer(
            prompt,
            max_length=max_len,
            min_length=min_len,
            do_sample=False
        )

        final_summary.append(result[0]['generated_text'])

    return " ".join(final_summary)


if __name__ == "__main__":
    text = input("Enter text:\n")
    print("\nSummary:\n")
    print(summarize_text(text))