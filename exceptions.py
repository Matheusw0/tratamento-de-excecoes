try:
    n1 = float(input("Insira um número\n"))
    n2 = float(input("Insira um número\n"))

    div = n1/n2

    print(f"Resultado = {div}")

except ZeroDivisionError:
    print("Erro: não é possível dividir por zero.")
except ValueError:
    print("Erro: valor invalido")
finally:
    print("Operação finalizada")
