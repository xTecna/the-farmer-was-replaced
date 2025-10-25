import campo
import gerenciador

clear()
campo.movimento(till)

conquistas = [Unlocks.Dinosaurs]
for conquista in conquistas:
	#objetivos = get_cost(conquista)
	objetivos = {Items.Cactus: 100000}
	gerenciador.alcanca_objetivos(objetivos)
	#campo.limpa()
	#unlock(conquista)
	#do_a_flip()
