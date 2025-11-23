import campo
import chapeus
import gerenciador

_tudo_bem = True

def verifica():
	global _tudo_bem

	for direcao in campo.direcoes:
		if can_move(direcao):
			return

	_tudo_bem = False

def modo_dinossauro(objetivo):
	global _tudo_bem

	while gerenciador.precisa(Items.Bone, objetivo):
		campo.vai_para(0, 0)
		change_hat(Hats.Dinosaur_Hat)

		_tudo_bem = True
		while _tudo_bem:
			campo.movimento_bloco(campo.n, campo.n, verifica)

		chapeus.usa()
