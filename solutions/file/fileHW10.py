def file_read_from_head(fname, nlines):
        from itertools import islice
        with open(fname) as f:
                for line in islice(f, nlines):
                        print(line,end='')

if __name__== '__main__':
    file_read_from_head('data/pokemon.csv',10)