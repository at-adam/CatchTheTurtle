import turtle
import time
import datetime
import random
import math

score = 0
# Function to show countdown on turtle screen
def show_countdown(t, timer):
    t.clear()
    t.write(str(timer), align="center", font=("Arial", 27, "normal"))

# Function for countdown timer
def countdown(t):
    total_seconds = 30  # Fixed 30-second game duration
    while total_seconds >= 0:
        timer = datetime.timedelta(seconds=total_seconds)
        show_countdown(t, timer)
        time.sleep(1)
        total_seconds -= 1

def show_score(t, score):
    t.clear()
    t.write(f"Score: {score}", align="center", font=("Arial", 27, "normal"))


def is_clicked(x, y):
    global score
    distance = math.sqrt((x - moving_turtle.xcor())**2 + (y - moving_turtle.ycor())**2)
    if distance < 20:
        score += 1
        show_score(score_turtle, score)

# Initialize the turtle screen
scene = turtle.Screen()
scene.bgcolor("Light Blue")
scene.title("Catch The Turtle")
scene.setup(width=900, height=900)

# Initialize a turtle for showing the countdown
countdown_turtle = turtle.Turtle()
countdown_turtle.hideturtle()
countdown_turtle.penup()
countdown_turtle.goto(0, 400)

score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.goto(0, 450)
show_score(score_turtle, score)


moving_turtle = turtle.Turtle()
moving_turtle.shape("turtle")
moving_turtle.color("black")
moving_turtle.penup()

scene.onscreenclick(is_clicked)

start_time = time.time()
total_seconds = 30  # 30 seconds

while True:
    elapsed_time = time.time() - start_time
    remaining_time = total_seconds - int(elapsed_time)
    timer = datetime.timedelta(seconds=remaining_time)

    if remaining_time >= 0:
        show_countdown(countdown_turtle, timer)
    else:
        break
    moving_turtle.hideturtle()
    x = random.randint(-375, 375)
    y = random.randint(-375, 375)
    moving_turtle.goto(x, y)
    moving_turtle.showturtle()
    time.sleep(0.7)

countdown_turtle.clear()
countdown_turtle.write("Oyun Bitti", align="center", font=("Arial", 30, "normal"))
print("Skorun:", score)

scene.mainloop()