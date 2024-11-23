import streamlit as st
import math
import random

def user_guessing_game():
    st.write("### User Guessing Game")
    number_to_guess = st.session_state["number_to_guess"]
    
    guess = st.number_input("Guess the number (1-100):", min_value=1, max_value=100, step=1)
    
    if st.button("Check"):
        if guess < number_to_guess:
            st.write("**Too Low! Try Again.**")
        elif guess > number_to_guess:
            st.write("**Too High! Try Again.**")
        else:
            st.write(f"**Congratulations! You guessed it! The number was {number_to_guess}.**")

def machine_guessing_game():
    st.write("### Machine Guessing Game")
    if "low" not in st.session_state:
        st.session_state["low"] = 1
    if "high" not in st.session_state:
        st.session_state["high"] = 100
    
    if st.button("Start Machine Guessing"):
        st.session_state["guess"] = (st.session_state["low"] + st.session_state["high"]) // 2
        st.write(f"Machine guesses: {st.session_state['guess']}")

    if "guess" in st.session_state:
        if st.button("Higher"):
            st.session_state["low"] = st.session_state["guess"] + 1
            st.session_state["guess"] = (st.session_state["low"] + st.session_state["high"]) // 2
        elif st.button("Lower"):
            st.session_state["high"] = st.session_state["guess"] - 1
            st.session_state["guess"] = (st.session_state["low"] + st.session_state["high"]) // 2
        elif st.button("Correct"):
            st.write(f"**Machine guessed it! The number was {st.session_state['guess']}**")
            return

        st.write(f"Machine guesses: {st.session_state['guess']}")

def calculate_optimal_guesses():
    st.write("### Optimal Number of Guesses")
    optimal_guesses = math.ceil(math.log2(100))  # Log base 2 of range 1-100
    st.write(f"The optimal number of guesses for the range 1-100 is: **{optimal_guesses}**")

def main():
    st.title("Number Guessing Game")
    mode = st.sidebar.selectbox("Choose Mode", ["User Guesses", "Machine Guesses"])
    
    if "number_to_guess" not in st.session_state:
        st.session_state["number_to_guess"] = random.randint(1, 100)
    
    if mode == "User Guesses":
        user_guessing_game()
    elif mode == "Machine Guesses":
        machine_guessing_game()

    calculate_optimal_guesses()

if __name__ == "__main__":
    main()
