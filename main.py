class Escola:
    def __init__(self, nome, endereco, cnpj):
        self.nome = nome
        self.endereco = endereco
        self.cnpj = cnpj
        self.salas = []

    def adicionar_sala(self, sala):
        self.salas.append(sala)

    def remover_sala(self, sala):
        if sala in self.salas:
            self.salas.remove(sala)


class SalaAula:
    def __init__(self, numero, capacidade, andar):
        self.numero = numero
        self.capacidade = capacidade
        self.andar = andar
        self.reservada = False

    def reservar(self):
        self.reservada = True

    def liberar(self):
        self.reservada = False


class Professor:
    def __init__(self, nome, matricula, especialidade):
        self.nome = nome
        self.matricula = matricula
        self.especialidade = especialidade

    def lecionar(self):
        print(f"{self.nome} está lecionando.")

    def atualizar_dados(self, nome=None, especialidade=None):
        if nome:
            self.nome = nome
        if especialidade:
            self.especialidade = especialidade


class Endereco:
    def __init__(self, logradouro, numero, cidade):
        self.logradouro = logradouro
        self.numero = numero
        self.cidade = cidade

    def atualizar(self, logradouro=None, numero=None, cidade=None):
        if logradouro:
            self.logradouro = logradouro
        if numero:
            self.numero = numero
        if cidade:
            self.cidade = cidade

    def exibir_endereco(self):
        return f"{self.logradouro}, {self.numero} - {self.cidade}"


class Aluno:
    def __init__(self, nome, matricula, curso, endereco):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.endereco = endereco

    def matricular(self):
        print(f"{self.nome} foi matriculado.")

    def atualizar_dados(self, nome=None, curso=None):
        if nome:
            self.nome = nome
        if curso:
            self.curso = curso


if __name__ == "__main__":
    escola = Escola("Escola Exemplo", "Rua Principal, 100", "00.000.000/0001-00")
    sala1 = SalaAula("101", 30, 1)
    escola.adicionar_sala(sala1)

    professor = Professor("João Silva", "P001", "Programação")
    endereco = Endereco("Rua das Flores", 50, "Parnaíba")
    aluno = Aluno("Maria Souza", "A001", "Análise e Desenvolvimento de Sistemas", endereco)

    sala1.reservar()
    professor.lecionar()
    aluno.matricular()

    print("Escola:", escola.nome)
    print("Salas:", len(escola.salas))
    print("Endereço do aluno:", aluno.endereco.exibir_endereco())
