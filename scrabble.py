letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters_to_points = {key:value for key, value in zip(letters, points)}

#print(letters_to_points)

letters_to_points[" "] = 0
#print(letters_to_points)

def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letters_to_points.get(letter, 0)
  return point_total

#print(score_word("BROWNIE"))

player_to_words = {"player1": ["OCTOPUS", "BASEBALL", "ENTRY"], "player2":["PLANET","NOSES", "SYSTEM"], "player3": ["SHADE", "FINGERS", "AUTOMOBILE"], "player4": ["ZEBRA", "ABSENSE", "SEMESTERS"]}

player_to_points = {}

for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points

print(player_to_points)


  




