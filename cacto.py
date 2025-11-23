import campo
import gerenciador
import megafazenda

def insertion_sort(direcao, planta=False):
	x, y = get_pos_x(), get_pos_y()
	
	if planta:
		campo.cultiva(Entities.Cactus)

	for i in range(1, campo.n):
		x_proximo, y_proximo = campo.proximo(x, y, campo.opostos[direcao], i)
		campo.vai_para(x_proximo, y_proximo)
		if planta:
			campo.cultiva(Entities.Cactus)

		j = i
		while j > 0 and measure(direcao) > measure():
			swap(direcao)
			move(direcao)
			j -= 1

def cria_insertion_sort(direcao, planta=False):
	def funcao():
		insertion_sort(direcao, planta)

	return funcao

def modo_cacto(objetivo):
	while gerenciador.precisa(Items.Cactus, objetivo):
		megafazenda.paraleliza_linha(cria_insertion_sort(West, True))
		megafazenda.paraleliza_linha(cria_insertion_sort(South), False)

		campo.vai_para(0, 0)
		harvest()
