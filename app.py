import streamlit as st

st.set_page_config(page_title="Only for Khushi 💖", layout="centered")

# Session state to control steps
if "step" not in st.session_state:
    st.session_state.step = 1

# STEP 1
if st.session_state.step == 1:
    st.markdown(
        """
        <h1 style="text-align:center;">🚨 Entry Check 🚨</h1>
        <h3 style="text-align:center;">You are only allowed to enter if you are <b>khushi khushi</b></h3>
        <h2 style="text-align:center;">Are you khushi khushi? 😏</h2>
        """,
        unsafe_allow_html=True
    )

    if st.button("YES 💕"):
        st.session_state.step = 2
        st.rerun()

# STEP 2
elif st.session_state.step == 2:
    st.markdown(
        """
        <h1 style="text-align:center;">⚠️ Serious Question ⚠️</h1>
        <h2 style="text-align:center;">Are you Shubham's girlfriend? 💖</h2>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("damn yas 😍"):
            st.session_state.step = 3
            st.rerun()

    with col2:
        st.markdown(
            """
            <style>
            #no-btn {
                position: relative;
            }
            </style>

            <button id="no-btn" onclick="moveButton()">no 😒</button>

            <script>
            function moveButton() {
                const btn = document.getElementById("no-btn");
                const x = Math.random() * 200 - 100;
                const y = Math.random() * 200 - 100;
                btn.style.transform = `translate(${x}px, ${y}px)`;
            }
            </script>
            """,
            unsafe_allow_html=True
        )

# STEP 3
elif st.session_state.step == 3:
    st.markdown(
        """
        <h1 style="text-align:center;">💖 FINAL TRUTH 💖</h1>
        <h2 style="text-align:center;">
        Ohh, you know he calls you...
        </h2>
        <h1 style="text-align:center;">
        cutiee 💕 <br>
        baby 🥺 <br>
        boobysauras 🦖 <br><br>
        and of course...
        </h1>
        <h1 style="text-align:center; color:red;">
        MINE ❤️
        </h1>
        """,
        unsafe_allow_html=True
    )
