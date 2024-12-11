import streamlit as st
from post_crew import CrewPostagem
crew_postagem = CrewPostagem ()

st.title ('Sistema de Postagem com CrewAI ')
tema = st.text_input ('Digite o tópico para a postagem ', 'IA na saúde')

if st.button ('Iniciar Processo ') :
    with st.spinner ('Executando tarefas do Crew ... ') :
        result = crew_postagem.kickoff (inputs ={'topic': tema })
        st.success ('Processo concluído!')
    st.subheader ('Postagem Gerada!')
    st.write ( result )
