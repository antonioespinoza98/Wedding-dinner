import streamlit as st


st.set_page_config(page_title="Chiara&Marco.com",
                    layout="wide", page_icon=":bouquet:",
                      initial_sidebar_state="expanded")

with st.sidebar:
    st.title("Chiara&Marco.com") 
    with st.container(border=True):
        st.image("img/nosotros.jpg")
        st.header("24 Luglio 2025")
        st.header("Ora dell'evento: 18:00")
        st.header("Indirizzo dell'evento: Via Alessandro Guidotti, 32/3, 40134 Bologna BO, Italia")
    
tabs1, tabs2 = st.tabs([ 
                                             "Lista dei desideri :gift:", 
                                             "Contatti e info :telephone_receiver:",
                                             ])


with tabs1:
    st.title("Lista dei desideri")
    with st.container(border=True):
        st.markdown("""
        ### *Da ciascuno secondo le sue possibilitá...* 
        """)
        st.markdown("""
        Abbiamo pensato ad alcune cose di cui avremo bisogno per il nostro trasloco a Maastricht,
        e ci piacerebbe che ci aiutaste con quello che potete!
        """)

        st.subheader("Istruzioni :pushpin:")
        st.markdown("""
            - Puoi scegliere qualsiasi oggetto della lista e decidere quanto vuoi contribuire
            - Se vuoi regalare qualcosa che non sia materiale, puoi selezionare il salvadanaio per i viaggi :pig2:
            - Una volta selezionato il regalo, troverai i dati per il bonifico! Per favore, aggiungi il regalo scelto nella causale
            - se hai una idea geniale che non è nella lista non la rifutiamo però considera che deve entrar in valigia :luggage:
                                            """)

    @st.dialog("Grazie per contribuire a questo regalo!")
    def dialog():
        st.write("Per favore, effettua il bonifico su uno dei seguenti conti bancari:")
        with st.container(border=True):
            st.markdown("""
            **Cliente:** MARCO ANTONIO ESPINOZA MARIN 
                        
            **Número de cuenta BAC:** 962085296 
                        
            **Número de cuenta IBAN:** CR39010200009620852961
                        
            **Detalle:** Artículo elegido de la lista de deseos
            """)
        with st.container(border=True):
            st.markdown("""
            **Nome:** Di Tommaso Chiara Alessandra
            
            **IBAN:** IT85E0707202409000000408406
            
            **BIC/SWIFT:** ICRA IT RRTS0
            
            **Causale:** articolo scelto dalla lista dei desideri
            """)
    
    with st.expander("Lista dei desideri :point_down:", expanded=False):
        # -- BICICLETA
        with st.container(border=True):
            col1, col2 = st.columns(2)
            with col1:
                st.image("img/biciChiara.jpg", width=300)
            with col2:
                st.subheader("Bicicletta di Chiara")
                st.markdown("""
                - Bicicletta da passeggio, con cestino e luci!
                - Estado: Condizioni: Usata
                - Taglia M
                """)
                button = st.button("Voglio regalare la bicicletta di Chiara!", key="chiara_bici")
                if button:
                    dialog()
        # --    BICICLETA MARCO
        with st.container(border=True):
            col1, col2 = st.columns(2)
            with col1:
                st.image("img/biciMarco.jpg", width=300)
            with col2:
                st.subheader("Bicicletta di Marco")
                st.markdown("""
                - Bicicletta da passeggio!
                - Condizioni: Usata
                - Taglia L
                """)
                button = st.button("Voglio regalare la bicicletta di Marco!", key="marco_bici")
                if button:
                    dialog()
        # -- Vasos
        with st.container(border=True):
            col1, col2 = st.columns(2)
            with col1:
                st.image("img/vasos.jpg", width=300)
            with col2:
                st.subheader("Bicchieri")
                st.markdown("""
                - Bicchieri di vetro!
                - Quantità: 10
                - Per le cene a  cui vi inviteremo!!
                        
                """)
                button = st.button("Voglio regalare i bicchieri!",key="vasos")
                if button:
                    dialog()
        # -- Copas
        with st.container(border=True):
            col1, col2 = st.columns(2)
            with col1:
                st.image("img/copasVino.jpg", width=300)
            with col2:
                st.subheader("Calici")
                st.markdown("""
                - Calici da vino!
                - Quantità: 10 
                            
                """)
                button = st.button("Voglio regalare i bicchieri!", key="copas")
                if button:
                    dialog()
        # -- Utencilios
        with st.container(border=True):
            col1, col2 = st.columns(2)
            with col1:
                st.image("img/utencilios.jpg", width=300)
            with col2:
                st.subheader("Utensili da cucina")
                st.markdown("""                
                - Quantità: set completo
                """)
                button = st.button("Voglio regalare i utensili!",key="utencilios")
                if button:
                    dialog()
        # -- Tacitas
        with st.container(border=True):
            col1, col2 = st.columns(2)
            with col1:
                st.image("img/tacitas.jpg", width=300)
            with col2:
                st.subheader("Tazze e tazzine")
                st.markdown("""                
                - Quantità: 6
                """)
                button = st.button("Voglio regalare le tazzine!",key="Tazas")
                if button:
                    dialog()
        # -- platos
        with st.container(border=True):
            col1, col2 = st.columns(2)
            with col1:
                st.image("img/platos.jpg", width=300)
            with col2:
                st.subheader("Piatti, con set di cucchiai, forchette e coltelli")
                st.markdown("""                
                - Quantità: set per 6 persone (per quando ci visiterete!)
                """)
                button = st.button("Voglio regalare le piatti!",key="platos")
                if button:
                    dialog()
        # -- cafetera
        with st.container(border=True):
            col1, col2 = st.columns(2)
            with col1:
                st.image("img/cafetera.jpg", width=300)
            with col2:
                st.subheader("La Moka")
                st.markdown("""

                """)
                button = st.button("Voglio regalare la Moka!",key="moka")
                if button:
                    dialog()
        # -- platos hondos
        with st.container(border=True):
            col1, col2 = st.columns(2)
            with col1:
                st.image("img/platoshondos.jpg", width=300)
            with col2:
                st.subheader("Set di ciotole")
                st.markdown("""
                - Set di ciotole per cereali, yogurt, frutta, salse e insalate""")
                button = st.button("Voglio regalare di ciotole!",key="hondos")
                if button:
                    dialog()

        # -- Cuchillos
        with st.container(border=True):
            col1, col2 = st.columns(2)
            with col1:
                st.image("img/cuchillos.jpg", width=300)
            with col2:
                st.subheader("set di coltelli con tagliere")
                button = st.button("Voglio regalare di coltelli!",key="cuchillos")
                if button:
                    dialog()

        # -- Freidora
        with st.container(border=True):
            col1, col2 = st.columns(2)
            with col1:
                st.image("img/freidora.jpg", width=300)
            with col2:
                st.subheader("Friggitrice ad aria (o fornetto elettrico)")
                st.markdown("""
                            Fondamentale perche nell'appartamento non c'e il forno!!""")
                button = st.button("Voglio regalare di friggitrice!",key="freidora")
                if button:
                    dialog()

        # -- licuadora
        with st.container(border=True):
            col1, col2 = st.columns(2)
            with col1:
                st.image("img/licuadora.jpg", width=300)
            with col2:
                st.subheader("Frullatore")
                button = st.button("Voglio regalare di frullatore!",key="licuadora")
                if button:
                    dialog()

        # -- Mesa de noche
        with st.container(border=True):
            col1, col2 = st.columns(2)
            with col1:
                st.image("img/mesadenoche.jpg", width=300)
            with col2:
                st.subheader("Comodini")
                button = st.button("Voglio regalare i comodini!",key="comodini")
                if button:
                    dialog()

        # -- Hervidor
        with st.container(border=True):
            col1, col2 = st.columns(2)
            with col1:
                st.image("img/hervidor.jpg", width=300)
            with col2:
                st.subheader("Bollitore")
                st.markdown("""
                  per un te caldo d'inverno  
                             """)
                button = st.button("Voglio regalare il bollitore!",key="bollitore")
                if button:
                    dialog()
        
        # -- Luz 
        with st.container(border=True):
            col1, col2 = st.columns(2)
            with col1:
                st.image("img/luz.jpg", width=300)
            with col2:
                st.subheader("Lampada da lettura")
                button = st.button("Voglio regalare la lampada",key="lampara")
                if button:
                    dialog()

        # -- proyector
        with st.container(border=True):
            col1, col2 = st.columns(2)
            with col1:
                st.image("img/proyector.jpg", width=300)
            with col2:
                st.subheader("Proiettore")
                st.markdown("""
                - Per vedere film !!! Una delle nostre attivita' preferite
                """)
                button = st.button("Voglio regalare il proiettore",key="proyector")
                if button:
                    dialog()

        # -- parlante
        with st.container(border=True):
            col1, col2 = st.columns(2)
            with col1:
                st.image("img/parlante.jpg", width=300)
            with col2:
                st.subheader("Cassa per la música")
                st.markdown("""
                - Marco, come ogni buon latino, ha bisogno della musica per pulire casa!
                """)
                button = st.button("Voglio regalare il cassa per la música",key="parlante")
                if button:
                    dialog()

        # -- sofa cama
        with st.container(border=True):
            col1, col2 = st.columns(2)
            with col1:
                st.image("img/sofacama.jpg", width=300)
            with col2:
                st.subheader("divano letto")
                st.markdown("""
                - per gli ospiti che ci vengono a trovare!!
                """)
                button = st.button("Voglio regalare il divano letto",key="divano")
                if button:
                    dialog()

        # -- plantas
        with st.container(border=True):
            col1, col2 = st.columns(2)
            with col1:
                st.image("img/plantas.jpg", width=300)
            with col2:
                st.subheader("Piante per la nostra casa")

                button = st.button("Voglio regalare delle piante",key="plantas")
                if button:
                    dialog()
        # -- chanchito
        with st.container(border=True):
            col1, col2 = st.columns(2)
            with col1:
                st.image("img/cobija.jpg", width=300)
            with col2:
                st.subheader("Set coperte con cuscini")
                button = st.button("Voglio contribuire al set coperte con cuscini",key="cobijas")
                if button:
                    dialog()
        # -- chanchito
        with st.container(border=True):
            col1, col2 = st.columns(2)
            with col1:
                st.image("img/chanchito.jpg", width=300)
            with col2:
                st.subheader("Porcellino viaggiatore")
                button = st.button("Voglio contribuire al salvadanaio per i viaggi",key="chancho")
                if button:
                    dialog()

with tabs2:
    st.title("hai domande? Chiamaci su WhatsApp! :telephone_receiver:")
    with st.container(border=True):
        col1, col2 = st.columns(2)
        with col1:
            st.image("img/chiara.jpg", width=100)
        with col2:
            st.subheader("Numero :calling:")
            st.write("+39 3472786628")
    with st.container(border=True):
        col1, col2 = st.columns(2)
        with col1:
            st.image("img/marco.jpg", width=100) 
        with col2:
            st.subheader("Número :calling:")
            st.write("+39 3534797619")

