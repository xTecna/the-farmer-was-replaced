def inicializa():
	return {"frente": None, "ultimo": None}

def vazia(f):
	return not f["frente"]

def enfila(f, valor):
	no = {"valor": valor, "proximo": None}
	if vazia(f):
		f["frente"] = no
	else:
		f["ultimo"]["proximo"] = no
	f["ultimo"] = no

def desenfila(f):
	valor_frente = f["frente"]["valor"]
	f["frente"] = f["frente"]["proximo"]
	if not f["frente"]:
		f["ultimo"] = None
	return valor_frente
