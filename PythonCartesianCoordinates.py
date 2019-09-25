# ~~ Cartesian Coordinate Points ~~

def give_me_hypothenuse(x1,y1,x2,y2):
    """ returns the distance between two cartesian coordinates """
    import math
    return math.sqrt((x2 - x1)**2 +(y2 - y1)**2)

def main():
    print(give_me_hypothenuse(0,0,3,4))

if __name__ == "__main__":
    main()