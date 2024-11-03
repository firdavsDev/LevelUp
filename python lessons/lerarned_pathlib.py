from pathlib import Path

#bosh oynaning urlini korsatadi
home_dir = Path.home()
print(home_dir)

#terminalda turgan joyingizni urlini korsatadi
cwd = Path.cwd()
print(cwd)

#run bergan file ning urlimi korsatadi
curr_file = Path(__file__)
print(curr_file)

#shu file dan oldingi urlni korsatadi
one_above = cwd.parent
print(one_above)

#shu filedan nechtadir oldin fileni urlini korsatadi
move_above = Path.cwd().parents[0]
print(move_above)

#tanlagan papkani urlini aniqlab beradi
join_path = cwd / 'Geeks'
print(join_path)

#tanlangan narsa papkaligini tekwirib beradi
print(join_path.is_dir())

#tanlangan papkalning ichidagi .py bilan tugediganlarini urllarini aniqlab beradi
target_dir = cwd / 'LevelUp'
for file in target_dir.iterdir():
    if file.suffix == '.py':
        print(file)