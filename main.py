from Bliblioteca_banco import *
banco = Conta("002",0,"Cliente", "Corrente",True,0)

banco.depositar(29)
banco.depositar(3)

banco.sacar(100)
banco.verificar_saldo()
banco.ativar_conta()

----------------------------------------
