import streamlit as st

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
    background: linear-gradient(135deg, #ffe6eb, #fff1f6);
}
h1, h2, h3 {
    font-family: 'Georgia', serif;
    text-align: center;
}
.divider {
    text-align: center;
    font-size: 22px;
    margin: 20px 0;
}
.fade {
    animation: fadeIn 1.5s ease-in;
}
@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
}

/* Floating hearts */
.heart {
    position: fixed;
    bottom: -50px;
    animation: floatUp 8s infinite ease-in;
    font-size: 22px;
    opacity: 0.7;
}
@keyframes floatUp {
    0% {transform: translateY(0); opacity: 0;}
    20% {opacity: 1;}
    100% {transform: translateY(-900px); opacity: 0;}
}

/* Floating NO button */
#no-btn {
    position: absolute;
    animation: float 3s ease-in-out infinite;
}
@keyframes float {
    0% {transform: translateY(0);}
    50% {transform: translateY(-15px);}
    100% {transform: translateY(0);}
}
</style>
""", unsafe_allow_html=True)

# ---------------- FLOATING HEARTS ----------------
st.markdown("""
<div class="heart" style="left:15%;">💗</div>
<div class="heart" style="left:45%;">💖</div>
<div class="heart" style="left:70%;">💕</div>
""", unsafe_allow_html=True)

# ---------------- MUSIC (USER-CONTROLLED & RELIABLE) ----------------
if st.session_state.music:
    st.audio(
        "https://cdn.pixabay.com/audio/2022/11/09/audio_9cfa0c1a9c.mp3",
        loop=True
    )
    st.caption("🎶 soft music, just in the background")

# ---------------- STEP 0 : ENTRY ----------------
if st.session_state.step == 0:
    st.markdown("<h1 class='fade'>🌸 Hey you 🌸</h1>", unsafe_allow_html=True)
    st.markdown("<h3>This page is meant for one person only.</h3>", unsafe_allow_html=True)
    st.markdown("<div class='divider'>💗 ✨ 💗</div>", unsafe_allow_html=True)

    password = st.text_input("Only enter if you are *khushi khushi* 💕", type="password")

    if password:
        if password.lower() == "khushi khushi":
            st.success("Okay… come in 😌")

            if st.button("Play our song & enter 💖"):
                st.session_state.music = True
                st.session_state.step = 1
                st.rerun()
        else:
            st.error("This isn’t for everyone 😌")

# ---------------- STEP 1 : NAME ----------------
elif st.session_state.step == 1:
    st.markdown("<h1 class='fade'>Before we go ahead…</h1>", unsafe_allow_html=True)
    st.markdown("<h3>Tell me your name 💕</h3>", unsafe_allow_html=True)
    st.markdown("<div class='divider'>🌷 🌷 🌷</div>", unsafe_allow_html=True)

    name = st.text_input("")

    if name and st.button("Okay 💖"):
        st.session_state.name = name
        st.session_state.step = 2
        st.rerun()

# ---------------- STEP 2 : THE QUESTION ----------------
elif st.session_state.step == 2:
    st.markdown(
        f"""
        <h1 class='fade'>{st.session_state.name} 💖</h1>
        <h3>Just one question…</h3>
        <h2>Are you Shubham’s girlfriend?</h2>
        """,
        unsafe_allow_html=True
    )
    st.markdown("<div class='divider'>💫 💕 💫</div>", unsafe_allow_html=True)

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
            const x = Math.random() * (window.innerWidth - 120);
            const y = Math.random() * (window.innerHeight - 120);
            btn.style.left = x + "px";
            btn.style.top = y + "px";
        }
        </script>
        """, unsafe_allow_html=True)

# ---------------- STEP 3 : FINAL ----------------
elif st.session_state.step == 3:
    st.markdown(
        f"""
        <h1 class='fade'>{st.session_state.name}… 💖</h1>
        <h3>This part is obvious.</h3>
        <div class='divider'>💗 💗 💗</div>

        <h1>
        He calls you<br><br>
        cutiee 💕<br>
        baby 🥺<br>
        boobysauras 🦖<br><br>
        </h1>

        <h1 style="color:#e60073;">
        and always…<br><br>
        M I N E ❤️
        </h1>

        <h3>— quietly, sincerely.</h3>
        """,
        unsafe_allow_html=True
    )
