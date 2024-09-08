import turtle

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


def get_coordinates_on_click(x, y):
    print(x, y)


turtle.onscreenclick(get_coordinates_on_click)
turtle.mainloop()

# screen.exitonclick()
