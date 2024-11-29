import streamlit as st
from Data import countries_all, countries_mid, countries_easy, countries_hard, countries_south_america, countries_oceania, countries_north_america, countries_africa, countries_europe, countries_asia



st.title("Developer Information")

    # Course and team members information
st.header("AI and the Web - Homework 1: GuessingGame")
st.write("Professor: Tobias Thelen")
st.write("Team Members:")
st.write("- Raphael")
st.write("- Mohit")
st.write("- Martin")

    # Project Description
st.subheader("Project Description")
st.write("In this project, we are developing a country guessing game.")



st.subheader("Country lists for CountryGuesser:")
st.markdown(f"**Easy**: {countries_easy}")
st.markdown(f"**Medium**: {countries_mid}")
st.markdown(f"**Hard**: {countries_hard}")
