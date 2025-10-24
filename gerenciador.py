import abobora
import campo
import util

def limpa():
	if can_harvest():
		harvest()

	if get_ground_type() != Grounds.Grassland:
		till()

def cria_modo(recurso, acao):
	def funcao(objetivo):
		while precisa(recurso, objetivo):
			campo.movimento(acao)
	return funcao

ordem = [Items.Pumpkin, Items.Carrot, Items.Wood, Items.Hay]
recursos = {
	Items.Hay: {
		"planta": Entities.Grass,
		"preparo": None,
		"cultivo": cria_modo(Items.Hay, harvest),
		"finalizacao": None,
		"custo_ciclo": campo.n * campo.n,
		"producao_ciclo": 16 * campo.n * campo.n
	},
	Items.Wood: {
		"planta": Entities.Tree,
		"preparo": None,
		"cultivo": cria_modo(Items.Wood, campo.planta_madeira),
		"finalizacao": campo.cria_movimento(limpa),
		"custo_ciclo": campo.n * campo.n,
		"producao_ciclo": 8 * 3 * campo.n * campo.n
	},
	Items.Carrot: {
		"planta": Entities.Carrot,
		"preparo": campo.cria_movimento(campo.cria_plant(Entities.Carrot, Grounds.Soil)),
		"cultivo": cria_modo(Items.Carrot, campo.cria_harvest(Entities.Carrot)),
		"finalizacao": campo.cria_movimento(limpa),
		"custo_ciclo": campo.n * campo.n,
		"producao_ciclo": 4 * campo.n * campo.n
	},
	Items.Pumpkin: {
		"planta": Entities.Pumpkin,
		"preparo": None,
		"cultivo": abobora.modo_abobora,
		"finalizacao": campo.cria_movimento(limpa),
		"custo_ciclo": 2 * campo.n * campo.n,
		"producao_ciclo": campo.n * campo.n * min(campo.n, 6)
	}
}

def precisa(recurso, objetivo):
	return num_items(recurso) < objetivo

def alcanca_objetivos_rec(recurso, objetivo):
	if precisa(recurso, objetivo):
		dados = recursos[recurso]

		custo = get_cost(dados["planta"])
		for item in custo:
			qtd = custo[item]

			objetivo_real = (objetivo - num_items(recurso))
			n_ciclos = util.teto_div(objetivo_real, dados["producao_ciclo"])
			custo_real = dados["custo_ciclo"] * n_ciclos

			alcanca_objetivos_rec(item, qtd * custo_real)

		if dados["preparo"]:
			dados["preparo"]()
		dados["cultivo"](objetivo)
		if dados["finalizacao"]:
			dados["finalizacao"]()

def alcanca_objetivos(objetivos):
	for recurso in objetivos:
		alcanca_objetivos_rec(recurso, objetivos[recurso])
