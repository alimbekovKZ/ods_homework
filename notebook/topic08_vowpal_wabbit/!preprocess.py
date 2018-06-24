import sys
import numpy as np
from tqdm import tqdm

file_in_name = sys.argv[-2]
file_out_name = sys.argv[-1]

tags = ['javascript', 'java', 'python', 'ruby',\
        'php', 'c++', 'c#', 'go', 'scala', 'swift']

tags_target = dict(zip(tags, range(1, 11)))

file_out = open(file_out_name, 'w')

with open(file_in_name, 'r') as file_in:
    for line in tqdm(file_in, total=10_000_000):
        spl = line.strip().split('\t')
        if len(spl) != 2:
            continue
        cur_tags = np.array(spl[1].split())
        find_tags = cur_tags[np.argwhere([tag in tags for tag in cur_tags])]
        # print(cur_tags, find_tags)
        if len(find_tags) != 1:
            continue
        file_out.write('{} | {}\n'.format(
            tags_target[find_tags[0][0]],
            spl[0].replace('|', '').replace(':', '')
        ))

file_out.close()
