from pathlib import Path, PurePath
import re, os

# path to data files
source = Path(Path.home() / 'python' / 'diablo2' / 'stats_parser' / 'data' )

total_games = 0
pindle_total = 0
eldritch_total = 0
shenk_total = 0
nihla_total = 0
travincal_total = 0
diablo_total = 0
total_list = []

regex_games = re.compile(r"Games:")
regex_dict = {
'nihla': 'Nihl|Nihlatak',
'pindle': 'Pin|Pindle',
'eldritch': 'Eld',
'travincal': 'Trav',
'diablo': 'Dia'
}

# encountered a problem that the script stops on .DS store files. 
# TODO implement that the file is skipped if the filename contains DS store
# for now use this command on mac to delete all .DS_Store files recursively 
# find . -name '.DS_Store' -type f -delete

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
                    file_read = my_file.read()

                    # check which runs were done by using the regex dict
                    for key in regex_dict:
                        reg = re.compile(regex_dict[key])
                        # if there is a match, add the numbers to the total variable
                        if reg.search(file_read):
                            globals()[f"{key}_total"] += int(g[1])

# print the result
print(f"Mephisto runs: 1300")
print(f"Lower Kurast runs: 1700")
print(f"Pit runs: 300")
print(f"Pindle runs: {pindle_total}")
print(f"Eldritch + Shenk runs: {eldritch_total}")
print(f"Nihla runs: {nihla_total}")
print(f"Travi runs: {travincal_total}")
print(f"Diablo runs: {diablo_total}")
print(f"Total runs: {total_games + 3300}")