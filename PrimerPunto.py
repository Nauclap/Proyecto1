import numpy as np
votos = np.zeros(30)
dict_votos = {}
for i in range(5000):
    x = int(np.ceil(30*(np.random.random())))
    votos[x-1] += 1
dict_candidatos = {}
for i in range(30):
    dict_candidatos['candidato '+str(i+1)]= int(votos[i])
#print(dict_candidatos)
print(' ')
dict_candidatos_ordenado = dict(sorted(dict_candidatos.items(), key=lambda item: item[1], reverse=True))
for candidato, votos in dict_candidatos_ordenado.items():
    print(f"Candidato {candidato}: {votos} votos")
