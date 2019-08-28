import yaml
def yml_data_file(file_name):
    with open('./data/'+file_name+'.yml','r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data