"""
OPEN CLOSED PRINCIPLE

Imagine que uma clínica veterinária tem seu sistema próprio para aprovação de exames. No primeiro momento, ela tem um método para
verificar exame de sangue. Em outro ela adiciona exame por raio-x. Notamos no código que, conforme a clínica adiciona exames,
deverão adicionar uma validação para o exame. O que aumentaria a complexidade do código e a manutenção do mesmo.

A solução deste caso pode ser feita com o princípio aberto-fechado (Open Closed Principle).
Utilizando do conceito do OCP, crie uma interface e classes que implementam a mesma para que, caso a clínica necessite de um novo
tipo de exame, uma nova classe seja adicionada, implementando métodos de uma interface padrão para exames.

"""
from abc import ABC, abstractmethod


# Interface padrão
class Exame(ABC):
    @abstractmethod
    def aprovar(self):
        pass


# Implementação para exame de sangue
class ExameSangue(Exame):
    def aprovar(self):
        # Condições específicas do exame de sangue
        print("Exame de sangue aprovado!")


# Implementação para exame de raio-x
class ExameRaioX(Exame):
    def aprovar(self):
        # Condições específicas do exame de raio-x
        print("Exame de raio-x aprovado!")


# Classe responsável apenas por aprovar exames (sem lógica específica)
class AprovadorExames:
    def aprovar_solicitacao_exame(self, exame: Exame):
        exame.aprovar()


# Exemplo de uso
if __name__ == "__main__":
    aprovador = AprovadorExames()

    exame1 = ExameSangue()
    exame2 = ExameRaioX()

    aprovador.aprovar_solicitacao_exame(exame1)
    aprovador.aprovar_solicitacao_exame(exame2)
