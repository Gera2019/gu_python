from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

words_array = [nouns, adverbs, adjectives]

def get_jokes(n):
    joke = []
    i = 1
    while i <= n:
        joke.append(' '.join(map(lambda word: choice(word), words_array)))
        i += 1
    print(joke)


get_jokes(5)

