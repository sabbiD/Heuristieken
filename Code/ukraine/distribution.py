from score import score
import csv

dist = score()


def distribution(score):
	radio = []
	for key in score:
		
		div = score.get(key)
		div = round((div/27)*100, 1)
		radio.append(div) 

	return radio

print(distribution(dist))



	
		
