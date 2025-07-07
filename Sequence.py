import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

from nltk.tokenize import word_tokenize
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def highlight_text(main_text, query, highlight_exact=True, highlight_similar=True, similarity_threshold=100):

    if not main_text or not query:
        return main_text

    highlighted_text = main_text
    query_lower = query.lower()
    main_text_lower = main_text.lower()

    words_in_main_text = main_text.split()

    highlight_ranges = []

    if highlight_exact:
        start_index = 0
        while True:
            idx = main_text_lower.find(query_lower, start_index)
            if idx == -1:
                break
            highlight_ranges.append((idx, idx + len(query)))
            start_index = idx + len(query)

    if highlight_similar:

        words_and_indices = []
        current_idx = 0
        for word in word_tokenize(main_text):
            word_len = len(word)
            idx_in_original = main_text.find(word, current_idx)
            if idx_in_original != -1:
                words_and_indices.append((word, idx_in_original, idx_in_original + word_len))
                current_idx = idx_in_original + word_len
            else:
                words_and_indices.append((word, -1, -1))

        for word, start, end in words_and_indices:
            if start == -1:
                continue
            is_exact_match = False
            for r_start, r_end in highlight_ranges:
                if start >= r_start and end <= r_end:
                    is_exact_match = True
                    break
            if is_exact_match:
                continue

            score = fuzz.ratio(query_lower, word.lower())
            if score >= similarity_threshold:
                highlight_ranges.append((start, end))

    highlight_ranges.sort()
    merged_ranges = []
    if highlight_ranges:
        current_start, current_end = highlight_ranges[0]
        for next_start, next_end in highlight_ranges[1:]:
            if next_start <= current_end:
                current_end = max(current_end, next_end)
            else:
                merged_ranges.append((current_start, current_end))
                current_start, current_end = next_start, next_end
        merged_ranges.append((current_start, current_end))
    parts = []
    last_idx = 0
    for start, end in merged_ranges:
        parts.append(main_text[last_idx:start])
        parts.append(f"**{main_text[start:end]}**")
        last_idx = end
    parts.append(main_text[last_idx:])

    return "".join(parts)