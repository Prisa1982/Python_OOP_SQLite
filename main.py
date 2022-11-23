#Importar nosso arquivo Pessoa.py no diretório model
from model.Pessoa import Pessoa

# Exemplo de uso
sapper = Pessoa(1,"Pricila Sapper")
print(sapper)

#Quero mostrar só o nome
print(sapper.nome)

  