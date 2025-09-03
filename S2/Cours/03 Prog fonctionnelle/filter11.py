words = ["variable", "file#", "header", "_non_public", "123Class"]

print(list(filter(str.isidentifier, words)))