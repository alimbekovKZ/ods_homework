import re
import sys
from tqdm import tqdm

path = 'stackoverflow.10kk.tsv'

in_file = sys.argv[1]
out_file = sys.argv[2]
print(f'in: {in_file}', f'out: {out_file}')

label_tags  = ['javascript', 'java', 'python', 'ruby', 
         'php', 'c++', 'c#', 'go', 'scala', 'swift']

dict_tag = dict(zip(label_tags, range(1, len(label_tags) + 1)))

def to_string_vw(document, label):
    return str(label or '') + ' |text ' + ' '.join(re.findall('\w{3,}', document.lower())) + '\n'

regex_special_char = re.compile('[|]|:')
regex_tags = re.compile('\t(.*)\n')
data_in = open(in_file, mode='r')

if in_file is path:   
    print('ook this is this type of shit   I know.. stackoverflow')
    size_of_file = 10000000
else:    
    #size_of_file = !wc -l ../../data/stackoverflow.10kk.tsv    
    size_of_file = 10000000
    
correct_lines = 0
corrupt_lines = 0
with open(out_file, mode='w') as vw_data:
    for i in tqdm(range(size_of_file)):
        #reading line
        line = data_in.readlines(1)[0]
        #putting tags
        tags_ = regex_tags.search(line).group(1).split()
        tag = [sample_tag for sample_tag in tags_ if sample_tag in label_tags]
        if len(tag) != 1: 
            corrupt_lines+=1 
            continue
        #converting to string
        #cleaning from spec charaacters
        line = regex_special_char.sub('', line)
        line = line[: re.search('\t', line).start()]
        label = dict_tag[tag[0]]
        vw_data.write(to_string_vw(line, label))
        correct_lines +=1
        
print(f'{corrupt_lines} lines was corrupted')
print(f'{correct_lines} lines was fine')