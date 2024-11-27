import streamlit as st
import random
from Data import countries_all, countries_mid, countries_easy, countries_hard, countries_south_america, countries_oceania, countries_north_america, countries_africa, countries_europe, countries_asia

st.title("Welcome to CountryGuesser! 🌎")

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

if "wrong_guesses" not in st.session_state:
    st.session_state.wrong_guesses = 0

if "number_of_guesses" not in st.session_state:
    st.session_state.number_of_guesses = []

if "level" not in st.session_state:
    st.session_state.level = 0






def recompute():
    st.session_state.random_country_easy = random.choice(countries_easy)
    st.session_state.random_country_mid = random.choice(countries_mid)
    st.session_state.random_country_hard = random.choice(countries_hard)


if "random_country_easy" not in st.session_state:
    st.session_state.random_country_easy = random.choice(countries_easy)
if "random_country_mid" not in st.session_state:
    st.session_state.random_country_mid = random.choice(countries_mid)
if "random_country_hard" not in st.session_state:
    st.session_state.random_country_hard = random.choice(countries_hard)

right_country =  st.session_state.random_country_easy
right_country1 = st.session_state.random_country_mid
right_country2 =st.session_state.random_country_hard

subcol1, subcol2 = st.columns([4,1])
with subcol1:
    st.subheader("Choose your difficulty")
with subcol2:
    st.subheader("Hints: 💡")

col1, col2, col3, space2, hints = st.columns([.6,.755,1,.5,1])
with col1:
    if st.button("Easy 🧑‍🦽‍➡️"):
        st.write(st.session_state.random_country_easy)
        st.session_state.level = "1"
        st.write(f"{st.session_state.level}")
with col2:
    if st.button("Medium 🏃‍➡️"):
        st.write(st.session_state.random_country_mid)
        st.session_state.level = "2"
        st.write(f"{st.session_state.level}")
with col3:
    if st.button("Hard 🏋️‍♀️"):
        st.write(st.session_state.random_country_hard)
        st.session_state.level = "3"
        st.write(f"{st.session_state.level}")
with hints:
    if st.session_state.level == "2" and st.session_state.wrong_guesses > 5:
        if st.session_state.random_country_mid in countries_africa:
            st.write(f"The Country you are searching is in Africa")
        elif st.session_state.random_country_mid in countries_oceania:
            st.write(f"The Country you are searching is in Africa")
        elif st.session_state.random_country_mid in countries_europe:
            st.write(f"The Country you are searching is in Europe")
        elif st.session_state.random_country_mid in countries_asia:
            st.write(f"The Country you are searching is in Asia")
        elif st.session_state.random_country_mid in countries_north_america:
            st.write(f"The Country you are searching is in North America")
        else:
            st.write(f"The Country you are searching is in South America")

        if st.session_state.level == "1" and st.session_state.wrong_guesses > 5:
            if st.session_state.random_country_easy in countries_africa:
                st.write(f"The Country you are searching is in Africa")
            elif st.session_state.random_country_easy in countries_oceania:
                st.write(f"The Country you are searching is in Africa")
            elif st.session_state.random_country_easy in countries_europe:
                st.write(f"The Country you are searching is in Europe")
            elif st.session_state.random_country_easy in countries_asia:
                st.write(f"The Country you are searching is in Asia")
            elif st.session_state.random_country_easy in countries_north_america:
                st.write(f"The Country you are searching is in North America")
            else:
                st.write(f"The Country you are searching is in South America")

        if st.session_state.level == "3" and st.session_state.wrong_guesses > 5:
            if st.session_state.random_country_hard in countries_africa:
                st.write(f"The Country you are searching is in Africa")
            elif st.session_state.random_country_hard in countries_oceania:
                st.write(f"The Country you are searching is in Africa")
            elif st.session_state.random_country_hard in countries_europe:
                st.write(f"The Country you are searching is in Europe")
            elif st.session_state.random_country_hard in countries_asia:
                st.write(f"The Country you are searching is in Asia")
            elif st.session_state.random_country_hard in countries_north_america:
                st.write(f"The Country you are searching is in North America")
            else:
                st.write(f"The Country you are searching is in South America")




# Add chat input for guessing numbers
if "messages" not in st.session_state:
    st.session_state.messages = []

if st.session_state.messages:
    latest_message = st.session_state.messages[-1]
    st.write(f"{username} guessed {latest_message['content']}")



user_guess = st.chat_input("Enter your guess")

if user_guess:
    try:
        if st.session_state.level == "1":
            if user_guess in countries_all:
                st.write(f"{user_guess}")
                st.write(f"{right_country}")
                #st.session_state.guesses_count.append(user_guess)
                if user_guess in countries_mid:
                    st.write("too hard")
                    st.session_state.wrong_guesses = st.session_state.wrong_guesses + 1
                elif user_guess in countries_hard:
                    st.write("too hard")
                    st.session_state.wrong_guesses = st.session_state.wrong_guesses + 1
                elif user_guess == st.session_state.random_country_easy:
                    st.write("correct")
                    st.write(f"correct and it only took {st.session_state.wrong_guesses} wrong guess(es)")
                    st.session_state.wrong_guesses = 0
                    recompute()
                else:
                    st.write("no correct")
                    st.session_state.wrong_guesses = st.session_state.wrong_guesses + 1

            else:
                st.write("smtwrong")

        elif st.session_state.level == "2":
            if user_guess in countries_all:
                st.write(f"{user_guess}")
                st.write(f"{right_country1}")
                #st.session_state.guesses_count.append(user_guess)
                if user_guess in countries_easy:
                    st.write("too easy")
                    st.session_state.wrong_guesses = st.session_state.wrong_guesses + 1
                elif user_guess in countries_hard:
                    st.write("too hard")
                    st.session_state.wrong_guesses = st.session_state.wrong_guesses + 1
                elif user_guess == st.session_state.random_country_mid:
                    st.write(f"correct and it only took {st.session_state.wrong_guesses} wrong guess(es)")
                    st.session_state.wrong_guesses = 0
                    recompute()
                else:
                    st.write("no correct")
                    st.session_state.wrong_guesses = st.session_state.wrong_guesses + 1
            else:
                st.write("smtwrong")
        elif st.session_state.level == "3":
            if user_guess in countries_all:
                st.write(f"{user_guess}")
                st.write(f"{right_country2}")
                #st.session_state.guesses_count.append(user_guess)
                if user_guess in countries_mid:
                    st.write("too easy")
                    st.session_state.wrong_guesses = st.session_state.wrong_guesses + 1
                elif user_guess in countries_easy:
                    st.write("too easy")
                    st.session_state.wrong_guesses = st.session_state.wrong_guesses + 1
                elif user_guess == st.session_state.random_country_hard:
                    st.write("correct")
                    st.write(f"correct and it only took {st.session_state.wrong_guesses} wrong guess(es)")
                    st.session_state.wrong_guesses = 0
                    recompute()
                else:
                    st.write("no correct")
                    st.session_state.wrong_guesses = st.session_state.wrong_guesses + 1
            else:
                st.write("smtwrong")
        else:
            st.write("please select a difficulty")


    except ValueError:
        st.write("**Bot**: Please enter a valid number.")
else:
    st.write("smotwrong")