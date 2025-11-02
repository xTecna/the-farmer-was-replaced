def enfila(fila, valor):
	no = {"valor": valor, "proximo": None}

	if not fila["frente"]:
		fila["frente"] = no
	else:
		fila["tras"]["proximo"] = no
	fila["tras"] = no

def desenfila(fila):
	velha_frente = fila["frente"]
	fila["frente"] = velha_frente["proximo"]

	return velha_frente["valor"]

def vazia(fila):
	return not fila["frente"]

def monta_enfila(fila):
	def funcao(valor):
		enfila(fila, valor)

	return funcao

def monta_desenfila(fila):
	def funcao():
		return desenfila(fila)

	return funcao

def monta_vazia(fila):
	def funcao():
		return vazia(fila)

	return funcao

def inicializa():
	fila = {"frente": None, "tras": None}

	fila["enfila"] = monta_enfila(fila)
	fila["desenfila"] = monta_desenfila(fila)
	fila["vazia"] = monta_vazia(fila)

	return fila
