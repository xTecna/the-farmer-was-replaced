import abobora
import campo
import girassol
import policultura
import util

def nivel(conquista):
	return 2**(num_unlocked(conquista) - 1)

ordem = [Items.Power, Items.Pumpkin, Items.Carrot, Items.Wood, Items.Hay]
recursos = {
	Items.Hay: {
		"planta": Entities.Grass,
		"cultivo": policultura.cria_modo_policultura(Items.Hay, Entities.Grass),
		"custo_ciclo": campo.n * campo.n,
		"producao_ciclo": nivel(Unlocks.Grass) * campo.n * campo.n
	},
	Items.Wood: {
		"planta": Entities.Tree,
		"cultivo": policultura.cria_modo_policultura(Items.Wood, Entities.Bush),
		"custo_ciclo": campo.n * campo.n,
		"producao_ciclo": nivel(Unlocks.Trees) * 3 * campo.n * campo.n
	},
	Items.Carrot: {
		"planta": Entities.Carrot,
		"cultivo": policultura.cria_modo_policultura(Items.Carrot, Entities.Carrot),
		"custo_ciclo": campo.n * campo.n,
		"producao_ciclo": nivel(Unlocks.Carrots) * campo.n * campo.n
	},
	Items.Pumpkin: {
		"planta": Entities.Pumpkin,
		"cultivo": abobora.modo_abobora,
		"custo_ciclo": 2 * campo.n * campo.n,
		"producao_ciclo": nivel(Unlocks.Pumpkins) * campo.n * campo.n * 6
	},
	Items.Power: {
		"planta": Entities.Sunflower,
		"cultivo": girassol.modo_girassol,
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

		dados["cultivo"](objetivo)

def alcanca_objetivos(objetivos):
	global ordem

	objetivos[Items.Power] = util.teto_div(calcula_objetivos(objetivos), 30)

	for recurso in ordem:
		if recurso not in objetivos:
			continue
		alcanca_objetivos_rec(recurso, objetivos[recurso])
