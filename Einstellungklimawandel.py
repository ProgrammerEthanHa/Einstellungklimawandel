import streamlit as st
import pandas as pd
import altair as alt

st.header("Einstellungen und Haltungen der Jugendlichen zum Klimawandel")
st.subheader("")

source = pd.DataFrame({
        'Anteil(%)': [26, 53, 21],
        'Einstufung': ['Klimaoptimisten', 'Kritiker des Klimawandels', 'Fatalistische Beobachter']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil(%):Q',
        x='Einstufung:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: Statista")