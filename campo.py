n = get_world_size()
metade_n = n // 2

opostos = {
	North: South,
	South: North,
	East: West,
	West: East
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

def limpa():
	def funcao():
		if can_harvest():
			harvest()
		if get_ground_type() != Grounds.Grassland:
			till()

	movimento(funcao)

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
	if num_items(Items.Water) > 0 and get_water() < 0.5:
		use_item(Items.Water)

def cultiva(planta):
	plant(planta)
	agua()

def prepara(planta, solo):
	if can_harvest():
		harvest()
	if get_ground_type() != solo:
		till()
	cultiva(planta)

def cria_plant(planta, solo):
	def funcao():
		prepara(planta, solo)

	return funcao

def planta_madeira():
	if not get_entity_type() or can_harvest():
		harvest()

		x = get_pos_x()
		y = get_pos_y()

		if x % 2 == y % 2:
			cultiva(Entities.Tree)
		else:
			cultiva(Entities.Bush)

def cria_harvest(planta):
	def funcao():
		if can_harvest():
			harvest()
			cultiva(planta)

	return funcao
