words = ["python", "typhoon", "phony"]

common_letters = set(words[0]) & set(words[1]) & set(words[2])
print("Common letters across all words:", common_letters)
