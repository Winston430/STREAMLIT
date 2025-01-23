import streamlit as st
import pandas as pd
import random  # For dummy data

# Placeholder functions for API interactions (replace with actual API calls)
def get_account_balance(account_type):
    # Simulate fetching balance from different services
    if account_type == "M-Pesa":
        return random.randint(100, 10000)
    elif account_type == "Airtel Money":
        return random.randint(50, 5000)
    elif account_type == "CRDB":
        return random.randint(1000, 50000)
    # ... Add more services
    else:
        return 0

def transfer_money(from_account, to_account, amount):
    # Simulate a transfer (no actual money movement)
    return f"Transfer of {amount} from {from_account} to {to_account} simulated."

def get_exchange_rate(from_currency, to_currency):
    # Simulate fetching exchange rate (replace with API call)
    return random.uniform(0.01, 0.05)  # Example rate

st.title("Pay-Me East Africa")

# User Authentication (Simplified)
user_authenticated = st.checkbox("User Logged In") # Replace with actual auth

if user_authenticated:
    st.write("Welcome, User!")

    # Account Balances
    st.subheader("Account Balances")
    account_types = ["M-Pesa", "Airtel Money", "CRDB", "NMB", "EQUITY", "ABSA", "Halo pesa"] #add all the banks
    balances = {account: get_account_balance(account) for account in account_types}

    balance_data = pd.DataFrame(list(balances.items()), columns=['Account', 'Balance'])
    st.dataframe(balance_data)

    total_balance = sum(balances.values())
    st.metric("Total Balance", f"KES {total_balance}") #change to your currency

    # Money Transfer
    st.subheader("Money Transfer")
    from_account = st.selectbox("From Account", account_types)
    to_account = st.selectbox("To Account", account_types)
    transfer_amount = st.number_input("Amount", min_value=1)

    if st.button("Transfer"):
        transfer_result = transfer_money(from_account, to_account, transfer_amount)
        st.write(transfer_result)

    # Bill Payments (Simplified)
    st.subheader("Bill Payments")
    bill_type = st.selectbox("Bill Type", ["Netflix", "Spotify", "Electricity", "Water"])
    bill_amount = st.number_input("Bill Amount", min_value=1)
    if st.button("Pay Bill"):
       st.write(f"Payment of {bill_amount} for {bill_type} simulated.")

    # Currency Converter
    st.subheader("Currency Converter")
    from_currency = st.selectbox("From Currency", ["KES", "USD", "EUR"])
    to_currency = st.selectbox("To Currency", ["KES", "USD", "EUR"])
    amount_to_convert = st.number_input("Amount to Convert", min_value=1)

    if st.button("Convert"):
        exchange_rate = get_exchange_rate(from_currency, to_currency)
        converted_amount = amount_to_convert * exchange_rate
        st.write(f"{amount_to_convert} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

else:
    st.write("Please log in to access the features.")
