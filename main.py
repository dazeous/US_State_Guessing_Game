import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

data = pd.read_csv("50_states.csv")
score = 0
guessed_states = []
is_game_finished = False
while not is_game_finished:
    answer = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another's state name?").title()
    if answer in data.state.values and answer not in guessed_states:
        guessed_states.append(answer)
        x, y = data[data.state==answer].x.item(), data[data.state==answer].y.item()
        pen.goto(x, y)
        pen.write(answer)
        score += 1
    else:
        if answer == "Exit":
            screen.bye()
            print("You exited the game.")
            not_guessed_states = [state for state in data.state.values if state not in guessed_states]
            pd.DataFrame(not_guessed_states).to_csv("states_not_guessed.csv")
        print("Wrong Guess! Try Again.")
    if score == 50:
        is_game_finished = True
screen.bye()
print("Congratulations! You're a true American!")
