import turtle, pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()

all_states = []

while len(all_states) < 50:

    user_answer = screen.textinput(title=f"{len(all_states)}/50 Guess the state", prompt="Type in the name of the state").title()

    if user_answer in states:
        all_states.append(user_answer)
        # display state name after correct guess
        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        state_data = data[data["state"] == user_answer]
        x_cor = state_data["x"].item()
        y_cor = state_data["y"].item()
        state.goto(x_cor, y_cor)
        state.write(user_answer)


screen.exitonclick()
