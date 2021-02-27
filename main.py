# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scorer_name_0 = 'Ruud Gullit'
scorer_name_1 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
scorers = scorer_name_0 + " " + str(goal_0) + ", " + scorer_name_1 + " " + str(goal_1)

report = (f'{scorer_name_0} scored in the {goal_0}nd minute\n{scorer_name_1} scored in the {goal_1}th minute')

print(report)

player = 'Sergey Gotsmanov'
first_name = player[:player.find(' ')]
print(first_name)
last_name_len = len(player[player.find(' ')+1:])
print(last_name_len)
name_short = f'{player[0]}. {player[player.find(" ")+1:]}'
print(name_short)
chant = ((first_name+'! ')*(len(first_name)))[:-1]
print(chant)
good_chant = chant[-1]!=' '
print(good_chant)