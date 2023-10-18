def readFile(name):
  with open(name, "r", errors="ignore") as file:
    return file.read()

def wordCount(text):
  palabras = len(text.split())
  return palabras

def uniqueWordCount(text):
  palabrasUnicas = len(set(text.split()))
  return palabrasUnicas

def findContent(text, word):
  quijote = text.count(word)
  return quijote

import re
def changeQuijoteToQuixote(text):
  pattern = r"Quijote"
  replacement = "Quixote"
  new_text = re.sub(pattern, replacement, text)
  return new_text