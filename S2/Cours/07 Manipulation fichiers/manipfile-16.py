with open(r'..\travail1\chemin\dog_breeds.txt', 'r') as reader:
    for line in reader.readlines():
        print(line, end='')