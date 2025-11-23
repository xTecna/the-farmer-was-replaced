_n_chapeus = 0
_chapeus = []

def inicializa():
	global _n_chapeus
	global _chapeus

	_chapeus = []
	for chapeu in Hats:
		if chapeu == Hats.Dinosaur_Hat:
			continue
		if num_unlocked(chapeu):
			_chapeus.append(chapeu)

	_n_chapeus = len(_chapeus)

def usa():
	indice = _n_chapeus * random() // 1
	change_hat(_chapeus[indice])

def usa_e_faz(acao):
	def funcao():
		usa()
		return acao()

	return funcao
