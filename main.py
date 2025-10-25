import gerenciador

clear()

conquista = Unlocks.Watering
objetivos = get_cost(conquista)

do_a_flip()
gerenciador.alcanca_objetivos(objetivos)
unlock(conquista)
do_a_flip()
