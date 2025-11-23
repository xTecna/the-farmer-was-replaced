import campo
import chapeus
import gerenciador
import megafazenda

def inicializa(conquista=None):
	campo.inicializa()
	chapeus.inicializa()
	megafazenda.inicializa()
	gerenciador.inicializa()

	if conquista == Unlocks.Expand:
		campo.ara()

clear()
inicializa(Unlocks.Expand)
chapeus.usa()

conquistas = list(Unlocks)
while True:
	conquista = gerenciador.escolha_conquista(conquistas)
	if not conquista:
		break

	print(conquista)

	objetivos = get_cost(conquista)
	gerenciador.alcanca_objetivos(objetivos)

	unlock(conquista)
	do_a_flip()

	inicializa(conquista)
