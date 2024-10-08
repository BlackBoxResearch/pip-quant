import streamlit as st
import random
import pandas as pd

def leaderboard_page():
    st.title("Leaderboard")

    df = pd.DataFrame(
        {
            "Rank": ["1", "2", "3"],
            "Account": ["John Smith", "Terry Cruise", "Mike Drop"],
            "Score": [random.randint(0, 1000) for _ in range(3)],
            "Equity Curve": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
        }
    )
    st.dataframe(
        df,
        column_config={
            "name": "App name",
            "stars": st.column_config.NumberColumn(
                "Github Stars",
                help="Number of stars on GitHub",
                format="%d ⭐",
            ),
            "Account": st.column_config.LinkColumn("Account"),
            "Equity Curve": st.column_config.LineChartColumn(
                "Equity Curve", y_min=0, y_max=5000
            ), 
        },
        hide_index=True,
    )

if __name__ == "__main__":
    leaderboard_page()