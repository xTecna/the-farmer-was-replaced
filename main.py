import campo
import gerenciador

clear()
campo.movimento(till)

conquistas = [Unlocks.Simulation]
for conquista in conquistas:
	objetivos = get_cost(conquista)
	gerenciador.alcanca_objetivos(objetivos)
	unlock(conquista)
	do_a_flip()
