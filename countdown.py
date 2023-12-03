from datetime import datetime

today = datetime.today()
day_of_year = today.strftime("%j")
year = today.strftime("%Y")

xmas = datetime(int(year), 12, 25)
xmas1 = xmas.strftime("%-j")
days_to_go = int(xmas1) - int(day_of_year)

name="thomas"
print('****')
# print(f'Ho! Ho! Ho! << {days_to_go} >> days until Christmas!')
ascii_art = rf'''
    ||::|:||   .--------,
    |:||:|:|   |_______ /        .-.
    ||::|:|| ."`  ___  `".    {{\\('v')/}}
    \\\/\///:  .'`   `'.  ;____`({{'v'}})'__
     \====/ './  o   o  \|~      ^" "^   |
      \\//   |   ())) .  |       {days_to_go}      |
       ||     \ `.__.'  /|   DAYS TO GO  |
       ||   _{{``-.___.-'\|               |
       || _." `-.____.-'`|    ___        |
       ||`        __ \   |___/   \_______|
     ."||        (__) \    \|     /
    /   `\/       __   vvvvv'\___/
    |     |      (__)        |
     \___/\                 /
       ||  |     .___.     |
       ||  |       |       |
       ||.-'       |       '-.
       ||          |          )
       ||----------'---------'
'''

print(ascii_art)
print(f'Ho! Ho! Ho! << {days_to_go} >> days until Christmas!')