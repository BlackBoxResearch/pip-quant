import streamlit as st
import numpy as np
import time

# Function to generate synthetic price data
def generate_path(S0, num_points, r, t_step, V, rand, rand_trend, mean, mean_reversion):
    S = S0 * np.ones(num_points)
    trend = 0
    for i in range(1, len(S)):
        trend = trend + rand_trend[i - 1] * S[i - 1] / 2000 - trend / 10
        S[i] = mean_reversion * (mean - S[i - 1]) + S[i - 1] * np.exp((r - 0.5 * V ** 2) * t_step + np.sqrt(t_step) * V * rand[i - 1]) + 0.7 * trend
    return S

# Function to create the accounts page with simulation and synthetic data plotting
def accounts_page():
    st.title("Accounts")

    # Monte Carlo Simulation Section
    st.subheader("Monte Carlo Simulation with Animated Plotting")
    num_simulations = st.slider("Number of Simulations", 1, 100, 10)
    num_steps = st.slider("Number of Steps", 10, 200, 100)
    
    stop_monte_carlo = st.button("Stop Monte Carlo Simulation")

    if st.button("Run Monte Carlo Simulation") and not stop_monte_carlo:
        # Progress bar and chart setup for Monte Carlo simulation
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Initialize random values for each simulation
        last_rows = np.random.randn(1, num_simulations)
        chart = st.line_chart(last_rows)

        # Monte Carlo Simulation loop
        for i in range(1, num_steps + 1):
            if stop_monte_carlo:
                st.warning("Monte Carlo Simulation Stopped")
                break

            new_rows = last_rows[-1, :] + np.random.randn(1, num_simulations)
            chart.add_rows(new_rows)
            status_text.markdown(f"{i}/{num_steps} steps complete")
            progress_bar.progress(int(i / num_steps * 100))
            last_rows = new_rows
            time.sleep(0.05)

        progress_bar.empty()

    st.write("---")  # Separator between the two charts

    # Synthetic Price Data Generation Section
    st.subheader("Synthetic Price Data Generation")
    num_points = st.slider("Number of Data Points", 10, 1000, 500)
    
    stop_synthetic = st.button("Stop Synthetic Data Generation")

    if st.button("Generate Synthetic Price Data") and not stop_synthetic:
        # Set parameters for the synthetic data generation
        S0 = 1
        r = 0
        V = 0.1
        t_step = 1 / 365
        mean = 1
        mean_reversion = 0.004
        seed = 123
        rs = np.random.RandomState(seed)
        
        # Generate random data for the synthetic price path
        rand = rs.standard_normal(num_points - 1)
        rand_trend = rs.standard_normal(num_points - 1)

        # Generate synthetic price path
        close_prices = generate_path(S0, num_points, r, t_step, V, rand, rand_trend, mean, mean_reversion)

        # Progress bar and chart setup for price data
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Plot the synthetic price data step by step
        chart = st.line_chart([close_prices[0]])  # Start chart with the first point
        
        for i in range(1, len(close_prices)):
            if stop_synthetic:
                st.warning("Synthetic Price Data Generation Stopped")
                break
            
            chart.add_rows([close_prices[i]])  # Add one new price point at a time
            status_text.markdown(f"{i}/{num_points} points complete")
            progress_bar.progress(int(i / num_points * 100))
            time.sleep(0.0001)  # Speed up the plot for faster visualization

        progress_bar.empty()

if __name__ == "__main__":
    accounts_page()
