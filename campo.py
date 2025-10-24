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

def vai_para(x_destino, y_destino):
	x, y = get_pos_x(), get_pos_y()

	dir_horizontal = East
	if x_destino < x:
		dir_horizontal = West
	dist_horizontal = abs(x_destino - x)
	if dist_horizontal > metade_n:
		dist_horizontal = n - dist_horizontal
		dir_horizontal = opostos[dir_horizontal]

	dir_vertical = North
	if y_destino < y:
		dir_vertical = South
	dist_vertical = abs(y_destino - y)
	if dist_vertical > metade_n:
		dist_vertical = n - dist_vertical
		dir_vertical = opostos[dir_vertical]

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

def cria_plant(planta, solo):
	def funcao():
		if can_harvest():
			harvest()
		if get_ground_type() != solo:
			till()
		cultiva(planta)

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
