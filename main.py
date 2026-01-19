import turtle
import pandas

screen = turtle.Screen()
screen.title("Indian States Game")
image = "Map_of_India.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("India_cord.csv")
all_states = data.states.to_list()
guessed_states = []


while len(guessed_states) < 28:
    answer_state = screen.textinput(f"{len(guessed_states)}/28 Correct", prompt="What's another state's name?")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("Missed_States")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.states == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.states.item(), font=("Arial", 12, 'normal'))

screen.exitonclick()
