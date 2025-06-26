import streamlit as st
import random

# ---------- ESTILO PERSONALIZADO OLIVIA RODRIGO ----------
st.markdown(
    """
    <style>
    .main {
        background-color: #f3e6fb;
        margin-left: 22rem;
    }
    h1, h2, h3, h4 {
        font-family: Georgia, serif;
        color: #6a0dad;
    }
    .stButton>button {
        background-color: #d6b3f9;
        color: black;
        border-radius: 12px;
        font-size: 16px;
    }
    .stRadio > div {
        color: #4b007d;
        font-weight: bold;
    }
    [data-testid=stSidebar] {
        position: fixed !important;
        height: 100vh !important;
        overflow-y: auto;
        background-color: #e5ccfa !important;
        border-right: 2px solid #b37cd4;
        z-index: 999;
    }
    [data-testid=stSidebarContent] {
        padding-top: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- DATA -----------
canciones_por_album = {
    "SOUR": {
        "drivers license": "I got my driver's license last week just like we always talked about...",
        "good 4 u": "Well, good for you, I guess you moved on really easily...",
        "traitor": "I wore makeup when we dated 'cause I thought you'd like me more...",
        "1 step forward, 3 steps back": "It's always one step forward and three steps back..."
    },
    "GUTS": {
        "vampire": "Hate to give the satisfaction asking how you're doing now...",
        "bad idea right?": "I know I should stop, but I can't...",
        "get him back!": "I wanna get him back, I wanna make him really jealous...",
        "making the bed": "I’m making the bed and lying in it too..."
    }
}

letras_por_emocion = {
    "😢 Triste": [
        canciones_por_album["SOUR"]["traitor"],
        canciones_por_album["SOUR"]["1 step forward, 3 steps back"]
    ],
    "😊 Enamorada": [
        canciones_por_album["SOUR"]["drivers license"],
        canciones_por_album["GUTS"]["making the bed"]
    ],
    "😤 Despechada": [
        canciones_por_album["SOUR"]["good 4 u"],
        canciones_por_album["GUTS"]["get him back!"]
    ],
    "😎 Empoderada": [
        canciones_por_album["GUTS"]["bad idea right?"],
        canciones_por_album["GUTS"]["vampire"]
    ]
}

# ---------- APP -----------
st.set_page_config(page_title="Rodriletras", page_icon="🎵")

st.sidebar.image("logo.png", width=200)
st.sidebar.title("RodriLetras 💜")
menu = st.sidebar.radio("Navegación:", ["🏠 Inicio", "🔍 Buscador", "🎮 Juegos", "🎭 Según tu emoción"])

# ---------- INICIO -----------
if menu == "🏠 Inicio":
    st.image("horizontal.jpg", use_container_width=True)
    st.title("🎤 RodriLetras")
    st.markdown("""
    Bienvenida/o a **RodriLetras**, una experiencia interactiva con las letras más icónicas de Olivia Rodrigo. 💜

    Explora emociones, juega con fragmentos de canciones y redescubre lo que hace que sus letras conecten tanto con nosotras. Ya sea que estés despechada, enamorada o empoderada... aquí hay algo para ti.

    Elige una opción del menú lateral para comenzar 👇
    """)

# ---------- BUSCADOR -----------
elif menu == "🔍 Buscador":
    st.header("🔍 Buscar letras de canciones")
    palabra = st.text_input("Ingresa una palabra clave:")
    album_filtrado = st.selectbox("Filtrar por álbum:", ["Todos"] + list(canciones_por_album.keys()))

    if st.button("Buscar 🎧"):
        resultados = []
        for album, canciones in canciones_por_album.items():
            if album_filtrado != "Todos" and album != album_filtrado:
                continue
            for titulo, letra in canciones.items():
                if palabra.lower() in letra.lower():
                    resultados.append((titulo, album, letra))

        if resultados:
            for titulo, album, letra in resultados:
                st.markdown(f"**🎵 {titulo}** ({album})\n> *{letra}*")
        else:
            st.warning("No se encontraron coincidencias.")

# ---------- JUEGOS -----------
elif menu == "🎮 Juegos":
    st.header("🎮 Juegos con letras")
    juego = st.selectbox("Elige un juego:", ["🎵 Adivina la canción", "💿 ¿De qué álbum es?"])

    if juego == "🎵 Adivina la canción":
        album = random.choice(list(canciones_por_album.keys()))
        canciones = list(canciones_por_album[album].items())
        seleccionadas = random.sample(canciones, 4)
        correcta = random.choice(seleccionadas)
        fragmento = correcta[1].split("...")[0] + "..."
        opciones = [c[0] for c in seleccionadas]
        random.shuffle(opciones)

        st.write("¿A qué canción pertenece este fragmento?")
        st.markdown(f"> *{fragmento}*")
        respuesta = st.radio("Elige la canción:", opciones)

        if st.button("Responder 🎤"):
            if respuesta == correcta[0]:
                st.success("✅ ¡Correcto!")
            else:
                st.error(f"❌ Incorrecto. Era: {correcta[0]}")

    elif juego == "💿 ¿De qué álbum es?":
        album = random.choice(list(canciones_por_album.keys()))
        canciones = list(canciones_por_album[album].items())
        titulo, letra = random.choice(canciones)
        fragmento = letra.split("...")[0] + "..."
        opciones = list(canciones_por_album.keys())
        random.shuffle(opciones)

        st.write("¿De qué álbum es esta canción?")
        st.markdown(f"> *{fragmento}*")
        respuesta = st.radio("Elige el álbum:", opciones)

        if st.button("Revisar 💿"):
            if respuesta == album:
                st.success("✅ ¡Correcto!")
            else:
                st.error(f"❌ Incorrecto. Era: {album} ({titulo})")

# ---------- JUEGO EMOCIONAL -----------
elif menu == "🎭 Según tu emoción":
    st.header("🎭 Elige tu emoción")
    emocion = st.select_slider("Desliza para elegir:", options=list(letras_por_emocion.keys()))

    if emocion:
        letra = random.choice(letras_por_emocion[emocion])
        st.markdown(f"### Letra recomendada para ti {emocion}:")
        st.markdown(f"> *{letra}*")
