with open("data/f3.txt", 'w') as f3:
    with open('data/f1.txt') as fh1, open('data/f2.txt') as fh2:
        for line1, line2 in zip(fh1, fh2):
            # line1 from abc.txt, line2 from test.txtg
            f3.write(line1.strip() + " " + line2.strip() + "\n")