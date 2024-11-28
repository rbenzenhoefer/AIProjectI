import streamlit as st
import pandas as pd
from collections import Counter

# Page Title
st.title("Your Statistics! 📊")

# Tabs for each game
tab1, tab2 = st.tabs(["🌎 Country Guesser", "🎲 Number Guesser"])


if "average_score" not in st.session_state:
    st.session_state.average_score = 0
if "total_guesses" not in st.session_state:
    st.session_state.total_guesses = 0
if "right_guesses" not in st.session_state:
    st.session_state.right_guesses = 0
if "gewinner" not in st.session_state:
    st.session_state.gewinner = ""
if "highscore" not in st.session_state:
    st.session_state.highscore = 0
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

# average guesses
try:
    st.session_state.average_guesses = st.session_state.total_guesses / st.session_state.right_guesses
except:
    st.session_state.average_guesses = st.session_state.total_guesses

try:
    st.session_state.average_easy = st.session_state.all_easy / st.session_state.guesses_easy
except:
    st.session_state.average_easy = st.session_state.guesses_easy


try:
    st.session_state.average_mid = st.session_state.guesses_mid / st.session_state.all_mid
except:
    st.session_state.average_mid = st.session_state.guesses_mid

try:
    st.session_state.average_hard = st.session_state.guesses_hard / st.session_state.all_hard
except:
    st.session_state.average_hard = st.session_state.guesses_hard

# Statistics for Country Guesser
with tab1:
    st.header("🌎 Country Guesser Statistics")
    col11, col22, col33 = st.columns(3)
    with col22:
        st.markdown("---")
        st.markdown(
            f"### <div style='text-align: center;'> 🏆 Highscore: {st.session_state.highscore:.0f} *by {st.session_state.gewinner}</div>*",
            unsafe_allow_html =True)
        st.markdown("---")

    # Placeholder for metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Total Guesses", value=f"{st.session_state.total_guesses}")
    with col2:
        st.metric(label="Correct Guesses", value=f"{st.session_state.right_guesses}")
    with col3:
        st.metric(label="Average Guesses per Game", value=f"{st.session_state.average_guesses:.1f}")
    with col4:
        st.metric(label="Average Score", value=f"{st.session_state.average_score:.0f}")


# Additional Charts/Details
    st.subheader("Detailed Statistics")
    st.write("Average Guesses needed")
    categories = ["Easy", "Medium", "Hard"]
    values = [st.session_state.average_easy, st.session_state.average_mid, st.session_state.average_hard]
    data = pd.DataFrame({"Category": pd.Categorical(categories, categories=categories, ordered=True), "Value": values})
    st.bar_chart(data.set_index("Category"))

#st.write(f"{st.session_state.average_easy}")
#st.write(f"{st.session_state.guesses_easy}")
#st.write(f"{st.session_state.all_easy}")
    st.markdown("---")
    st.write("How we estimate your Guess:")


# Statistics for Number Guesser
if "guesses" not in st.session_state:
    st.session_state.guesses = []
if "favourite_number" not in st.session_state:
    favourite_number = 0

counter = Counter(st.session_state.guesses)
try:
    favourite_number, count = counter.most_common(1)[0]
except:
    st.write("")
if "total_games" not in st.session_state:
    st.session_state.total_games = 0
if "won_games" not in st.session_state:
    st.session_state.won_games = 0
try:
    st.session_state.average_rounds = st.session_state.total_games / st.session_state.won_games
except:
    st.session_state.average_rounds = st.session_state.total_games

with tab2:
    st.header("🎲 Number Guesser Statistics")
    col11, col22, col33 = st.columns(3)
    with col22:
        st.markdown("---")
        st.markdown(
            f"### <div style='text-align: center;'> Your favourite number: <br><br> <span style='font-size: 50px;'>{favourite_number}</span></div>",
            unsafe_allow_html=True)
        st.markdown("---")


    # Placeholder for metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Total Guesses", value=f"{st.session_state.total_games}")
    with col2:
        st.metric(label="Correct Guesses", value=f"{st.session_state.won_games}")
    with col3:
        st.metric(label="Average Guesses per Number", value=f"{st.session_state.average_rounds:.1f}")

    # Additional Charts/Details
    st.subheader("Detailed Statistics")



    # Ensure necessary session variables exist
    if "slider_values" not in st.session_state:
        st.session_state.slider_values = []  # List to store slider values for each round
    if "guess_counts" not in st.session_state:
        st.session_state.guess_counts = []  # List to store the number of guesses for each round

    # Assuming slider_values and guess_counts are updated in your existing game logic
    # Compute the average number of guesses per slider value
    if st.session_state.slider_values and st.session_state.guess_counts:
        data = pd.DataFrame({
            "Slider Value": st.session_state.slider_values,
            "Guesses": st.session_state.guess_counts
        })
        average_guesses = data.groupby("Slider Value")["Guesses"].mean().reset_index()

        # Create and display the line chart
        st.title("Average Number of Guesses vs. Slider Value")
        st.line_chart(average_guesses.set_index("Slider Value"))
    else:
        st.write("Play the game to see the chart!")

#reset statistics