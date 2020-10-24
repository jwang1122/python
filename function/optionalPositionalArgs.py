def f1(*args, k1="k1", k2="k2", k3="k3"):
    for i in args:
        print(i, end=' ')
    print(f"{k1}::{k2}::{k3}")

f1(1,"2","3",k1="k1a",k2="k2a",k3="k3a")