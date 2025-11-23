import campo
import chapeus
import gerenciador
import megafazenda

_girassois = {}

def inicializa():
	global _girassois

	campo.cultiva(Entities.Sunflower)
	_girassois[measure()].add((get_pos_x(), get_pos_y()))

def tarefa_plantio():
	global _girassois

	campo.movimento_linha(inicializa)
	return _girassois

def constroi_resultados(resultados):
	global _girassois

	for resultado in resultados:
		for i in range(7, 16):
			for x, y in resultado[i]:
				_girassois[i].add((x, y))

def tarefa_colheita(x, y):
	def funcao():
		campo.vai_para(x, y)
		campo.colhe()

	return chapeus.usa_e_faz(funcao)

def modo_girassol(objetivo):
	global _girassois

	for i in range(7, 16):
		_girassois[i] = set()

	while gerenciador.precisa(Items.Power, objetivo):
		resultados = megafazenda.paraleliza_linha(tarefa_plantio)
		constroi_resultados(resultados)

		for i in range(15, 6, -1):
			drones = []

			for x, y in _girassois[i]:
				campo.vai_para(campo.metade_n, campo.metade_n)

				drone = None
				while not drone:
					drone = spawn_drone(tarefa_colheita(x, y))
				drones.append(drone)

			for drone in drones:
				wait_for(drone)

			_girassois[i] = set()
