class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome
        self.__ano = ano
        self.__duracao = duracao
        self.__like = 0

    @property
    def nome(self):
        return self.__nome.title()

    @property
    def ano(self):
        return self.__ano

    @property
    def duracao(self):
        return self.__duracao

    @property
    def like(self):
        return self.__like

    def dar_like(self):
        self.__like =+1

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome
        self.__ano = ano
        self.__temporadas = temporadas
        self.__like = 0

    @property
    def nome(self):
            return self.__nome.title()

    @property
    def ano(self):
            return self.__ano

    @property
    def temporadas(self):
            return self.__temporadas

    @property
    def like(self):
            return self.__like

    @temporadas.setter
    def temporadas(self, quantidade_atutal):
        self.__temporadas = quantidade_atutal

    def dar_like(self):
        self.__like =+1



vingadores = Filme('vingadores - guerra infinita', 2018, 160)
print(f'Nome: {vingadores.nome} - Ano:{vingadores.ano}'
          f'- Duração: {vingadores.duracao} - Likes: {vingadores.like}')

atlanta = Serie('atlanta', 2018, 2)
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano}'
      f'- Temporadas: {atlanta.temporadas} - Likes: {atlanta.like}')
