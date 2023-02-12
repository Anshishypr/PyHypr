# -------------------------------------------------- Mensuration -------------------------------------------------- #

class Maths:
    def info(self):
        print('''
        What Do You Want To Do ? 

            1. Area
            2. Volume
            3. Perimeter / Circumference
            4. Total Surface Area
            5. Lateral Surface Area
    ''')
    def task(self):
        user = int(input("Enter Selection -> "))
        match(user):
            case 1:
                fig1 = str(input("Figure -> "))
                Area(fig1)
            case 2:
                fig2 = str(input("Figure -> "))
                Volume(fig2)
            case 3:
                fig3 = str(input("Figure -> "))
                Perimeter(fig3)
            case 4:
                fig4 = str(input("Figure -> "))
                TSA(fig4)
            case 5:
                fig5 = str(input("Figure -> "))
                LSA(fig5)
            case _:
                print("Not Valid.")
                self.task()

class Area:
    def __init__(self, figureA):
        self.fig = figureA
        match(self.fig):
            case "Rectangle":
                len = float(input("Lenght -> "))
                wid = float(input("Breadth -> "))
                measure = str(input("Unit -> "))
                self.rectangle(len, wid, measure)
            case "Square":
                side = float(input("Side -> "))
                measure = str(input("Unit -> "))
                self.square(side, measure)
            case "Circle":
                radii = float(input("Radius -> "))
                measure = str(input("Unit -> "))
                self.circle(radii, measure)
            case "Triangle":
                base = float(input("Base -> "))
                height = float(input("Height -> "))
                measure = str(input("Unit -> "))
                self.triangle(base, height, measure)
            case _:
                print("Invalid Figure.")
                math.task()

    def rectangle(self, l, b, u):
        area = l * b
        print(f"Area = {area} {u}²\n")

    def square(self, s, u):
        area = s * s
        print(f"Area = {area} {u}²\n")
        math.task()

    def circle(self, r, u):
        area = 22/7 * r * r
        print(f"Area = {area} {u}²\n")
        math.task()

    def triangle(self, b, h, u):
        area = 1/2 * b * h
        print(f"Area = {area} {u}²\n")
        math.task()

class Volume:
    def __init__(self, figureV):
        self.fig = figureV
        match(self.fig):
            case "Cuboid":
                len = float(input("Lenght -> "))
                wid = float(input("Breadth -> "))
                hei = float(input("Height -> "))
                measure = str(input("Unit -> "))
                self.cuboid(len, wid, hei, measure)
            case "Cube":
                side = float(input("Side -> "))
                measure = str(input("Unit -> "))
                self.cube(side, measure)
            case "Cylinder":
                radii = float(input("Radius -> "))
                hei = float(input("Height -> "))
                measure = str(input("Unit -> "))
                self.cylinder(radii, hei, measure)
            case "Sphere":
                radii = float(input("Radius -> "))
                measure = str(input("Unit -> "))
                self.sphere(radii, measure)

    def cuboid(self, l, b, h, u):
        volume = l * b * h
        print(f"Volume = {volume} {u}³\n")
        math.task()
    
    def cube(self, s, u):
        volume = s * s * s
        print(f"Volume = {volume} {u}³\n")
        math.task()

    def cylinder(self, r, h, u):
        volume = 22/7 * r * r * h
        print(f"Volume = {volume} {u}³\n")
        math.task()
    
    def sphere(self, r, u):
        volume = 4/3 * 22/7 * r * r * r
        print(f"Volume = {volume} {u}³\n")
        math.task()

class Perimeter:
    def __init__(self, figureP):
        self.fig = figureP
        match(self.fig):
            case "Rectangle":
                len = float(input("Lenght -> "))
                wid = float(input("Breadth -> "))
                measure = str(input("Unit -> "))
                self.rectangle(len, wid, measure)
            case "Square":
                side = float(input("Side -> "))
                measure = str(input("Unit -> "))
                self.square(side, measure)
            case "Circle":
                radii = float(input("Radius -> "))
                measure = str(input("Unit -> "))
                self.circle(radii, measure)
            case "Triangle":
                a = float(input("Side (a) -> "))
                b = float(input("Side (b) -> "))
                c = float(input("Side (c) -> "))
                measure = str(input("Unit -> "))
                self.triangle(a, b, c)
            case _:
                print("Invalid Figure.\n")
                math.task()

    def rectangle(self, l, b, u):
        peri = 2 * (l + b)
        print(f"Perimeter = {peri} {u}\n")

    def square(self, s, u):
        peri = s * 4
        print(f"Perimeter = {peri} {u}\n")
        math.task()

    def circle(self, r, u):
        peri = 2 * 22/7 * r
        print(f"Perimeter = {peri} {u}\n")
        math.task()

    def triangle(self, a, b, c, u):
        peri = a + b + c
        print(f"Perimeter = {peri} {u}\n")
        math.task()

class TSA:
    def __init__(self, figureTSA):
        self.fig = figureTSA
        match(self.fig):
            case "Cuboid":
                len = float(input("Lenght -> "))
                wid = float(input("Breadth -> "))
                hei = float(input("Height -> "))
                measure = str(input("Unit -> "))
                self.cuboid(len, wid, hei, measure)
            case "Cube":
                side = float(input("Side -> "))
                measure = str(input("Unit -> "))
                self.cube(side, measure)
            case "Cylinder":
                radii = float(input("Radius -> "))
                hei = float(input("Height -> "))
                measure = str(input("Unit -> "))
                self.cylinder(radii, hei, measure)
            case "Sphere":
                radii = float(input("Radius -> "))
                measure = str(input("Unit -> "))
                self.sphere(radii, measure)

    def cuboid(self, l, b, h, u):
        tsa = 2 * ((l * b) + (b * h) + (h * l))
        print(f"TSA = {tsa} {u}²\n")
        math.task()

    def cube(self, a, u):
        tsa = 6 * a * a
        print(f"TSA = {tsa} {u}²\n")
        math.task()

    def cylinder(self, r, h, u):
        tsa = 2 * 22/7 * r * (r + h)
        print(f"TSA = {tsa} {u}²\n")
        math.task()

    def sphere(self, r, u):
        tsa = 4 * 22/7 * r * r
        print(f"TSA = {tsa} {u}²\n")
        math.task()

class LSA:
    def __init__(self, figureLSA):
        self.fig = figureLSA
        match(self.fig):
            case "Cuboid":
                len = float(input("Lenght -> "))
                wid = float(input("Breadth -> "))
                hei = float(input("Height -> "))
                measure = str(input("Unit -> "))
                self.cuboid(len, wid, hei, measure)
            case "Cube":
                side = float(input("Side -> "))
                measure = str(input("Unit -> "))
                self.cube(side, measure)
            case "Cylinder":
                radii = float(input("Radius -> "))
                hei = float(input("Height -> "))
                measure = str(input("Unit -> "))
                self.cylinder(radii, hei, measure)
            case "Sphere":
                radii = float(input("Radius -> "))
                measure = str(input("Unit -> "))
                self.sphere(radii, measure)

    def cuboid(self, l, b, h, u):
        lsa = 2 * h * (l + b)
        print(f"TSA = {lsa} {u}²\n")
        math.task()

    def cube(self, a, u):
        lsa = 4 * a * a
        print(f"TSA = {lsa} {u}²\n")
        math.task()

    def cylinder(self, r, h, u):
        lsa = 2 * 22/7 * r * h
        print(f"TSA = {lsa} {u}²\n")
        math.task()
    
    def sphere(self, r, u):
        lsa = 4 * 22/7 * r * 2
        print(f"TSA = {lsa} {u}²\n")
        math.task()

math = Maths()
math.info()
math.task()