import streamlit as st
import numpy as np
import pandas as pd
import math

# 1. Title/Header Setup
st.title("🧮 Advanced Scientific Calculator")
st.markdown("---")

# 2. Capture user input using Streamlit's text input widget
# Instead of input(), this provides a clean web text box
user_input = st.text_input("Enter your calculation (e.g., 5 + 5 or math.sqrt(16)):", key="calc_input")

# 3. Create a clean column layout for buttons
col1, col2 = st.columns([1, 5])

with col1:
    # Clicking this button re-runs the script and evaluates the math
    calculate_button = st.button("Calculate", type="primary")

# 4. Process the math expression when the button is clicked or Enter is pressed
if user_input:
    # Handle manual exit strings safely without crashing the script
    if user_input.strip().lower() in ['quit', 'exit']:
        st.info("To close the calculator, simply close this browser tab!")
    
    # Check if they typed text instead of math equations
    elif any(char.isalpha() for char in user_input) and not user_input.strip().startswith(('math.', 'np.', 'numpy.')):
        st.error("Sorry - this is a calculator. Please enter a mathematical expression.")
        
    else:
        try:
            # Create a safe environment for eval
            allowed_names = {
                'math': math,
                'np': np,
                'numpy': np,
                'pd': pd,
                'pandas': pd
            }
            
            # Evaluate expression safely
            result = eval(user_input, {"__builtins__": None}, allowed_names)
            
            # Display successful results beautifully
            st.success(f"**Result:** {result}")
            
        except Exception as e:
            st.error(f"Error: Invalid Expression ({e})")
