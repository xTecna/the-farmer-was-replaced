import campo
import gerenciador

def inicializa(conquista=None):
	campo.inicializa()
	gerenciador.inicializa()

	if conquista == Unlocks.Expand:
		campo.movimento(till)

clear()
inicializa(Unlocks.Expand)

conquistas = list(Unlocks)
while True:
	conquista = gerenciador.escolha_conquista(conquistas)
	if not conquista:
		break

	print(conquista)
	if conquista == Unlocks.Megafarm:
		do_a_flip()
		pet_the_piggy()
		break

	objetivos = get_cost(conquista)
	gerenciador.alcanca_objetivos(objetivos)

	unlock(conquista)
	do_a_flip()
