import campo
import gerenciador

_girassois = {}

def inicializa():
	global _girassois

	campo.cultiva(Entities.Sunflower)
	_girassois[measure()].add((get_pos_x(), get_pos_y()))

def modo_girassol(objetivo):
	global _girassois

	for i in range(7, 16):
		_girassois[i] = set()

	while gerenciador.precisa(Items.Power, objetivo):
		campo.movimento(inicializa)
		
		for i in range(15, 6, -1):
			for x, y in _girassois[i]:
				campo.vai_para(x, y)
				while not can_harvest():
					campo.agua()
				harvest()
			_girassois[i] = set()
