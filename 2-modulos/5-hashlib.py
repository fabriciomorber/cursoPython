import hashlib

# 1 - Verificar os algoritmos disponíveis
print(hashlib.algorithms_available)

# 2 - Verificar algoritmos de acordo com o SO
print(hashlib.algorithms_guaranteed)

# 3 - Utilizando o SHA256
algotithm = hashlib.sha256()
print(algotithm.digest())
mensagem = "A melhor forma de prever o futuro é criá-lo".encode()
algotithm.update(mensagem)
print(algotithm.hexdigest())

# 4 - Utilizando o MD5
md5 = hashlib.md5()
md5.update(mensagem)
print(md5.hexdigest())