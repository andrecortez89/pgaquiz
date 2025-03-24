import streamlit as st

# Dados do quiz (pergunta, opcoes, indice da correta, explicacao)
quiz = [
    ...  # (mesmo conteúdo das perguntas anteriores, mantido)
]

st.title("Quiz Interativo - Programa de Gerenciamento de Antimicrobianos (PGA)")

if "pontuacao" not in st.session_state:
    st.session_state.pontuacao = 0
if "indice" not in st.session_state:
    st.session_state.indice = 0
if "respostas" not in st.session_state:
    st.session_state.respostas = {}

indice = st.session_state.indice
pontuacao = st.session_state.pontuacao

if indice < len(quiz):
    q = quiz[indice]
    st.subheader(f"Pergunta {indice + 1}")
    resposta = st.radio(q["pergunta"], q["opcoes"], key=f"resposta_{indice}")
    respondeu = st.session_state.respostas.get(indice, False)

    if not respondeu and st.button("Responder", key=f"botao_{indice}"):
        correta = q["opcoes"][q["correta"]]
        if resposta == correta:
            st.success("✅ Resposta correta!")
            st.session_state.pontuacao += 1
        else:
            st.error("❌ Resposta incorreta.")
        st.info(f"Comentário: {q['explicacao']}")
        st.session_state.respostas[indice] = True
        st.session_state.indice += 1
        st.experimental_rerun()
else:
    st.success(f"Fim do quiz! Você acertou {pontuacao} de {len(quiz)} perguntas.")
    if st.button("Reiniciar Quiz"):
        st.session_state.indice = 0
        st.session_state.pontuacao = 0
        st.session_state.respostas = {}
        st.experimental_rerun()
