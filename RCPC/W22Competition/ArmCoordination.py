def questionC():
    coordinate = input().split()
    radius = int(input())

    xValue = int(coordinate[0])
    yValue = int(coordinate[1])

    print("{} {}".format(xValue+radius, yValue+radius))
    print("{} {}".format(xValue+radius, yValue-radius))
    print("{} {}".format(xValue-radius, yValue-radius))
    print("{} {}".format(xValue-radius, yValue+radius))


questionC()