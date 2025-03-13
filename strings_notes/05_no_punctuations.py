import string
raw_string = "abdABC123.[]"
processed = ""
for x in raw_string:
  if x  in string.digits:
    processed += x
print(processed)
