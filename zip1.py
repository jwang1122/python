def test():
    name = ("Berlin", "Cairo", "Buenos Aires", "Los Angeles", "Tokyo",
            "New York", "London", "Beijing")
    temperature = (29, 36, 19, 26, 27, 28, 22, 32)

    atitude = (1.2, 4.5, 6.4, 1.1, 4.8, 8.4, 3.9, 2.1)
    x = list(zip(name, temperature))
    print(x)

    x = tuple(zip(name, temperature))
    print(x)

    cities = list(zip(name, temperature, atitude))
    print(cities)


test()