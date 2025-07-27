import turtle
import pandas


screen = turtle.Screen()
screen.title("State Guess Game")
screen.setup(776, 850)
image = "map_of_India.gif"
# turtle.addshape(image)
turtle.bgpic(image)
guesed_states = []
data = pandas.read_csv("states_and_uts.csv")

is_game_over = False
state_list = data.state.to_list()

while is_game_over != True:
    Guess = screen.textinput(title=f"{len(guesed_states)} / 36",prompt="Guess the State name ").title()

    if Guess == "Exit":
        missing_state = [state for state in state_list if state not in guesed_states]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("missing_state.csv")
        break
    if Guess in state_list:
        guesed_states.append(Guess)
        t= turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == Guess]
        t.goto(state_data.x.item(),state_data.y.item())
        t.pendown()
        t.write(Guess)
    if len(guesed_states) == 36:
        is_game_over =True

screen.exitonclick()


