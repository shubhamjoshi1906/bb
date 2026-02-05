import streamlit as st

st.set_page_config(page_title="Only For You 💖", layout="centered")

# ---------------- SESSION STATE ----------------
if "step" not in st.session_state:
    st.session_state.step = 0
if "name" not in st.session_state:
    st.session_state.name = ""

# ---------------- GLOBAL STYLES ----------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #ffe6eb, #fff0f5);
}
h1, h2, h3 {
    font-family: 'Trebuchet MS', sans-serif;
    text-align: center;
}
.floating-hearts {
    position: fixed;
    bottom: -50px;
    animation: floatUp 8s infinite ease-in;
    font-size: 24px;
}
@keyframes floatUp {
    0% {transform: translateY(0); opacity: 0;}
    20% {opacity: 1;}
    100% {transform: translateY(-800px); opacity: 0;}
}
#no-btn {
    position: absolute;
    animation: float 3s ease-in-out infinite;
}
@keyframes float {
    0% {transform: translate(0, 0);}
    50% {transform: translate(30px, -20px);}
    100% {transform: translate(0, 0);}
}
</style>
""", unsafe_allow_html=True)

# ---------------- FLOATING HEARTS ----------------
st.markdown("""
<div class="floating-hearts" style="left:10%;">💖</div>
<div class="floating-hearts" style="left:40%;">💕</div>
<div class="floating-hearts" style="left:70%;">💗</div>
""", unsafe_allow_html=True)

# ---------------- ROMANTIC MUSIC ----------------
st.markdown("""
<audio autoplay loop>
<source src="https://cdn.pixabay.com/audio/2022/10/25/audio_3f7c1fa65c.mp3" type="audio/mp3">
</audio>
""", unsafe_allow_html=True)

# ---------------- STEP 0 : SECRET ENTRY ----------------
if st.session_state.step == 0:
    st.markdown("<h1>🌸 Hey Beautiful 🌸</h1>", unsafe_allow_html=True)
    password = st.text_input("Only enter if you are *khushi khushi* 💕", type="password")

    if password:
        if password.lower() == "khushi khushi":
            st.success("Hehe… welcome 😌")
            if st.button("Come closer 💌"):
                st.session_state.step = 1
                st.rerun()
        else:
            st.error("Nope 😌 This place isn’t for everyone")

# ---------------- STEP 1 : NAME ----------------
elif st.session_state.step == 1:
    st.markdown("<h1>💬 One small thing first…</h1>", unsafe_allow_html=True)
    name = st.text_input("What should he call you? 🥺")

    if name and st.button("Okay 💕"):
        st.session_state.name = name
        st.session_state.step = 2
        st.rerun()

# ---------------- STEP 2 : THE QUESTION ----------------
elif st.session_state.step == 2:
    st.markdown(
        f"""
        <h1>{st.session_state.name} 💖</h1>
        <h2>Be honest…</h2>
        <h2>Are you Shubham’s girlfriend? 😏</h2>
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
            const x = Math.random() * window.innerWidth * 0.6;
            const y = Math.random() * window.innerHeight * 0.6;
            btn.style.left = x + "px";
            btn.style.top = y + "px";
        }
        </script>
        """, unsafe_allow_html=True)

# ---------------- STEP 3 : FINAL LOVE ----------------
elif st.session_state.step == 3:
    st.markdown(
        f"""
        <h1>💖 Okay {st.session_state.name}…</h1>
        <h2>You already know this…</h2>

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

        <h3>— forever & always</h3>
        """,
        unsafe_allow_html=True
    )


