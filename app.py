import streamlit as st
import time

st.set_page_config(page_title="Only For You 💖", layout="centered")

# ---------------- SESSION STATE ----------------
if "step" not in st.session_state:
    st.session_state.step = 0
if "name" not in st.session_state:
    st.session_state.name = ""
if "music" not in st.session_state:
    st.session_state.music = False

# ---------------- STYLES ----------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #ffe6eb, #fff5f8);
}
h1, h2, h3 {
    font-family: 'Georgia', serif;
    text-align: center;
}
.fade {
    animation: fadeIn 2s ease-in;
}
@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
}
#no-btn {
    position: absolute;
    animation: float 3s ease-in-out infinite;
}
@keyframes float {
    0% {transform: translateY(0);}
    50% {transform: translateY(-20px);}
    100% {transform: translateY(0);}
}
</style>
""", unsafe_allow_html=True)

# ---------------- MUSIC (USER-ACTIVATED) ----------------
if st.session_state.music:
    st.audio(
        "https://cdn.pixabay.com/audio/2023/03/28/audio_4b0b3a8e6c.mp3",
        loop=True,
    )
    st.caption("🎶 soft music just for you")

# ---------------- STEP 0 ----------------
if st.session_state.step == 0:
    st.markdown("<h1 class='fade'>🌸 Hey you 🌸</h1>", unsafe_allow_html=True)
    st.markdown("<h3>This page only opens for one person.</h3>", unsafe_allow_html=True)

    password = st.text_input("Say the magic words 💕", type="password")

    if password.lower() == "khushi khushi":
        if st.button("Enter 💖"):
            st.session_state.music = True
            st.session_state.step = 1
            st.rerun()
    elif password:
        st.error("Not for everyone 😌")

# ---------------- STEP 1 ----------------
elif st.session_state.step == 1:
    st.markdown("<h1 class='fade'>Before anything…</h1>", unsafe_allow_html=True)
    name = st.text_input("What should he call you? 🥺")

    if name and st.button("Okay 💕"):
        st.session_state.name = name
        st.session_state.step = 2
        st.rerun()

# ---------------- STEP 2 ----------------
elif st.session_state.step == 2:
    st.markdown(
        f"""
        <h1 class='fade'>{st.session_state.name} 💖</h1>
        <h2>One honest question…</h2>
        <h2>Are you Shubham’s girlfriend?</h2>
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
        st.markdown("""
        <button id="no-btn" onmouseover="escape()">no 😒</button>

        <script>
        function escape() {
            const btn = document.getElementById("no-btn");
            const x = Math.random() * (window.innerWidth - 100);
            const y = Math.random() * (window.innerHeight - 100);
            btn.style.left = x + "px";
            btn.style.top = y + "px";
        }
        </script>
        """, unsafe_allow_html=True)

# ---------------- STEP 3 ----------------
elif st.session_state.step == 3:
    st.markdown(
        f"""
        <h1 class='fade'>Okay {st.session_state.name}…</h1>
        <h2>This part is obvious but still…</h2>

        <h1>
        He calls you<br><br>
        cutiee 💕<br>
        baby 🥺<br>
        boobysauras 🦖<br><br>
        </h1>

        <h1 style="color:#e60073;">
        and most importantly…<br><br>
        M I N E ❤️
        </h1>

        <h3>— and he means it.</h3>
        """,
        unsafe_allow_html=True
    )
