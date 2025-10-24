import campo
import gerenciador
import fila

_fila = None

def inicializa():
	global _fila

	campo.cria_plant(Entities.Pumpkin, Grounds.Soil)()
	fila.enfila(_fila, (get_pos_x(), get_pos_y()))	

def verifica(x, y):
	global _fila

	if not can_harvest():
		fila.enfila(_fila, (x, y))

		if get_entity_type() == Entities.Dead_Pumpkin:
			campo.cultiva(Entities.Pumpkin)

def modo_abobora(objetivo):
	global _fila

	while gerenciador.precisa(Items.Pumpkin, objetivo):
		_fila = fila.inicializa()
		campo.movimento(inicializa)

		while not fila.vazia(_fila):
			x, y = fila.desenfila(_fila)
			campo.vai_para(x, y)
			verifica(x, y)
		
		harvest()
