import streamlit as st
import pandas as pd
import plotly.express as px

# Seitenkonfiguration
st.set_page_config(page_title="Ijeoma Osakwe - Data Analyst Portfolio", layout="wide")

# Header
st.title("Ijeoma Osakwe")
st.subheader("Computational Linguist & Junior Data Analyst Aspirant")
st.markdown("""
Ich verwandle komplexe Daten in klare Handlungsempfehlungen. 
Mit einem Master in Computational Linguistics und Erfahrung in SQL, Python und NLP 
unterstütze ich Teams dabei, datengetriebene Entscheidungen zu treffen.
""")

# Sidebar Navigation
menu = ["Über mich", "Projekte", "Skills & Sprachen", "Kontakt"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Über mich":
    st.header("Wer ich bin")
    st.write("""
    Als Computerlinguistin mit Erfahrung bei Cornerstone OnDemand und DeepL 
    habe ich gelernt, wie man semantische Strukturen analysiert und Datenqualität sicherstellt.
    Mein Ziel bei Sony Music ist es, diese analytische Präzision einzusetzen, um 
    Marketingstrategien zu optimieren und Fandoms nachhaltig aufzubauen.
    """)
    st.info("📍 Stuttgart, Deutschland | 🇩🇪 Deutsch (C1) | 🪈 Flötist")

elif choice == "Projekte":
    st.header("Relevante Projekte")
    
    # Projekt 1: Cornerstone OnDemand
    st.subheader("Ontologie-Mapping & Datenoptimierung @ Cornerstone OnDemand")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Herausforderung:**")
        st.write("Verbesserung der Skills-Ontologie durch semantische Erweiterungen.")
    with col2:
        st.markdown("**Lösung:**")
        st.write("SQL-Optimierung und Zusammenarbeit mit Data Scientists.")
    
    st.success("Ergebnis: Reduzierte Latenz bei Datenabfragen und schnellere Modelliterationen.")
    
    # Visualisierung (Beispiel-Daten)
    st.markdown("### Performance-Metriken (Beispiel)")
    data = pd.DataFrame({
        'Monat': ['Jan', 'Feb', 'Mär', 'Apr'],
        'Datenqualität': [85, 88, 92, 95],
        'Effizienz': [70, 75, 85, 90]
    })
    fig = px.line(data, x='Monat', y=['Datenqualität', 'Effizienz'], title='Verbesserung der Datenqualität')
    st.plotly_chart(fig, use_container_width=True)

    # Projekt 2: Marigold Health
    st.subheader("Sentiment-Analyse & Klassifikation @ Marigold Health")
    st.write("Entwicklung eines ML-Klassifikators (Python, scikit-learn) zur Kategorisierung von Gesundheitsdaten aus sozialen Medien.")
    st.code("Python, scikit-learn, Pandas", language="python")

elif choice == "Skills & Sprachen":
    st.header("Technische Fähigkeiten")
    
    # Skills Visualisierung
    skills_data = pd.DataFrame({
        'Skill': ['Python', 'SQL', 'NLP (spaCy, NLTK)', 'Streamlit', 'Data Storytelling'],
        'Level': [95, 90, 90, 85, 80]
    })
    fig_bar = px.bar(skills_data, x='Skill', y='Level', color='Level', title='Technische Kompetenz', range_y=[0, 100])
    st.plotly_chart(fig_bar, use_container_width=True)
    
    st.header("Sprachen")
    st.write("""
    - **Igbo:** Muttersprache
    - **Englisch:** Muttersprache
    - **Deutsch:** C1
    - **Spanisch:** C1
    - **Brasilianisches Portugiesisch:** B2
    - **Arabisch:** A1
    """)

elif choice == "Kontakt":
    st.header("Kontakt aufnehmen")
    st.write("Ich freue mich darauf, meine Fähigkeiten bei Sony Music einzubringen.")
    st.email("iosakwe@protonmail.ch")
    st.link_button("LinkedIn Profil", "https://linkedin.com/in/iosakwe")
    st.download_button("Lebenslauf als PDF herunterladen", data=open("Ijeoma_Osakwe_CV.pdf", "rb"), file_name="Ijeoma_Osakwe_CV.pdf")
