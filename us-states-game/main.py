import turtle, pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()

all_states_guessed = False

while not all_states_guessed:

    user_answer = screen.textinput(title="Guess the state", prompt="Type in the name of the state").title()

    if user_answer in states:
        state_data = data[data["state"] == user_answer]
        x_cor = int(state_data["x"])
        y_cor = int(state_data["y"])

        # display state name after correct guess
        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        state.goto(x_cor, y_cor)
        state.write(user_answer, font=("Arial", 8, "normal"))

        # remove state after correct guess
        states.remove(user_answer)
