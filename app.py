import streamlit as st

# Set page title
st.set_page_config(page_title="Largest of 3 numbers")

# Add a title
st.title("Largest of three numbers")

# Add two text boxes
num1 = st.number_input("Enter first number",value=0)
num2 = st.number_input("Enter second number",value=0)
num3 = st.number_input("Enter third number",value=0)


if st.button("Submit"):
    largest = 0

    if ((num1 > num2) and (num1 > num3)):
        largest = num1

    elif(num2 > num3):
        largest = num2

    else:
        largest = num3



    # Show the inputs

    st.write("- Largest of 3 numbers is :")
    st.markdown(f"<h1 style='text-align: center; color: red;'>{largest}</h1>", unsafe_allow_html=True)
