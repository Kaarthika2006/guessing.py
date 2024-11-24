import streamlit as st

def calculate_square(number):
    return number**2

def calculate_cube(number):
    return number**3

def calculate_square_root(number):
    return number ** 0.5

st.title("Square and Cube Calculator")
st.write("Enter a number and choose an operation to calculate its square or cube.")

number = st.number_input("Enter a number:")

operation = st.radio("Choose an operation:", ("Square", "Cube","Square Root","Exist"))

if st.button("Calculate"):
    if operation == "Square":
        result = calculate_square(number)
        st.success(f"The square of {number} is {result}.")
    elif operation == "Cube":
        result = calculate_cube(number)
        st.success(f"The cube of {number} is {result}.")
    elif operation == "Square Root":
        if number >= 0:
            result = calculate_square_root(number)
            st.success(f"The square root of {number} is {result}.")
        else:
            st.error("Square root of a negative number is undefined.")
    elif operation == "Exist":
        st.title("**Program Ended**")
        st.stop()        
