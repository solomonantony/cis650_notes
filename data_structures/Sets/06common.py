words = ["python", "typhoon", "phony", "max"]

common_letters = set(words[0]) & set(words[1]) & set(words[2]) & set(words[3])
print("Common letters across all words:", common_letters)
