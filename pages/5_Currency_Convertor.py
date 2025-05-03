import streamlit as st
from utils.currency_utils import currency_converter_widget
from utils.auth import require_auth

st.set_page_config(
    page_title="Currency Converter",
    page_icon="💱",
    layout="wide"
)


require_auth()


st.markdown("""
<style>
    .page-title {
        font-size: 2.5rem !important;
        color: #1E88E5;
    }
    .converter-card {
        background-color: #E8F5E9;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='page-title'>💱 Currency Converter</h1>", unsafe_allow_html=True)
st.markdown("Convert currencies for your international travels")


currency_converter_widget()


st.markdown("## 💡 Currency Tips for Travelers")

tips_col1, tips_col2 = st.columns(2)

with tips_col1:
    st.markdown("""
    <div class="converter-card">
    <h3>Before Your Trip</h3>
    <ul>
    <li>Check if your destination accepts credit cards widely</li>
    <li>Notify your bank about international travel</li>
    <li>Exchange some money before departure for immediate expenses</li>
    <li>Research typical prices at your destination</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with tips_col2:
    st.markdown("""
    <div class="converter-card">
    <h3>During Your Trip</h3>
    <ul>
    <li>Use ATMs for better exchange rates than currency exchange offices</li>
    <li>Pay in local currency when given the option</li>
    <li>Keep a small amount of USD as emergency backup</li>
    <li>Save receipts for currency exchanges</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)