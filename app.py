
import streamlit as st

from password import generate_password

with open( "css/style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)
# Logo

st.title(":lock: Random Password Generator")
st.header("Generate a random password based on user input to keep your data secure.", divider=True)

st.write("Password Length")
length = st.slider("Select the length of your password", 8, 32, 16, 1)

st.write("Password must contains:")  
col1, col2, col3, col4 = st.columns(4)
with col1:
    use_uppercase = st.checkbox("ABC", value=True)
with col2:
    use_lowercase = st.checkbox("abc", value=True)
with col3:
    use_numbers = st.checkbox("123", value=True)
with col4:
    use_symbols = st.checkbox("@#$", value=True)

if not any([use_uppercase, use_lowercase, use_numbers, use_symbols]):
    st.warning("Please select at least one option to generate a password.")
    st.stop()

new_password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_symbols)

st.subheader("Your new password is:")
with st.empty():
    st.markdown(f'<span class="password">{new_password}</span>' , unsafe_allow_html= True)

st.button("Generate new password")





