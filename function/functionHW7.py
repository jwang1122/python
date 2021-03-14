def func1(*args):
    print(f"func1{args}")
    for arg in args:
        print(arg)

func1(20, 40, 60)
func1(80, 100)