class SaldoNegativoErro(Exception):
    pass

class SaqueMenorIgualZero(Exception):
    pass

try:  
    saldo = float(input("Informe o saldo bancário.\n"))
    saque = float(input("Insira a quantia que deseja sacar.\n"))

    if saldo < saque:
        raise SaldoNegativoErro

    if saque <= 0:
        raise SaqueMenorIgualZero

except ValueError:
    print("Erro de valor. Digite um número")

except SaldoNegativoErro:
    print("Valor de saque maior do que saldo na conta")

except SaqueMenorIgualZero:
    print("Saque não pode ser menor ou igual a zero")

else:
    saldo -= saque
    print(f"Saldo restante: {saldo}")

finally:
    print("Operação bancária finalizada.")
