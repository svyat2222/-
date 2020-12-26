import sys
w = sys.stdout.write
def t(n,s):
	for i in range (n):
		for a in range(n-i):
			w(" ")
		#конец елки слева
		w("[ета елка ета я сегодня 1 января")
		for l in range(i<<1):
			if i == n-1:
				#рисует послений рядок
				w("_")
			else:
				#рисует елку
				w("-")
		#конец елки справа
		w(" ета  елка ета я сегодня 1 января]")
		print("")
		
	#рисует низ елки
	for o in range(s):
		for i in range (n):
			w(" ")
		#бревно
		
		print("[ета елка ета я сегодня 1 января]")
			
# 10 - кол-во иголока, 2 - кол-во бревен
t(10, 2)
