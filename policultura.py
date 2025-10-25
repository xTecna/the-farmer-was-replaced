import campo
import gerenciador

_voto_por_casa = {}
_votos_pra_casa = {}
_plantas = [Entities.Grass, Entities.Bush, Entities.Tree, Entities.Carrot]

def cria_modo_policultura(recurso, planta):
	def funcao(objetivo):
		modo_policultura(recurso, planta, objetivo)

	return funcao

def decide_planta(x, y, planta):
	global _voto_por_casa
	global _votos_pra_casa

	planta_vencedora = planta
	votos_vencedores = 0
	for candidata in _votos_pra_casa[(x, y)]:
		votos = _votos_pra_casa[(x, y)][candidata]
		if votos > votos_vencedores:
			planta_vencedora = candidata
			votos_vencedores = votos

	return planta_vencedora

def vota(x, y):
	global _voto_por_casa
	global _votos_pra_casa

	candidata, (x_candidata, y_candidata) = get_companion()
	if _voto_por_casa[(x, y)]:
		candidata_anterior, x_candidata_anterior, y_candidata_anterior = _voto_por_casa[(x, y)]
		_votos_pra_casa[(x_candidata_anterior, y_candidata_anterior)][candidata_anterior] -= 1
	_voto_por_casa[(x, y)] = (candidata, x_candidata, y_candidata)
	_votos_pra_casa[(x_candidata, y_candidata)][candidata] += 1

def cultiva_e_vota(planta):
	def funcao():
		x, y = get_pos_x(), get_pos_y()
	
		vencedora = decide_planta(x, y, planta)
		campo.colhe_e_cultiva(vencedora)
		if vencedora == planta:
			vota(x, y)

	return funcao

def modo_policultura(recurso, planta, objetivo):
	global _voto_por_casa
	global _votos_pra_casa

	for x in range(campo.n):
		for y in range(campo.n):
			_voto_por_casa[(x, y)] = None
			_votos_pra_casa[(x, y)] = {}
			for p in _plantas:
				if p == planta:
					continue
				_votos_pra_casa[(x, y)][p] = 0

	while gerenciador.precisa(recurso, objetivo):
		campo.movimento(cultiva_e_vota(planta))

	campo.limpa()
