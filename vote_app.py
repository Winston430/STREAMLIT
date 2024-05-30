import streamlit as st

def main():
    st.title("Voting Eligibility Checker")
    st.write("Please enter your details to check if you are eligible to vote.")
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age", min_value=0, max_value=150)
    if st.button("Check Eligibility"):
        if age >= 18:
            st.success(f"Hello {name}, you are eligible to vote!")
        else:
            st.error(f"Sorry {name}, you are not eligible to vote yet.")

if __name__ == "__main__":
    main()
