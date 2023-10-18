def readFile(name):
  with open(name, "r", errors="ignore") as file:
    return file.read()

def wordCount(text):
  palabras = len(text.split())
  return palabras

def uniqueWordCount(text):
  palabrasUnicas = len(set(text.split()))
  return palabrasUnicas

import re
def findContent(text, word):
  textFind = text.count(word)
  return textFind

import re
def changeQuijoteToQuixote(text):
  pattern = r"Quijote"
  replacement = "Quixote"
  new_text = re.sub(pattern, replacement, text)
  return new_text