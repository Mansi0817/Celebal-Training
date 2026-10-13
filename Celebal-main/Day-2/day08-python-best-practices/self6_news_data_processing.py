# Self Practice Program 6: News Data Processing

import re


def check_word_presence(news, word):
    """Check whether a word appears in the news."""
    return re.search(rf"\b{re.escape(word)}\b", news, re.IGNORECASE) is not None


def count_words(news):
    """Count words in the news paragraph."""
    return len(re.findall(r"\b\w+\b", news))


def count_word_occurrences(news, word):
    """Count occurrences of a particular word."""
    return len(re.findall(rf"\b{re.escape(word)}\b", news, re.IGNORECASE))


def check_digits(news):
    """Check whether the news contains any digits."""
    return bool(re.search(r"\d", news))


def remove_articles(news):
    """Remove the articles a, an, and the."""
    return re.sub(r"\b(a|an|the)\b", "", news, flags=re.IGNORECASE)


def remove_vowels(news):
    """Remove vowels from the text."""
    return re.sub(r"[aeiouAEIOU]", "", news)


def process_news(news):
    """Perform all news-processing operations."""

    print("Presence of 'Modi':", check_word_presence(news, "Modi"))
    print("Number of words:", count_words(news))
    print("Number of occurrences of 'the':",
          count_word_occurrences(news, "the"))
    print("Presence of digits:", check_digits(news))

    compact_news = remove_articles(news)
    print("Compact news data without articles:", compact_news)

    vowel_free_news = remove_vowels(compact_news)
    print("Compact news data without vowels:", vowel_free_news)


if __name__ == "__main__":
    news_paragraph = input("Enter the news paragraph: ")
    process_news(news_paragraph)