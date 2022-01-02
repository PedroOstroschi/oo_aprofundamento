class Conteudo_Video:
    def __init__(self, nome, ano):
        self._nome = nome
        self._ano = ano
        self._like = 0

    @property
    def nome(self):
        return self._nome.title()

    @property
    def ano(self):
        return self._ano

    @property
    def like(self):
        return self._like

    def dar_like(self):
        self._like =+1

    def __str__(self):
        return (f'{self.nome} - {self.ano} - {self.like}')




class Filme(Conteudo_Video):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self._duracao = duracao


    @property
    def duracao(self):
        return self._duracao

    def __str__(self):
        return (f'{self.nome} - {self.ano} - {self.duracao} minutos - {self.like}')


class Serie(Conteudo_Video):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self._temporadas = temporadas

    @property
    def temporadas(self):
            return self._temporadas

    @temporadas.setter
    def temporadas(self, quantidade_atutal):
        self._temporadas = quantidade_atutal

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.temporadas} temporadas - {self.like}'

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)




vingadores = Filme('vingadores - guerra infinita', 2018, 160)
print(f'Nome: {vingadores.nome} - Ano:{vingadores.ano}'
          f'- Duração: {vingadores.duracao} - Likes: {vingadores.like}')

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_like()
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano}'
      f'- Temporadas: {atlanta.temporadas} - Likes: {atlanta.like}')

filme_e_serie = [vingadores, atlanta]
fim_de_semana = Playlist('Fim de semana', filme_e_serie)

for programas in fim_de_semana.listagem:
    print(programas)
