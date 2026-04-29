# Project 4 — Word Counter
# Author: Samuel Aguado

text = input("Enter a sentence: ")

# Convertir a minúsculas y quitar espacios extra
words = text.lower().split()

word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("\n=== Word Frequency ===")
for word, count in word_count.items():
    print(f"{word}: {count}")