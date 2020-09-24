array = input('Digite uma frase: ').split()

for word in array:
    print(word)

i = 0
while i < len(array):
    print(f'A {i + 1} palavra é {array[i]}')
    i += 1
