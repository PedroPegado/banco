path = 'C:\\Users\\20211174010009\\Documents\\aulas\\banco\\Contas.txt'

with open(path, 'r') as f:
    contas = f.readlines()

print(contas)

class ContaBancaria:
    def __init__(self, numero):
        self.numero = numero

        if self.numero not in contas:
            print('Vimos que você não tem uma conta, crie: ')
            self.titular = input('Digite seu nome: ')
            self.saldo = '0.0'
            with open(path, 'w') as f:
                f.write(self.titular + '\n')
                f.write(self.numero + '\n')
                f.write(self.saldo + '\n')
    
    def depositar(self, valor):
        self.saldo = float(self.saldo)
        self.saldo += valor

emilly = ContaBancaria('002')


