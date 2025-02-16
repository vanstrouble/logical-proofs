import re

text = "Hola pequeña Aideé. Te he echado mucho de menos y solo quería decirte lo mucho que te amo y la inspiración que eres para mí cada día de mi vida."

def normalize_word(word):
     return re.sub(r'[.,](?!(?<=\d.)\d)', '', re.sub(r'(?<=[^\W\d_])(?<![MmXx])(?=\d)|(?<=\d)(?=[^\W\d_])', ' ', word)).lower()

def word_repetitions(text):
    counts = {}
    separated_words = text.split(" ")
    for word in separated_words:
        if normalize_word(word) in counts:
            counts[normalize_word(word)] += 1
        else: counts[normalize_word(word)] = 1
    print(f"{counts}")


if __name__ == "__main__":
    word_repetitions(text)
