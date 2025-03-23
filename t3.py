import string
sentence = "Котики та краби - милі тварини, які часто живуть на узбережжі."
words = sentence.split()

for word in words:
    word = word.strip(string.punctuation)
    if word.lower().startswith('к'): 
        print(word)
        break
