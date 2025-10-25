import campo
import gerenciador

def inicializa():
	campo.cultiva(Entities.Cactus)

def insertion_sort(direcao):
	x, y = get_pos_x(), get_pos_y()
	x_delta, y_delta = campo.deltas[campo.opostos[direcao]]

	for i in range(1, campo.n):
		campo.vai_para(x + i * x_delta, y + i * y_delta)

		j = i
		while j > 0 and measure(direcao) > measure():
			swap(direcao)
			move(direcao)
			j -= 1

def modo_cacto(objetivo):
	while gerenciador.precisa(Items.Cactus, objetivo):
		campo.movimento(inicializa)

		for linha in range(campo.n):
			campo.vai_para(0, linha)
			insertion_sort(West)

		for coluna in range(campo.n):
			campo.vai_para(coluna, 0)
			insertion_sort(South)

		campo.vai_para(0, 0)
		harvest()
