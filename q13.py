from collections import Counter
with open('This.txt') as f:
    word_counts = Counter(f.read().split())
for word, count in word_counts.items():
    print(f"'{word}': {count}")
