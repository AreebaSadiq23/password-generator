import streamlit as st
import random
import string

def generate_password(length=12, use_special=True, use_numbers=True, use_upper=True):
    characters = string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_strength(password):
    score = 0
    if any(char.isdigit() for char in password):
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char in string.punctuation for char in password):
        score += 1
    if len(password) >= 12:
        score += 1

    # **Fix: Ensure score remains within the valid index range (0 to 3)**
    score = min(score, 3)
    
    return ["Weak", "Moderate", "Strong", "Very Strong"][score]

# Streamlit UI
st.title("🔑 Secure Password Generator")

# User Input Controls
length = st.slider("🔢 Select Password Length", min_value=6, max_value=30, value=12)
use_special = st.checkbox("💥 Include Special Characters", value=True)
use_numbers = st.checkbox("🔢 Include Numbers", value=True)
use_upper = st.checkbox("🔡 Include Uppercase Letters", value=True)

if st.button("⚡ Generate Password"):
    password = generate_password(length, use_special, use_numbers, use_upper)
    strength = password_strength(password)
    
    st.success(f"✅ Generated Password: `{password}`")
    st.info(f"🔍 Password Strength: **{strength}**")

st.write("👆 Click the button to generate a strong password!")
