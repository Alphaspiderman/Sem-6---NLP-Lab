from collections import Counter


def get_n_grams(text: str, n: int):
    words = text.split(" ")
    if n > len(words):
        print(f"Not enough words to find {n}-grams")
        quit()
    if n == len(words):
        return [tuple(words)]
    n_grams = [tuple(words[i : i + n]) for i in range(len(words) - n + 1)]
    return n_grams


def get_rev_n_grams(text: str, n: int):
    words = text.split(" ")[::-1]
    if n > len(words):
        print(f"Not enough words to find {n}-grams")
        quit()
    if n == len(words):
        return [tuple(words)]
    n_grams = [tuple(words[i : i + n]) for i in range(len(words) - n + 1)]
    return n_grams


def get_n_gram_prob(n_grams):
    n_gram_prob = {i: n_grams[i] / sum(n_grams.values()) for i in n_grams.keys()}
    return n_gram_prob


text = input("Enter text to analyse: ")
n = int(input("Enter the type of n-grams to check (2 for bi-grams): "))
n_grams = get_n_grams(text, n)
n_gram_freqs = Counter(n_grams)
n_gram_probs = get_n_gram_prob(n_gram_freqs)
print(f"Text: {text}")
print(f"Frequencies: {dict(n_gram_freqs)}")
print(f"Probabilities: {n_gram_probs}")
print(f"Reversed {n}-Gram: {get_rev_n_grams(text, n)}")
