import campo
import chapeus
import util

n_drones = 0
linhas = 0
colunas = 0

_limite_linhas = 0
_limite_colunas = 0

def inicializa():
	global n_drones
	global linhas
	global colunas
	global _limite_linhas
	global _limite_colunas

	n_drones = max_drones()

	drones_por_linha = util.sqrt_2(n_drones)
	drones_por_coluna = n_drones // drones_por_linha

	linhas = campo.n // drones_por_linha
	colunas = campo.n // drones_por_coluna
	if colunas % 2 == 1:
		colunas -= 1

	_limite_linhas = linhas * drones_por_linha
	_limite_colunas = colunas * drones_por_coluna

def paraleliza_linha(acao, por_linha=True):
	drones = []
	resultados = []

	for i in range(campo.n):
		if por_linha:
			campo.vai_para(0, i)
		else:
			campo.vai_para(i, 0)

		drone = spawn_drone(chapeus.usa_e_faz(acao))
		if drone:
			drones.append(drone)
		else:
			resultados.append(chapeus.usa_e_faz(acao)())

	for drone in drones:
		resultados.append(wait_for(drone))

	return resultados

def paraleliza_blocos(acao):
	drones = []
	resultados = []

	for x in range(0, _limite_colunas, colunas):
		for y in range(0, _limite_linhas, linhas):
			campo.vai_para(x, y)

			drone = spawn_drone(chapeus.usa_e_faz(acao))
			if drone:
				drones.append(drone)
			else:
				resultados.append(chapeus.usa_e_faz(acao)())

	for drone in drones:
		resultados.append(wait_for(drone))

	return resultados
