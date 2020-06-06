# Questo in Python 3 è un commento che non influisce nell'esecuzione del codice

# Importare un modulo esterno
print("Silvia")

input('Give me an information?')


fh = open("words.txt", "r")

count = 0
for line in fh:
    print(line.strip())
    count = count + 1

print(count,"Lines")




