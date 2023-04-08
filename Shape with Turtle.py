import turtle

pen = turtle.Pen()
pen.shape("turtle")
N = 3
L = 50

# Inner Degree is id
# Sides of Polygon is N
# Length of sides is L

while N <=13:
    id = (N-2)*180/N
    pen.left(id/2)
    for i in range(N):
        pen.left(180 - id)
        pen.forward(L)

    pen.up()
    pen.right(id/2)
    pen.forward(L/4)
    pen.down()

    N +=1
    L += 8
    

turtle.done()


