def Taiwan_receipt_lottery(special_prize,first_prize,receipt):
	money = 0
	for i in range(len(receipt)):
		for j in range(3):
			if receipt[i] == special_prize[j]:
				money += 2000000
			if receipt[i] == first_prize[j]:
				money += 200000
			elif receipt[i][1:] == first_prize[j][1:]:
				money += 40000
			elif receipt[i][2:] == first_prize[j][2:]:
				money += 10000
			elif receipt[i][3:] == first_prize[j][3:]:
				money += 4000
			elif receipt[i][4:] == first_prize[j][4:]:
				money += 1000
			elif receipt[i][5:] == first_prize[j][5:]:
				money += 200
	return money

special_prize = []
first_prize = []
receipt = []

for _ in range(3):
	special_prize.append(input())
for _ in range(3):
	first_prize.append(input())
N = eval(input())
for _ in range(N):
	receipt.append(input())
print(Taiwan_receipt_lottery(special_prize,first_prize,receipt))