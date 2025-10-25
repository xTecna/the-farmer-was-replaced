import campo
import gerenciador

clear()
campo.movimento(till)

conquistas = [Unlocks.Fertilizer]
for conquista in conquistas:
	objetivos = get_cost(conquista)
	gerenciador.alcanca_objetivos(objetivos)
	campo.limpa()
	unlock(conquista)
	do_a_flip()
