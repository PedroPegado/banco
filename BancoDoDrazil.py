path = 'C:\\Users\\saped\\Documents\\GitHub\\banco\\Contas.txt'

with open(path, 'r') as f:
    contas = f.readlines()

profiles = []

class ContaBancaria:
    def __init__(self, numero):
        self.numero = numero
        cont1 = 0
        for c in profiles:
            if c == self.numero:
                break
            cont1+=1
        contaN = contas[cont1].split('/')
        self.titular = contaN[0]
        self.saldo = contaN[2]
        cont = 0
        while cont != len(contas):
            contaN = contas[cont].split('/')
            profiles.append(contaN[1])
            cont+=1
        if self.numero not in profiles:
            self.criarConta()
            
    def criarConta(self):
        self.titular = input('Digite seu nome:')
        self.saldo = 0
        with open(path, 'a') as f:
            f.write(f'{self.titular}/{self.numero}/{self.saldo}\n')
                
    def depositar(self, valor):
        cont = 0
        for c in profiles:
            if c == self.numero:
                break
            cont+=1
        contaN = contas[cont].split('/')
        self.saldo = float(self.saldo)
        self.saldo += valor
        self.saldo = str(self.saldo)
        with open(path, 'w') as f:
            f.write(f'{self.titular}/{self.numero}/{self.saldo}\n')
        
pedro = ContaBancaria('007')

