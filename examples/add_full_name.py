import pandas

def add_full_name(path_to_csv, path_to_new_csv):
    df = pandas.read_csv(path_to_csv)
    
    df['nameFull']=df['nameFirst'] + ' ' + df['nameLast']
    df.to_csv(path_to_new_csv)

if __name__ == '__main__':
   add_full_name('../data/Master.csv', '../data/Master_new.csv')
