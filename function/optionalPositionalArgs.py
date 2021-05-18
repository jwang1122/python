def f1(*args, k1="k1", k2="k2", k3="k3"):
    for i in args:
        print(i, end=' ')
    print(f"{k1}::{k2}::{k3}")

def get_multiple(*keys, dictionary, default=None):
    return [dictionary.get(key, default) for key in keys]

f1(1,"2","3",k1="k1a",k2="k2a",k3="k3a")

fruits = {'lemon': 'yellow', 'orange': 'orange', 'tomato': 'red'}
values = get_multiple('lemon', 'tomato', 'squash', dictionary=fruits, default='unknown')
print(values)