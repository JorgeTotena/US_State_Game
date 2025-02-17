# Import required libraries
import pandas  # For data handling (reading CSV)
import turtle  # For GUI and visualization
from turtle import Turtle  # Turtle object for drawing text on the screen

# Set up the game screen
screen = turtle.Screen()
image = "blank_states_img.gif"  # Path to the U.S. map image
screen.addshape(image)  # Register the image as a shape
turtle.shape(image)  # Set the map as the turtle's shape

# Initialize game variables
score = 0  # Track the number of correctly guessed states
game_status = True  # Control the game loop
data = pandas.read_csv("50_states.csv")  # Load state names and coordinates
duplicates = []  # Track guessed states to avoid repeats

# Main game loop
while game_status:
    # Prompt the user for a state name (auto-capitalize input)
    answer_state = turtle.textinput(
        f"{score}/50 states guessed", "What's another state name?"
    ).title()

    if answer_state == "Exit": # break the loop if the user wants it
        # Crear una nueva lista con los estados que no están en duplicates
        all_states = data.state.to_list()
        new_states = []
        for state in all_states:
            if state not in duplicates:
                new_states.append(state)

        print(new_states)
        new_states = pandas.DataFrame(new_states)
        new_states.to_csv("States_to_learn.csv")
        break


    # Check if the guessed state exists in the CSV data
    guessed = data[data["state"] == answer_state]

    # Only proceed if the score is less than 50 (all states not yet guessed)
    if score <= 50:
        if not guessed.empty:  # Check if the guessed state is valid
            if answer_state not in duplicates:  # Prevent duplicate guesses
                # Extract coordinates from the CSV data
                guessed_x = guessed.x.item()  # X-coordinate of the state
                guessed_y = guessed.y.item()  # Y-coordinate of the state

                # Set up a turtle to write the state name on the map
                text_turtle = Turtle()
                text_turtle.hideturtle()  # Hide the turtle cursor
                text_turtle.penup()  # Prevent drawing lines
                text_turtle.goto(guessed_x, guessed_y)  # Move to the state's location
                text_turtle.write(answer_state)  # Write the state name

                score += 1  # Increment the score
                duplicates.append(answer_state)  # Add to guessed states
        else:
            print("False")  # Optional: Indicate incorrect guess (can be removed)
    else:
        game_status = False  # End the loop when all 50 states are guessed

#states to learn csv, generate the list of states that haven't been guessed by the user



"""Angela's solution
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)


"""

screen.exitonclick()