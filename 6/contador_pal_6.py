import re

def contar_palavras(texto):
    palavras = re.findall(r'\b\w+\b', texto)
    return len(palavras)