import os
import datetime

langs = ['cs','de_DE','es','es_LAT','fr','it','ja','ko','pl','pt_BR','ru','tw_CN','uk','zh_CN']
timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
output_folder = f'{timestamp}'

os.makedirs(output_folder)

with open('iron_crown.pot', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for lang in langs:
    output = []
    current_msgid = []
    in_msgid = False

    for line in lines:
        if 'Language: \\n' in line:
            line = r'\"Language: ' + lang + r'\n\"' + '\n'
        if line.startswith('msgid '):
            current_msgid = [line.replace('msgid ', '')]
            in_msgid = True
            output.append(line)
        elif line.startswith('msgstr '):
            in_msgid = False
            output.append('msgstr ' + ''.join(current_msgid))
        elif in_msgid and line.startswith('\"'):
            current_msgid.append(line)
            output.append(line)
        else:
            in_msgid = False
            output.append(line)

    file_path = os.path.join(output_folder, f'{lang}.po')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(output)
