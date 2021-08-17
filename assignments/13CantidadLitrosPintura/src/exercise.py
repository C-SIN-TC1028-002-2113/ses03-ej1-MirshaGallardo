def main():
    #escribe tu código abajo de esta línea
    import math
    a = float(input("Area a pintar en metros: "))
    r = float(input("Rendimiento (m2/l): "))
    l = math.ceil(a/r)
    print("Litros a comprar:",l)



    pass

if __name__ == '__main__':
    main()
