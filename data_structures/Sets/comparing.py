word1 = "hello"
word2 = "world"

set1, set2 = set(word1), set(word2)

print("Letters in both words (intersection):", set1 & set2)
print("Letters only in word1:", set1 - set2)
print("Letters only in word2:", set2 - set1)
print("All letters (union):", set1 | set2)
