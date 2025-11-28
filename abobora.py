import campo
import gerenciador
import fila

_fila = None

def inicializa():
	global _fila

	campo.cultiva(Entities.Pumpkin)
	_fila["enfila"]((get_pos_x(), get_pos_y()))	

def verifica(x, y):
	global _fila

	if not can_harvest():
		_fila["enfila"]((x, y))

		if get_entity_type() == Entities.Dead_Pumpkin:
			campo.cultiva(Entities.Pumpkin)

def modo_abobora(objetivo):
	global _fila

	while gerenciador.precisa(Items.Pumpkin, objetivo):
		_fila = fila.inicializa()
		campo.movimento(inicializa)

		while not _fila["vazia"]():
			x, y = _fila["desenfila"]()
			campo.vai_para(x, y)
			verifica(x, y)
		
		harvest()
