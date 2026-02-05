import streamlit as st
import random

st.set_page_config(page_title="Only For You 💖", layout="centered")

# ---------- SESSION STATE ----------
if "step" not in st.session_state:
    st.session_state.step = 0

if "name" not in st.session_state:
    st.session_state.name = ""

# ---------- BACKGROUND ----------
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #ffdde1, #ee9ca7);
    }
    button {
        font-size: 18px !important;
        border-radius: 12px !important;
        padding: 10px 20px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- STEP 0 : PASSWORD ----------
if st.session_state.step == 0:
    st.markdown("<h1 style='text-align:center;'>🔐 Secret Entry 🔐</h1>", unsafe_allow_html=True)
    password = st.text_input("Only allowed if you are *khushi khushi* 💕", type="password")

    if password:
        if password.lower() == "khushi khushi":
            st.success("Access Granted 💖")
            if st.button("Enter 😌"):
                st.session_state.step = 1
                st.rerun()
        else:
            st.error("Nope 😌 Try again")

# ---------- STEP 1 : NAME ----------
elif st.session_state.step == 1:
    st.markdown("<h1 style='text-align:center;'>💌 Before We Proceed…</h1>", unsafe_allow_html=True)
    name = st.text_input("What should I call you? 🥺")

    if name:
        if st.button("Continue 💕"):
            st.session_state.name = name
            st.session_state.step = 2
            st.rerun()

# ---------- STEP 2 : GIRLFRIEND QUESTION ----------
elif st.session_state.step == 2:
    st.markdown(
        f"""
        <h1 style="text-align:center;">Hey {st.session_state.name} 💖</h1>
        <h2 style="text-align:center;">Are you Shubham’s girlfriend? 😏</h2>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("damn yas 😍"):
            st.balloons()
            st.session_state.step = 3
            st.rerun()

    with col2:
        st.markdown(
            """
            <button id="no-btn" onclick="moveButton()">no 😒</button>

            <script>
            function moveButton() {
                const btn = document.getElementById("no-btn");
                const x = Math.random() * 300 - 150;
                const y = Math.random() * 300 - 150;
                btn.style.transform = `translate(${x}px, ${y}px)`;
            }
            </script>
            """,
            unsafe_allow_html=True
        )

# ---------- STEP 3 : FINAL LOVE CONFESSION ----------
elif st.session_state.step == 3:
    st.markdown(
        f"""
        <h1 style="text-align:center;">💖 Okay {st.session_state.name}…</h1>
        <h2 style="text-align:center;">You know he calls you…</h2>

        <h1 style="text-align:center;">
        cutiee 💕<br>
        baby 🥺<br>
        boobysauras 🦖
        </h1>

        <h1 style="text-align:center; color:red;">
        and of course… <br><br>
        M I N E ❤️
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <audio autoplay loop>
            <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mp3">
        </audio>
        """,
        unsafe_allow_html=True
    )

