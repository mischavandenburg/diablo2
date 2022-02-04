from pathlib import Path, PurePath
import re, os

# path to data files
source = Path(Path.cwd() / 'data' )

total_games = 0
pindle_total = 0
eldritch_total = 0
shenk_total = 0
nihla_total = 0

regex_games = re.compile(r"Games:")
regex_dict = {
'nihla': 'Nihl|Nihlatak',
'pindle': 'Pin|Pindle',
'eldritch': 'Eld'
}

for folder_name, sub_folder, file_names in os.walk(source):
    for filename in file_names:
        p = PurePath(folder_name, filename)
        with open(p, 'rt') as my_file:
            # search for games number line
            for line in my_file:
                # find number of games and add to total games
                if regex_games.search(line):
                    g = line.split()
                    total_games += int(g[1])
                    f = my_file.read()

                    # check which runs were done by using the regex dict
                    for key in regex_dict:
                        location = regex_dict[key]
                        reg = re.compile(location)
                        # if there is a match, add the numbers to the total variable
                        if reg.search(f):
                            var_name = key + '_total'
                            globals()[var_name] += int(g[1])

# print the result
print('Total runs: ' + str(total_games))
print('Pindle runs: ' + str(pindle_total))
print('Eldritch + Shenk runs: ' + str(eldritch_total))
print('Nihla runs: ' + str(nihla_total))


