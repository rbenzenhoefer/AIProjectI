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

st.subheader("Choose your difficulty")
slider_value = st.slider("", min_value=0, max_value=100, value=50)

# Number game setup
slider_value_int = int(slider_value)
if "stable_right_number" not in st.session_state:
    st.session_state.stable_right_number = random.randint(0, slider_value_int)
st.write(st.session_state.stable_right_number)

def recalculate():
    global slider_value, slider_value_int
    slider_value_int = int(slider_value)
    st.session_state.stable_right_number = random.randint(0, slider_value_int)


# Add chat input for guessing numbers
if "messages" not in st.session_state:
    st.session_state.messages = []

if st.session_state.messages:
    latest_message = st.session_state.messages[-1]
    st.write(f"{username} guessed {latest_message['content']}")



user_guess = st.chat_input("Enter your guess")

if user_guess:
    try:
        guess = int(user_guess)
        st.session_state.guesses.append(guess)

        if guess < st.session_state.stable_right_number:
            st.write(f"**Bot**: Your guess of {guess} is too low!")
        elif guess > st.session_state.stable_right_number:
            st.write(f"**Bot**: Your guess of {guess} is too high!")
        else:
            st.write(f"**Bot**: Congratulations! You guessed the right number {st.session_state.stable_right_number}!")
            recalculate()

    except ValueError:
        st.write("**Bot**: Please enter a valid number.")


#st.write(st.session_state.guesses)







