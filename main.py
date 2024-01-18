from numerizer import numerize
from deep_translator import GoogleTranslator

tradutor=GoogleTranslator("pt","en")

numero_em_texto = "mil trezentos e trinta e sete"
numero_em_texto_ingles = tradutor.translate(numero_em_texto)
numero = int(numerize(numero_em_texto_ingles))

print(numero)
print(type(numero))