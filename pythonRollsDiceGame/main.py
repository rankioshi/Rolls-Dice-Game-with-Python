#====== JOGO DE DADOS ==========
'''
escolhe quanto apostar
rola os dados
se a soma for 7 -> ganha o dobro
se a soma for 12 || 2 -> ganha o triplo
se digitar zero (0) -> fim de jogo
se acabar o dinheiro -> fim de jogo
'''
import random

money = 100 # quantidade atual de dinheiro
min_bet = 10 # aposta mínima
current_bet = 0 # aposta atual
die_1 = 0 # primeiro dado
die_2 = 0 # segundo dado
dice = 0 # soma dos dados 1 e 2

def bet():
	global money # sempre que voce ta dentro de uma funçao o python n reconhece mais as variaveis, entao o global serve para puxar as variaveis (podia só criar uma nova tbm)
	global current_bet
	global min_bet
	current_bet = money + 1
	while current_bet > money or current_bet < min_bet:
		current_bet = int(input("Quanto quer apostar? "))
		if current_bet > money:
			print("Você tem apenas", money)
		elif current_bet < min_bet:
			print("Aposta mínima:", min_bet)
	money = money - current_bet
	print("Você apostou", current_bet)

def draw_info():
	global money
	print("Faça sua aposta")
	print("Saldo atual", money)

def loose(m):
	print()
	print("Não foi dessa vez!!!")
	print()
	if m >= min_bet:
		print("Você ainda tem", m)
	else:
		print("Você está falido(a)")
		print("FIM DE JOGO")

def win(result):
	global money
	global current_bet
	print()
	print("Parabéns!!!")
	if result == 7:
		money = money + (2 * current_bet)
		print("Você ganhou", current_bet)
	elif result == 12 or result == 2:
		money = money + (3 * current_bet)
		print("Você ganhou", current_bet * 2)
	print()

def roll_dice():
	global die_1
	global die_2
	global dice
	die_1 = random.randint(1, 6)
	die_2 = random.randint(1, 6)
	print("Rolls:", die_1, "e", die_2)
	dice = die_1 + die_2

def test_result(d):
	global money
	if d == 7 or d == 2 or d == 12:
		win(d)
	else:
		loose(money)
	

while money > 0:
	draw_info()
	bet()
	roll_dice()
	test_result(dice)