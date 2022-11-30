from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shape("circle")
        self.penup()
        # self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.goto(0, 0)
        self.y = 10
        self.x = 10
        self.spd = 0.1

    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)
        # for i in range(10):
        #     self.setheading(self.y)
        #     self.forward(1)

    def refresh(self):
        self.goto(0, 0)
        self.spd = 0.1
        self.bounce_x()

    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1
        self.spd *= 0.9
