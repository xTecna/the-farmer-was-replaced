import campo
import gerenciador
import megafazenda
import util

_visitados = set()
_x_tesouro = 0
_y_tesouro = 0

def comp(a, b):
	return a[0] > b[0]

def dfs(x, y):
	global _visitados
	global _x_tesouro
	global _y_tesouro

	_visitados.add((x, y))

	if get_entity_type() == Entities.Treasure:
		return True

	direcoes = []
	for direcao in campo.direcoes:
		x_proximo, y_proximo = campo.proximo(x, y, direcao)
		direcoes.append((campo.distancia(x_proximo, y_proximo, _x_tesouro, _y_tesouro), direcao, x_proximo, y_proximo))
	util.insertion_sort(direcoes, comp)

	for _, direcao, x_proximo, y_proximo in direcoes:
		if can_move(direcao) and (x_proximo, y_proximo) not in _visitados:
			move(direcao)
			if dfs(x_proximo, y_proximo):
				return True
			move(campo.opostos[direcao])

	return False

def tarefa(objetivo):
	def funcao():
		global _visitados
		global _x_tesouro
		global _y_tesouro
	
		custo = gerenciador.nivel(Unlocks.Mazes) * min(megafazenda.linhas, megafazenda.colunas)
		x_meio, y_meio = get_pos_x() + megafazenda.colunas // 2, get_pos_y() + megafazenda.linhas // 2
	
		while gerenciador.precisa(Items.Gold, objetivo):
			campo.vai_para(x_meio, y_meio)
			campo.cultiva(Entities.Bush)
	
			for _ in range(301):
				use_item(Items.Weird_Substance, custo)
	
				x, y = get_pos_x(), get_pos_y()
				_visitados = set()
				_x_tesouro, _y_tesouro = measure()
				dfs(x, y)
			harvest()

	return funcao

def modo_labirinto(objetivo):
	megafazenda.paraleliza_blocos(tarefa(objetivo))
	clear()
	campo.ara()
