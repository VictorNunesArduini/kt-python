import random


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    def print_pessoa(self):
        print("Nome: " + self.nome + ", Idade: " + str(self.idade))


class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario


class Cliente(Pessoa):
    pass


class Aluno(Cliente):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.matricula = random.randint(0, 10000)

    def print_aluno(self):
        print("Nome: " + self.nome + ", Idade: " + str(self.idade) + ", Matricula: " + str(self.matricula))


class Professor(Funcionario):
    def __init__(self, nome, idade, salario, cursos):
        super().__init__(nome, idade, salario)
        self.cursos = cursos

    def concat_cursos(self, cursos):
        concat_list = ""
        for i in cursos:
            concat_list += i + " "
        return concat_list

    def print_professor(self):
        print("Nome: " + self.nome + ", Idade: " + str(self.idade) + ", Salario: " + str(self.salario) +
              ", Cursos Ministrados: " + self.concat_cursos(self.cursos))


# instanciando objs Aluno
aluno_um = Aluno("Victor Arduini", 24)
aluno_dois = Aluno("Éric Silva", 23)

# instanciando objs Professor
professor_um = Professor("Paulo Rodrigues", 54, 5000.0, ["Cálculo 2", "Física 1"])

aluno_um.print_aluno()
aluno_dois.print_aluno()

professor_um.print_professor()
professor_um.idade = 60

professor_um.print_pessoa()
