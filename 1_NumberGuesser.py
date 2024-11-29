# Import necessary libraries
import streamlit as st
import random

# App title and introductory UI setup
st.title("Welcome to NumberGuesser! 🎲")  # Display the app title
st.header("How should we call you?")  # Prompt for username input
username = ""
username = st.text_input("*be creative*", placeholder="SpaceCowboy462 has a cool sound to it don't you think?")
if username:
    st.success(f"You really want us to call you {username}?     ...okay")  # Acknowledge the username
elif username == "":
    st.text("")  # Handle empty username input gracefully
else:
    st.info("please enter your username")  # Provide a gentle nudge for entering a username
st.write("")

# Initialize session state variables for tracking guesses and game stats
if "guesses" not in st.session_state:
    st.session_state.guesses = []  # Stores all guesses in the current session
if "total_games" not in st.session_state:
    st.session_state.total_games = 0  # Counts total games played
if "won_games" not in st.session_state:
    st.session_state.won_games = 0  # Tracks games won

# Allow user to select difficulty by setting the maximum number
st.subheader("Choose your difficulty")
st.markdown("*to generate a new number you have to guess the current number or use the button below*")
slider_value = st.slider("", min_value=0, max_value=100, value=50)  # Slider to adjust difficulty (max range)

# Generate the target number within the selected difficulty range
slider_value_int = int(slider_value)
if "stable_right_number" not in st.session_state:
    st.session_state.stable_right_number = random.randint(1, slider_value_int)  # Random target number
# st.write(st.session_state.stable_right_number)  # Uncomment for debugging the target number

# Function to recalculate a new target number and update stats
def recalculate():
    global slider_value, slider_value_int
    slider_value_int = int(slider_value)
    st.session_state.stable_right_number = random.randint(1, slider_value_int)  # Generate new target number
    st.session_state.won_games = st.session_state.won_games + 1  # Increment won games count

# Initialize session state variables for additional features
if "messages" not in st.session_state:
    st.session_state.messages = []  # Tracks chat-like feedback for guesses
if st.session_state.messages:
    latest_message = st.session_state.messages[-1]
    st.write(f"{username} guessed {latest_message['content']}")  # Display the last guess made by the user

# Track slider adjustments and guesses count
if "slider_values" not in st.session_state:
    st.session_state.slider_values = []  # Keeps track of slider values for each game
if "guess_counts" not in st.session_state:
    st.session_state.guess_counts = []  # Stores the number of guesses per game
if "current_guesses" not in st.session_state:
    st.session_state.current_guesses = 0  # Tracks guesses in the current round

# Chat input for user guesses
user_guess = st.chat_input("Enter your guess")

if user_guess:
    try:
        guess = int(user_guess)  # Convert input to integer
        st.session_state.current_guesses += 1  # Increment guesses for the current game
        st.session_state.guesses.append(guess)  # Append the guess to session state
        st.session_state.total_games = st.session_state.total_games + 1  # Increment total games counter

        # Check if the user's guess matches the target number
        if guess == st.session_state.stable_right_number:
            st.session_state.slider_values.append(slider_value)  # Save slider value for this game
            st.session_state.guess_counts.append(st.session_state.current_guesses)  # Save number of guesses
            st.session_state.current_guesses = 0  # Reset guess counter for new game
            st.write("**Bot**: Correct! New number generated.")
            recalculate()  # Generate a new target number
        elif guess < st.session_state.stable_right_number:
            st.write("**Bot**: Too low! Try again.")  # Hint for low guess
        elif guess > st.session_state.stable_right_number:
            st.write("**Bot**: Too high! Try again.")  # Hint for high guess

    except ValueError:
        st.write("**Bot**: Please enter a valid number.")  # Handle invalid input gracefully

# Button to regenerate a new number without guessing
if st.button("Regenerate"):
    recalculate()  # Reset and generate a new target number
