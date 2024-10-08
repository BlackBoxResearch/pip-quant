import streamlit as st
import time
import numpy as np

# Define the Accounts page
def accounts_page():
    st.title("Accounts")
    st.write("This is the Accounts page with some demo plotting.")

    # Progress bar and chart demo on the Accounts page
    progress_bar = st.progress(0)
    status_text = st.empty()
    last_rows = np.random.randn(1, 1)
    chart = st.line_chart(last_rows)

    for i in range(1, 101):
        new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
        status_text.text("%i%% Complete" % i)
        chart.add_rows(new_rows)
        progress_bar.progress(i)
        last_rows = new_rows
        time.sleep(0.05)

    progress_bar.empty()
    st.button("Update")

# Run the page
if __name__ == "__main__":
    accounts_page()
