import abobora
import campo
import girassol
import util

def nivel(conquista):
	return 2**(num_unlocked(conquista) - 1)

def cria_modo(recurso, acao):
	def funcao(objetivo):
		while precisa(recurso, objetivo):
			campo.movimento(acao)
	return funcao

ordem = [Items.Power, Items.Pumpkin, Items.Carrot, Items.Wood, Items.Hay]
recursos = {
	Items.Hay: {
		"planta": Entities.Grass,
		"preparo": None,
		"cultivo": cria_modo(Items.Hay, harvest),
		"finalizacao": None,
		"custo_ciclo": campo.n * campo.n,
		"producao_ciclo": nivel(Unlocks.Grass) * campo.n * campo.n
	},
	Items.Wood: {
		"planta": Entities.Tree,
		"preparo": None,
		"cultivo": cria_modo(Items.Wood, campo.planta_madeira),
		"finalizacao": campo.limpa,
		"custo_ciclo": campo.n * campo.n,
		"producao_ciclo": nivel(Unlocks.Trees) * 3 * campo.n * campo.n
	},
	Items.Carrot: {
		"planta": Entities.Carrot,
		"preparo": campo.cria_movimento(campo.cria_plant(Entities.Carrot, Grounds.Soil)),
		"cultivo": cria_modo(Items.Carrot, campo.cria_harvest(Entities.Carrot)),
		"finalizacao": campo.limpa,
		"custo_ciclo": campo.n * campo.n,
		"producao_ciclo": nivel(Unlocks.Carrots) * campo.n * campo.n
	},
	Items.Pumpkin: {
		"planta": Entities.Pumpkin,
		"preparo": None,
		"cultivo": abobora.modo_abobora,
		"finalizacao": campo.limpa,
		"custo_ciclo": 2 * campo.n * campo.n,
		"producao_ciclo": nivel(Unlocks.Pumpkins) * campo.n * campo.n * 6
	},
	Items.Power: {
		"planta": Entities.Sunflower,
		"preparo": None,
		"cultivo": girassol.modo_girassol,
		"finalizacao": campo.limpa,
		"custo_ciclo": campo.n * campo.n,
		"producao_ciclo": nivel(Unlocks.Sunflowers) * 5 * ((campo.n * campo.n) - 9) + 9
	}
}

def calcula_objetivos_rec(recurso, objetivo):
	resposta = 0

	if precisa(recurso, objetivo):
		dados = recursos[recurso]

		objetivo_real = (objetivo - num_items(recurso))
		n_ciclos = util.teto_div(objetivo_real, dados["producao_ciclo"])
		custo_real = dados["custo_ciclo"] * n_ciclos

		resposta = custo_real

		custo = get_cost(dados["planta"])
		for item in custo:
			qtd = custo[item]
			resposta += calcula_objetivos_rec(item, qtd * custo_real)

	return resposta

def calcula_objetivos(objetivos):
	resposta = 0

	for recurso in ordem:
		if recurso not in objetivos:
			continue
		resposta += calcula_objetivos_rec(recurso, objetivos[recurso])

	return resposta

def precisa(recurso, objetivo):
	return num_items(recurso) < objetivo

def alcanca_objetivos_rec(recurso, objetivo):
	if precisa(recurso, objetivo):
		dados = recursos[recurso]
		
		objetivo_real = (objetivo - num_items(recurso))
		n_ciclos = util.teto_div(objetivo_real, dados["producao_ciclo"])
		custo_real = dados["custo_ciclo"] * n_ciclos

		custo = get_cost(dados["planta"])
		for item in custo:
			qtd = custo[item]
			alcanca_objetivos_rec(item, qtd * custo_real)

		if dados["preparo"]:
			dados["preparo"]()
		dados["cultivo"](objetivo)
		if dados["finalizacao"]:
			dados["finalizacao"]()

def alcanca_objetivos(objetivos):
	global ordem

	objetivos[Items.Power] = util.teto_div(calcula_objetivos(objetivos), 30)

	for recurso in ordem:
		if recurso not in objetivos:
			continue
		alcanca_objetivos_rec(recurso, objetivos[recurso])
