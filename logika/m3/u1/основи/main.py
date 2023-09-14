with open("quotes.txt", 'r', encoding= "utf-8") as file:
    print(file.read())

author = input('Введіть автора')

with open("quotes.txt", 'a', encoding= "utf-8") as file:
    file.write(f'({author})')

with open("quotes.txt", 'r', encoding= "utf-8") as file:
    print(file.read())