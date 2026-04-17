import streamlit as st

st.title("welcom our app")
st.header("titre d'une section")
st.subheader("titre d'une soussection")
st.write("lamine")
st.markdown("""voici les etapes pôur creer
*etape1
*etape2""")
st.button("envoyer")
st.radio("votre genre",["Homme","Femme"])
st.selectbox("votre choix",["sig","python"])
st.multiselect("votre choix",["sig","python","Geomatique","Eelectromecanique"])
#alerte
st.info("Informatique")
st.success("leg")
st.warning("Attention")
st.error("erreur")

#saisir
st.text_input("nom")
st.number_input("age")
st.date_input("date")
st.time_input("heure")
st.text_area("commentaire")

#media
st.image("IMPG.png")
#st.audio("music")
st.balloons()
with st.sidebar:
    st.header("barre")
    #alerte
    st.info("Informatique")
    st.success("leg")
    st.warning("Attention")
    st.error("erreur")

st.write("---")
st.header("APPLICATION CALCULE SOMME")
a = st.number_input("nombre1")

    