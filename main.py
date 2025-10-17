n = get_world_size()

def movimento(acao):
	for _ in range(n):
		for _ in range(n - 1):
			acao()
			move(North)
		acao()
		move(East)

def pronto(feno, madeira, cenoura):
	return num_items(Items.Hay) >= feno and num_items(Items.Wood) >= madeira and num_items(Items.Carrot) >= cenoura

def agua():
	if num_items(Items.Water) > 0 and get_water() < 0.5:
		use_item(Items.Water)

def cria_plant(planta, solo):
	def funcao():
		if can_harvest():
			harvest()
		if get_ground_type() != solo:
			till()
		plant(planta)
		agua()

	return funcao

def planta_madeira():
	if not get_entity_type() or can_harvest():
		harvest()

		x = get_pos_x()
		y = get_pos_y()

		if x % 2 == y % 2:
			plant(Entities.Tree)
		else:
			plant(Entities.Bush)
		agua()

def cria_harvest(planta):
	def funcao():
		if can_harvest():
			harvest()
			plant(planta)
			agua()

	return funcao

clear()

objetivo_feno = 300
objetivo_madeira = 0
objetivo_cenoura = 0

objetivo_real_feno = objetivo_feno + objetivo_cenoura - num_items(Items.Carrot)
objetivo_real_madeira = objetivo_madeira + objetivo_cenoura - num_items(Items.Carrot)

while not pronto(objetivo_feno, objetivo_madeira, objetivo_cenoura):
	while num_items(Items.Hay) < objetivo_real_feno:
		movimento(harvest)

	while num_items(Items.Wood) < objetivo_real_madeira:
		movimento(planta_madeira)

	if num_items(Items.Carrot) < objetivo_cenoura:
		movimento(cria_plant(Entities.Carrot, Grounds.Soil))
		while num_items(Items.Carrot) < objetivo_cenoura:
			movimento(cria_harvest(Entities.Carrot))