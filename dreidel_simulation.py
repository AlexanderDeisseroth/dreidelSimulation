import random

dreidel = ['shin', 'hey', 'gimel', 'nun']

players = input('players:')
rounds = input('rounds:')

pot = 0

player_list = {}
for player in range(int(players)):
  player_list['player'+str(player)] = 10

print(player_list)

for round in range(int(rounds)):
  print('round: '+str(round))
  for player in player_list:
    if player_list[player] != 0:
      pot += 1
      player_list[player] -= 1
  for player in range(int(players)):
    if player_list['player'+str(player)] != 0:
      print('player: '+str(player))
      print("player " + str(player)+"'s stack: "+str(player_list['player'+str(player)]))
      spin = random.choice(dreidel)
      print('spin: '+spin)
      if spin == 'gimel':
        player_list['player'+str(player)] += pot
        pot = 0
      elif spin == 'hey':
        half_pot = pot/2
        print(half_pot)
        rounded_half_pot = int(half_pot)
        player_list['player'+str(player)] += rounded_half_pot
        pot -= rounded_half_pot
      elif spin == 'shin':
        pot += 1
        player_list['player'+str(player)] -= 1
      print("player " + str(player)+"'s stack: "+str(player_list['player'+str(player)]))
      print('pot: '+str(pot))
      print('')
    

print(player_list)