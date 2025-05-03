import streamlit as st
import requests
import pandas as pd
from datetime import datetime

def get_exchange_rates(base_currency="USD"):
    """Get current exchange rates"""
    try:
        url = f"https://open.er-api.com/v6/latest/{base_currency}"
        response = requests.get(url)
        data = response.json()
        
        if data['result'] == 'success':
            return data['rates']
        else:
            st.error("Could not fetch exchange rates")
            return None
    except Exception as e:
        st.error(f"Error fetching exchange rates: {e}")
        return None

def currency_converter_widget():
    """Display a currency converter widget"""
    st.subheader("💱 Currency Converter")
    
    
    rates = get_exchange_rates()
    
    if rates:
        
        currencies = list(rates.keys())
        
        col1, col2 = st.columns(2)
        
        with col1:
            from_currency = st.selectbox("From Currency", currencies, index=currencies.index("USD"))
            amount = st.number_input("Amount", min_value=0.01, value=100.00, step=10.0)
            
        with col2:
            to_currency = st.selectbox("To Currency", currencies, index=currencies.index("EUR"))
            
            
            if from_currency == "USD":
                conversion_rate = rates[to_currency]
            else:
                
                usd_value = amount / rates[from_currency]
                conversion_rate = rates[to_currency] / rates[from_currency]
            
            converted_amount = amount * conversion_rate
            
            st.metric(
                label=f"Converted Amount ({to_currency})",
                value=f"{converted_amount:.2f} {to_currency}",
                delta=f"Rate: 1 {from_currency} = {conversion_rate:.4f} {to_currency}"
            )
        
        
        st.caption(f"Exchange rates last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        
        
        st.subheader("Popular Currency Pairs")
        popular_currencies = ["USD", "EUR", "GBP", "JPY", "CAD", "AUD"]
        
        
        popular_rates = {k: rates[k] for k in popular_currencies if k in rates}
        
        
        rates_df = pd.DataFrame({
            "Currency": popular_rates.keys(),
            f"Value (1 USD)": [f"{rate:.4f}" for rate in popular_rates.values()]
        })
        
        st.table(rates_df)
    else:
        st.warning("Could not load exchange rates. Please try again later.")