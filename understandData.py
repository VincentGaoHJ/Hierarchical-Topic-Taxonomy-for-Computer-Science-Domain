pd = dict()
pd['data_dir'] = './raw_data/'
# pd['index'] = pd['data_dir'] + 'index.txt'
pd['keyword_cnt'] = pd['data_dir'] + 'keyword_cnt.txt'
# pd['keywords'] = pd['data_dir'] + 'keywords.txt'
pd['papers'] = pd['data_dir'] + 'papers.txt'


for key in pd.keys():
    if key == "data_dir":
        continue
    print("\n\n\n")
    print(key)
    fpa = open(pd[key])
    index = 0
    for linea in fpa.readlines():
        index = index + 1
        linea = linea.replace("\n", "")
        print(linea)
        if index == 1000:
            break
    fpa.close()
