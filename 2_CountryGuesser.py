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

if "all_easy" not in st.session_state:
    st.session_state.all_easy = 0
if "guesses_easy" not in st.session_state:
    st.session_state.guesses_easy = 0

if "all_mid" not in st.session_state:
    st.session_state.all_mid = 0
if "guesses_mid" not in st.session_state:
    st.session_state.guesses_mid = 0

if "all_hard" not in st.session_state:
    st.session_state.all_hard = 0
if "guesses_hard" not in st.session_state:
    st.session_state.guesses_hard = 0

if "level" not in st.session_state:
    st.session_state.level = 0


# total guesses
if "total_guesses" not in st.session_state:
    st.session_state.total_guesses = 0
# correct guesses
if "right_guesses" not in st.session_state:
    st.session_state.right_guesses = 0
# score mechanic
if "score" not in st.session_state:
    st.session_state.score = 1566
if "highscore" not in st.session_state:
    st.session_state.highscore = 0
if "gewinner" not in st.session_state:
    st.session_state.gewinner = ""
if "average_score" not in st.session_state:
    st.session_state.average_score = 0
if "total_score" not in st.session_state:
    st.session_state.total_score = 0




def find_average_score():
    try:
        st.session_state.average_score = st.session_state.total_score / st.session_state.right_guesses
    except:
        st.session_state.average_score = st.session_state.total_score

def checkhighscore():
    global gewinner, total_score
    st.session_state.total_score = st.session_state.total_score + st.session_state.score
    if st.session_state.score > st.session_state.highscore:
        st.session_state.highscore = st.session_state.score
        st.session_state.gewinner = username
    else:
        st.session_state.highscore = st.session_state.highscore



def recompute():
    st.session_state.random_country_easy = random.choice(countries_easy)
    st.session_state.random_country_mid = random.choice(countries_mid)
    st.session_state.random_country_hard = random.choice(countries_hard)
    st.session_state.right_guesses = st.session_state.right_guesses + 1
    st.session_state.score = 1566
    find_average_score()



if "random_country_easy" not in st.session_state:
    st.session_state.random_country_easy = random.choice(countries_easy)
if "random_country_mid" not in st.session_state:
    st.session_state.random_country_mid = random.choice(countries_mid)
if "random_country_hard" not in st.session_state:
    st.session_state.random_country_hard = random.choice(countries_hard)

right_country = st.session_state.random_country_easy
right_country1 = st.session_state.random_country_mid
right_country2 = st.session_state.random_country_hard

subcol1, subcol2 = st.columns([4,1])
with subcol1:
    st.subheader("Choose your difficulty")
with subcol2:
    st.subheader("Hints: 💡")

col1, col2, col3, space2, hints = st.columns([.6,.755,1,.5,1])
with col1:
    if st.button("Easy 🧑‍🦽‍➡️"):
        st.session_state.wrong_guesses = 0
        st.write(st.session_state.random_country_easy)
        st.session_state.level = "1"
        #st.write(f"{st.session_state.level}")
with col2:
    if st.button("Medium 🏃‍➡️"):
        st.session_state.wrong_guesses = 0
        #st.write(st.session_state.random_country_mid)
        st.session_state.level = "2"
        #st.write(f"{st.session_state.level}")
with col3:
    if st.button("Hard 🏋️‍♀️"):
        st.session_state.wrong_guesses = 0
        #st.write(st.session_state.random_country_hard)
        st.session_state.level = "3"
        #st.write(f"{st.session_state.level}")
with hints:
    if st.session_state.level == "2" and st.session_state.wrong_guesses > 5:
        if st.session_state.random_country_mid in countries_africa:
            st.write(f"The Country you are searching is in Africa")
        elif st.session_state.random_country_mid in countries_oceania:
            st.write(f"The Country you are searching is in Oceania")
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
            st.write(f"The Country you are searching is in Oceania")
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
            st.write(f"The Country you are searching is in Oceania")
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
                #st.write(f"{right_country}")
                #st.write(f"{st.session_state.wrong_guesses}")
                st.session_state.total_guesses = st.session_state.total_guesses + 1
                st.session_state.all_easy = st.session_state.all_easy + 1
                if user_guess in countries_mid:
                    st.write("too hard")
                    st.session_state.wrong_guesses = st.session_state.wrong_guesses + 1
                    st.session_state.score = st.session_state.score - 3
                   #st.write(f"{username}'s Score: {st.session_state.score}")
                elif user_guess in countries_hard:
                    st.write("too hard")
                    st.session_state.wrong_guesses = st.session_state.wrong_guesses + 1
                    st.session_state.score = st.session_state.score - 3
                    #st.write(f"{username}'s Score: {st.session_state.score}")
                elif user_guess == st.session_state.random_country_easy:
                    #st.write("correct")
                    st.write(f"correct and it only took {st.session_state.wrong_guesses} wrong guess(es)")
                    st.session_state.wrong_guesses = 0
                    st.session_state.score = st.session_state.score * 1.3
                    st.session_state.guesses_easy = st.session_state.guesses_easy + 1
                    st.write(f"{username}'s Score: {st.session_state.score:.0f}")
                    checkhighscore()
                    recompute()
                else:
                    st.write("no correct")
                    st.session_state.wrong_guesses = st.session_state.wrong_guesses + 1
                    st.session_state.score = st.session_state.score - 3
                    #st.write(f"{username}'s Score: {st.session_state.score:.0f}")

            else:
                st.write("Please guess a Country")
                #st.write(f"{username}'s Score: {st.session_state.score}")

        elif st.session_state.level == "2":
            if user_guess in countries_all:
                st.write(f"{user_guess}")
                #st.write(f"{right_country1}")
                st.session_state.total_guesses = st.session_state.total_guesses + 1
                st.session_state.all_mid = st.session_state.all_mid + 1
                if user_guess in countries_easy:
                    st.write("too easy")
                    st.session_state.wrong_guesses = st.session_state.wrong_guesses + 1
                    st.session_state.score = int(st.session_state.score) - 3
                elif user_guess in countries_hard:
                    st.write("too hard")
                    st.session_state.wrong_guesses = st.session_state.wrong_guesses + 1
                    st.session_state.score = int(st.session_state.score) - 3
                elif user_guess == st.session_state.random_country_mid:
                    st.write(f"correct and it only took {st.session_state.wrong_guesses} wrong guess(es)")
                    st.session_state.wrong_guesses = 0
                    st.session_state.score = int(st.session_state.score) * 1.4
                    st.session_state.guesses_mid = st.session_state.guesses_mid + 1
                    st.write(f"{username}'s Score: {st.session_state.score:.0f}")
                    checkhighscore()
                    recompute()
                else:
                    st.write("no correct")
                    st.session_state.wrong_guesses = st.session_state.wrong_guesses + 1
                    st.session_state.score = int(st.session_state.score) - 3
            else:
                st.write("Please guess a Country")

        elif st.session_state.level == "3":
            if user_guess in countries_all:
                st.write(f"{user_guess}")
                #st.write(f"{right_country2}")
                st.session_state.total_guesses = st.session_state.total_guesses + 1
                st.session_state.all_hard = st.session_state.all_hard + 1
                if user_guess in countries_mid:
                    st.write("too easy")
                    st.session_state.wrong_guesses = st.session_state.wrong_guesses + 1
                    st.session_state.score = int(st.session_state.score) - 3
                elif user_guess in countries_easy:
                    st.write("too easy")
                    st.session_state.wrong_guesses = st.session_state.wrong_guesses + 1
                    st.session_state.score = int(st.session_state.score) - 3
                elif user_guess == st.session_state.random_country_hard:
                    #st.write("correct")
                    st.write(f"correct and it only took {st.session_state.wrong_guesses} wrong guess(es)")
                    st.session_state.wrong_guesses = 0
                    st.session_state.score = int(st.session_state.score) * 1.6
                    st.session_state.guesses_hard = st.session_state.guesses_hard + 1
                    st.write(f"{username}'s Score: {st.session_state.score:.0f}")
                    checkhighscore()
                    recompute()
                else:
                    st.write("no correct")
                    st.session_state.wrong_guesses = st.session_state.wrong_guesses + 1
                    st.session_state.score = int(st.session_state.score) - 3
            else:
                st.write("Please guess a Country")
        else:
            st.write("please select a difficulty")


    except ValueError:
        st.write("**Bot**: Please enter a valid number.")
else:
    st.write("")

#st.write(f"{st.session_state.highscore:.0f}")
#st.write(f"{st.session_state.gewinner}")
#st.write(f"{st.session_state.total_score:.0f}")
#st.write(f"{st.session_state.average_score:.0f}")
#st.write(f"{st.session_state.right_guesses}")
#st.write(f"{st.session_state.wrong_guesses}")
