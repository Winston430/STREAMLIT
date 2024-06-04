import streamlit as st

def main():
    st.title("Voting Eligibility Checker")
    st.write("Please enter your details to check if you are eligible to vote.")
    
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age", min_value=0, max_value=150)
    country = st.text_input("Enter your country")
    city = st.text_input("Enter your city")
    nida = st.text_input("Enter your NIDA number")

    if st.button("Check Eligibility"):
        if age >= 18 and validate_nida(nida) and validate_unique_nida(nida) and country == Tanzania:
            st.success(f"Hello {name}, you are eligible to vote!")
        else:
            st.error(f"Sorry {name}, you are not eligible to vote yet.") 

def validate_nida(nida):
    # Perform NIDA validation here, for example, you can check length, format, etc.
    # Return True if NIDA is valid, False otherwise
    return True

def validate_unique_nida(nida):
    # Check if the provided NIDA is unique in your database or dataset
    # Return True if unique, False otherwise
    return True

if __name__ == "__main__":
    main()
