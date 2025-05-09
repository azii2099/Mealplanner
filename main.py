import streamlit as st
from utils.data_manager import init_session_state
from components.profile import render_profile_section
from components.meal_plan import render_meal_plan_section
from components.tracking import render_tracking_section

st.set_page_config(
    page_title="AI Meal Planner",
    page_icon="🍝",
    layout="wide",
    initial_sidebar_state="expanded"
)

def load_css():
    with open("styles/custom.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def main():
    load_css()
    init_session_state()
    
    st.title("🥗 AI Meal Planner")
    
    # Sidebar navigation
    page = st.sidebar.radio("Navigation", 
                           ["Profile", "Meal Plan", "Tracking"])
    
    # Display selected section
    if page == "Profile":
        render_profile_section()
    elif page == "Meal Plan":
        if not st.session_state.user_profile['name']:
            st.warning("Please complete your profile first!")
        else:
            render_meal_plan_section()
    else:
        if not st.session_state.user_profile['name']:
            st.warning("Please complete your profile first!")
        else:
            render_tracking_section()
    
    # Footer
    st.sidebar.markdown("---")
    st.sidebar.markdown("Built with ❤️ using Streamlit and OpenAI BY AZIZ REHMAN")

if __name__ == "__main__":
    main()
