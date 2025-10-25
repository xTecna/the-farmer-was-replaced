n = get_world_size()
metade_n = n // 2

opostos = {
	North: South,
	South: North,
	East: West,
	West: East
}
deltas = {
	North: (0, 1),
	South: (0, -1),
	East: (1, 0),
	West: (-1, 0)
}

def movimento(acao):
	for _ in range(n):
		for _ in range(n - 1):
			acao()
			move(North)
		acao()
		move(East)

def cria_movimento(acao):
	def funcao():
		movimento(acao)

	return funcao

def colhe():
	while get_entity_type() and not can_harvest():
		pass
	harvest()

def limpa():
	movimento(colhe)

def define_dimensoes(p, p_destino, direcao):
	if p_destino < p:
		direcao = opostos[direcao]

	dist = abs(p_destino - p)
	if dist > metade_n:
		dist = n - dist
		direcao = opostos[direcao]

	return dist, direcao

def vai_para(x_destino, y_destino):
	x, y = get_pos_x(), get_pos_y()
	
	dist_horizontal, dir_horizontal = define_dimensoes(get_pos_x(), x_destino, East)
	dist_vertical, dir_vertical = define_dimensoes(get_pos_y(), y_destino, North)

	for _ in range(dist_horizontal):
		move(dir_horizontal)
	for _ in range(dist_vertical):
		move(dir_vertical)

def agua():
	if num_items(Items.Water) > 0 and get_water() <= 0.75:
		use_item(Items.Water)

def cultiva(planta):
	plant(planta)
	agua()

def colhe_e_cultiva(planta):
	colhe()
	cultiva(planta)
