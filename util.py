def teto_div(a, b):
	if a % b > 0:
		return a // b + 1
	return a // b

def insertion_sort(v, comp):
	for i in range(1, len(v)):
		j = i
		while j > 0 and comp(v[j - 1], v[j]):
			v[j - 1], v[j] = v[j], v[j - 1]
			j -= 1
