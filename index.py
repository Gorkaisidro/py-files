# import your functions here
from utils import files

# read the quijote here
book1 = files.readFile("el_quijote.txt")
book2 = files.readFile("el_quijote_ii.txt")

print(book1)
print("----")
print(book2)
print("----")

book = book1 + book2
print(book)
print("----")

# Word Count
print("Word Count: ", files.wordCount(book))
print("----")
# Unique Word Count
print('Unique Word Count: ', files.uniqueWordCount(book))
print("----")
# Quijote count
print('find Quijote: ', files.findContent(book, 'Quijote'))
print("-----")
# Sancho count
print('find Sancho: ', files.findContent(book, 'Sancho'))
print("----")
# Change Quijote to Quixote and write it to a new file "el_quixote.txt"
# print('Change Quijote to Quixote: ', files.changeQuijoteToQuixote(book))


