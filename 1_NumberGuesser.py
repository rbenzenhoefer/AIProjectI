import streamlit as st
import random

st.title("Welcome to NumberGuesser! 🎲")

st.header("How should we call you?")
username = ""
username = st.text_input("*be creative*", placeholder="SpaceCowboy462 has a cool sound to it don't you think?")
if username:
    st.success(f"You really want us to call you {username}?     ...okay")
elif username == "":
    st.text("")
else:
    st.info("please enter your username")
st.write("")

if "guesses" not in st.session_state:
    st.session_state.guesses = []

if "total_games" not in st.session_state:
    st.session_state.total_games = 0
if "won_games" not in st.session_state:
    st.session_state.won_games = 0


st.subheader("Choose your difficulty")
st.markdown("*to generate a new number you have to guess the current number or use the button below*")
slider_value = st.slider("", min_value=0, max_value=100, value=50)

# Number game setup
slider_value_int = int(slider_value)
if "stable_right_number" not in st.session_state:
    st.session_state.stable_right_number = random.randint(1, slider_value_int)
#st.write(st.session_state.stable_right_number)

def recalculate():
    global slider_value, slider_value_int
    slider_value_int = int(slider_value)
    st.session_state.stable_right_number = random.randint(1, slider_value_int)
    st.session_state.won_games = st.session_state.won_games + 1


# Add chat input for guessing numbers
if "messages" not in st.session_state:
    st.session_state.messages = []

if st.session_state.messages:
    latest_message = st.session_state.messages[-1]
    st.write(f"{username} guessed {latest_message['content']}")

if "slider_values" not in st.session_state:
    st.session_state.slider_values = []  # Stores slider value for each round
if "guess_counts" not in st.session_state:
    st.session_state.guess_counts = []  # Tracks total guesses for each slider value
if "current_guesses" not in st.session_state:
    st.session_state.current_guesses = 0

user_guess = st.chat_input("Enter your guess")

if user_guess:
    try:
        #guess = int(user_guess)
        #st.session_state.guesses.append(guess)
        #st.session_state.total_games = st.session_state.total_games + 1

        #if guess < st.session_state.stable_right_number:
         #   st.write(f"**Bot**: Your guess of {guess} is too low!")
        #elif guess > st.session_state.stable_right_number:
         #   st.write(f"**Bot**: Your guess of {guess} is too high!")
        #else:
         #   st.write(f"**Bot**: Congratulations! You guessed the right number {st.session_state.stable_right_number}!")
          #  recalculate()

        guess = int(user_guess)
        st.session_state.current_guesses += 1
        st.session_state.guesses.append(guess)
        st.session_state.total_games = st.session_state.total_games + 1

        if guess == st.session_state.stable_right_number:

            st.session_state.slider_values.append(slider_value)
            st.session_state.guess_counts.append(st.session_state.current_guesses)



            st.session_state.current_guesses = 0
            st.write("**Bot**:Correct! New number generated.")
            recalculate()
        elif guess < st.session_state.stable_right_number:
            st.write("**Bot**:Too low! Try again.")
        elif guess > st.session_state.stable_right_number:
            st.write("**Bot**:Too high! Try again.")



    except ValueError:
        st.write("**Bot**: Please enter a valid number.")

if st.button("Regenerate"):
    recalculate()









