import turtle
import winsound

#Main screen
screen = turtle.Screen()
screen.title("pingpong game by SIDDHESH")
screen.bgcolor("green")
screen.setup(width=800, height=600)
screen.tracer(0)

#Player A
player_a = turtle.Turtle()
player_a.speed(0)
player_a.color("white")
player_a.shape("square")
player_a.shapesize(stretch_wid=5, stretch_len=1)
player_a.penup()
player_a.goto(-350,0)

#Player B
player_b = turtle.Turtle()
player_b.speed(0)
player_b.color("white")
player_b.shape("square")
player_b.shapesize(stretch_wid=5, stretch_len=1)
player_b.penup()
player_b.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.color("white")
ball.shape("circle")
ball.penup()
ball.goto(0,0)
ball.dx = 0.35
ball.dy = 0.35

#To make the screen attractive
line = turtle.Turtle()
line.speed(0)
line.color("white")
line.pensize(3)
line.left(90)
line.forward(300)
line.right(180)
line.forward(220)
line.left(90)
line.circle(-80)
line.right(90)
line.forward(380)
line.hideturtle()
line.penup()
line.goto(0,0)

#To move the players
def player_a_up():
    if player_a.ycor() + 50 < 300:
        y = player_a.ycor()
        y += 30
        player_a.sety(y)

def player_a_down():
    if player_a.ycor() - 50 > -300:
        y = player_a.ycor()
        y -= 30
        player_a.sety(y)

def player_b_up():
    if player_b.ycor() + 50 < 300:
        y = player_b.ycor()
        y += 30
        player_b.sety(y)

def player_b_down():
    if player_b.ycor() - 50 > -300:
        y = player_b.ycor()
        y -= 30
        player_b.sety(y)
    
#Giving controls of players on keyboard
screen.listen()
screen.onkeypress(player_a_up, key ="w")
screen.onkeypress(player_a_down, key ="s")
screen.onkeypress(player_b_up, key ="Up")
screen.onkeypress(player_b_down, key ="Down")

#Score
score = turtle.Turtle()
score.speed(0)
score.color("black")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 20, "bold"))

#To end the game
end = turtle.Turtle()
end.speed(0)
end.color("yellow")
end.penup()
end.hideturtle()
end.goto(0,0)

#initial values of points of payers
points_a = 0
points_b = 0

try:
    while True:                
        screen.update()
        
    #to move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

    #To stop the balls from top and bottom border
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            winsound.PlaySound("C:\\Users\\siddhesh\\Desktop\\siddhesh\\python assignment\\PYTHON PROJECT\\bounce.wav", winsound.SND_ASYNC)

        elif ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
            winsound.PlaySound("C:\\Users\\siddhesh\\Desktop\\siddhesh\\python assignment\\PYTHON PROJECT\\bounce.wav", winsound.SND_ASYNC)

    # To stop the from both side border
        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            points_a += 1
            score.clear()
            score.write("Player 1: {}  Player 2: {}".format(points_a, points_b), align="center", font=("Courier", 20, "bold"))
            winsound.PlaySound("C:\\Users\\siddhesh\\Desktop\\siddhesh\\python assignment\\PYTHON PROJECT\\point.wav", winsound.SND_ASYNC)

        elif ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            points_b += 1
            score.clear()
            score.write("Player 1: {}  Player 2: {}".format(points_a, points_b), align="center", font=("Courier", 20, "bold"))
            winsound.PlaySound("C:\\Users\\siddhesh\\Desktop\\siddhesh\\python assignment\\PYTHON PROJECT\\point.wav", winsound.SND_ASYNC)

    # To stop the ball by players
        if (ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < player_b.ycor() + 50) and (ball.ycor() > player_b.ycor() - 50):
            ball.setx(340)
            ball.dx *= -1
            winsound.PlaySound("C:\\Users\\siddhesh\\Desktop\\siddhesh\\python assignment\\PYTHON PROJECT\\bounce.wav", winsound.SND_ASYNC)

        elif (ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < player_a.ycor() + 50) and (ball.ycor() > player_a.ycor() - 50):
            ball.setx(-340)
            ball.dx *= -1
            winsound.PlaySound("C:\\Users\\siddhesh\\Desktop\\siddhesh\\python assignment\\PYTHON PROJECT\\bounce.wav", winsound.SND_ASYNC)
        
        #Auto player
        if player_a.ycor() < ball.ycor():
            player_a_up()

        elif player_a.ycor() > ball.ycor():
            player_a_down()
            
    #To end the game and show the winner
        if points_a > 4:
            end.write("   GAME OVER \n PLAYER 1 WINS!", font=("Elephant", 30, "bold"), align=("center"))
            winsound.PlaySound("C:\\Users\\siddhesh\\Desktop\\siddhesh\\python assignment\\PYTHON PROJECT\\over.wav", winsound.SND_ASYNC)
            break
        
        elif points_b > 4:
            end.write("   GAME OVER \n PLAYER 2 WINS!", font=("Elephant", 30, "bold"), align=("center"))
            winsound.PlaySound("C:\\Users\\siddhesh\\Desktop\\siddhesh\\python assignment\\PYTHON PROJECT\\over.wav", winsound.SND_ASYNC)
            break
        
except:
    print("check the code")

finally:
    turtle.done()
