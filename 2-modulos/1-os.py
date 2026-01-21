import os

# 1 - Retornar a pasta atual
print(os.getcwd())

# 2 - Listar arquivos e pastas
print(os.listdir())

# 3 - Versão do SO
os.system("ver")

# 4 - Configurações da Máquina
os.system("systeminfo")

# 5 - Limpar a Tela do Terminal
os.system("cls")

# 6- Deligar o computador
#os.system("shutdown /s")   # Desliga o pc
os.system("shutdown /a")    # Cancela o desligamento

def turn_off_one_hour():
    os.system("shutdown /s /t 3600")

def turn_off_half_an_hour():
    os.system("shutdown /s /t 1800")

def cancel_shutdow():
    os.system("shutdown /a")

# turn_off_one_hour()
# cancel_shutdow()
# turn_off_half_an_hour()
cancel_shutdow()