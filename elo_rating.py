"""
Those functions are used to create an Elo ranking system.

By Hugo Mechiche - 10 jan. 2021
"""

#Calculates a player's probability of winning
def probalityForPlayer(player_score):
	prob = player_score / (1 + player_score)
	return prob

#Calculates the probality for playerX to win according to
# the score difference he has with playerY
def probalityDifference(prob_playerX, prob_playerY):
	pD = prob_playerX / (prob_playerX + prob_playerY)
	return pD

#Calculates the number of points a player earns based on
# the outcome of the game and the probability of difference.
def eloModification(player_coeff, result, pD_player):
	E = player_coeff * (result + pD_player)
	return E

def playerCoefficient(player_score, player_number_of_games):
	if player_number_of_games < 30:
		K = 40
	else:
		if player_score < 2400:
			K = 20
		elif player_score >= 2400:
			K = 10
	return K
