import streamlit as st
import random

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
        "making the bed": "I’m making the bed and lying it too..."
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
st.title("🎵 RodriLetras: Explora las letras de Olivia Rodrigo")

menu = st.sidebar.radio("Selecciona una sección:", ["🔍 Buscador", "🎮 Juegos", "🎭 Según tu emoción"])

# ---------- BUSCADOR -----------
if menu == "🔍 Buscador":
    st.subheader("Buscar letras de canciones")
    palabra = st.text_input("Ingresa una palabra clave:")
    album_filtrado = st.selectbox("Filtrar por álbum:", ["Todos"] + list(canciones_por_album.keys()))

    if st.button("Buscar"):
        resultados = []
        for album, canciones in canciones_por_album.items():
            if album_filtrado != "Todos" and album != album_filtrado:
                continue
            for titulo, letra in canciones.items():
                if palabra.lower() in letra.lower():
                    resultados.append((titulo, album, letra))

        if resultados:
            for titulo, album, letra in resultados:
                st.markdown(f"**{titulo}** ({album})\n> *{letra}*")
        else:
            st.warning("No se encontraron coincidencias.")

# ---------- JUEGOS -----------
elif menu == "🎮 Juegos":
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

        if st.button("Responder"):
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

        if st.button("Revisar"):
            if respuesta == album:
                st.success("✅ ¡Correcto!")
            else:
                st.error(f"❌ Incorrecto. Era: {album} ({titulo})")

# ---------- JUEGO EMOCIONAL -----------
elif menu == "🎭 Según tu emoción":
    st.subheader("¿Cómo te sientes hoy?")
    emocion = st.select_slider("Desliza para elegir:", options=list(letras_por_emocion.keys()))

    if emocion:
        letra = random.choice(letras_por_emocion[emocion])
        st.markdown(f"### Letra recomendada para ti ({emocion}):\n> *{letra}*")
