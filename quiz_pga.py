import streamlit as st
import pandas as pd
from datetime import datetime
import smtplib
from email.message import EmailMessage

# Configuração da página
st.set_page_config(
    page_title="Quiz Interativo - Programas de Gerenciamento de Antimicrobianos",
    page_icon="💊",
    layout="centered"
)

# Título principal
st.title("Quiz Interativo - Programas de Gerenciamento de Antimicrobianos")

# Função para salvar respostas em CSV
def save_responses(responses):
    try:
        try:
            df = pd.read_csv('respostas_quiz.csv')
        except:
            df = pd.DataFrame()

        responses['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        df = pd.concat([df, pd.DataFrame([responses])], ignore_index=True)
        df.to_csv('respostas_quiz.csv', index=False)
        return True
    except Exception as e:
        st.error(f"Erro ao salvar as respostas: {e}")
        return False

# Função para envio por e-mail
def send_email(responses):
    try:
        msg = EmailMessage()
        msg['Subject'] = "Respostas do Quiz - Programa de Gerenciamento de Antimicrobianos"
        msg['From'] = "andrecortez89@gmail.com"  # 🔁 Substitua pelo seu e-mail
        msg['To'] = responses.get('email', 'destinatario_padrao@email.com')  # Pode ser um destinatário fixo

        # Corpo do e-mail com as respostas
        content = "\n".join([f"{key}: {value}" for key, value in responses.items()])
        msg.set_content(f"Respostas do quiz:\n\n{content}")

        # Configurar servidor SMTP
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login("andrecortez89@gmail.com", "xezgptqvpixtgzcu")  # 🔁 Substitua pela sua senha de app
            smtp.send_message(msg)
        return True
    except Exception as e:
        st.error(f"Erro ao enviar e-mail: {e}")
        return False

# Inicializar estados da sessão
if 'responses' not in st.session_state:
    st.session_state.responses = {}

if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# Formulário
with st.form(key='quiz_form'):
    # Questão 1
    st.subheader("1. Qual a sua instituição?")
    instituicao = st.text_input("Instituição", key="instituicao")
    st.session_state.responses['instituicao'] = instituicao

    # Opcional: E-mail para receber cópia
    st.subheader("Deseja receber uma cópia das suas respostas?")
    email = st.text_input("Digite seu e-mail (opcional)", key="email")
    if email:
        st.session_state.responses['email'] = email

    # Questões do Quiz
    st.subheader("2. Em relação aos componentes do Programa de Gerenciamento de Antimicrobianos...")
    q2 = st.radio("Selecione uma opção", [
        "Formulários de Restrição de antimicrobianos...",
        "Substituição automática de antimicrobianos por outros de mesmo espectro.",
        "Auditoria prospectiva das prescrições...",
        "Implementação de protocolos clínicos..."
    ], key="q2")
    st.session_state.responses['q2'] = q2

    st.subheader("3. Considerando os conceitos apresentados...")
    q3 = st.radio("Selecione uma opção", [
        "São conceitos opostos...",
        "O \"Antimicrobial Stewardship\" refere-se ao conceito...",
        "É aplicável apenas em países de língua inglesa...",
        "É uma prática exclusiva da enfermagem..."
    ], key="q3")
    st.session_state.responses['q3'] = q3

    st.subheader("4. Sobre a auditoria prospectiva com feedback...")
    q4 = st.radio("Selecione uma opção", [
        "Pode ser associada com pré-autorização...",
        "É mais efetiva quando realizada por profissionais...",
        "Limita a liberdade clínica...",
        "Permite a reavaliação do tratamento..."
    ], key="q4")
    st.session_state.responses['q4'] = q4

    st.subheader("5. A equipe de enfermagem responsável...")
    q5 = st.radio("Selecione uma opção", [
        "Utilizando ou orientando as técnicas apropriadas...",
        "Informando se um paciente tem ou não sintomas...",
        "A equipe de enfermagem geralmente sabe...",
        "Pode alertar o time do PGA...",
        "Todas as alternativas acima."
    ], key="q5")
    st.session_state.responses['q5'] = q5

    st.subheader("6. Atribuições do time gestor do PGA...")
    q6 = st.radio("Selecione uma opção", [
        "Definir políticas e normativas do programa",
        "Realizar o monitoramento contínuo...",
        "Revisar antimicrobianos de pacientes...",
        "Propor melhorias para o programa",
        "Discutir o alcance das metas..."
    ], key="q6")
    st.session_state.responses['q6'] = q6

    st.subheader("7. Relacione os componentes essenciais...")
    st.markdown("COLUNA I e II conforme descrição...")
    q7 = st.radio("Selecione a sequência correta", [
        "5, 3, 4, 1, 2, 6",
        "6, 3, 4, 1, 2, 5",
        "5, 3, 4, 2, 1, 6",
        "5, 4, 3, 1, 2, 6",
        "6, 4, 3, 1, 2, 5"
    ], key="q7")
    st.session_state.responses['q7'] = q7

    st.subheader("8. Terapia sequencial refere-se a:")
    q8 = st.radio("Selecione uma opção", [
        "Substituição de um antimicrobiano por outro...",
        "Aumento gradual da dose...",
        "Conversão da via intravenosa para oral...",
        "Alternância de diferentes classes...",
        "Administração de dois antimicrobianos..."
    ], key="q8")
    st.session_state.responses['q8'] = q8

    st.subheader("9. Em relação à otimização da dose...")
    q9 = st.radio("Selecione uma opção", [
        "Infusão prolongada de beta-lactâmicos...",
        "Ajuste posológico conforme características...",
        "Adaptação da dose conforme características clínicas...",
        "Definição do diagnóstico da infecção...",
        "Otimização da forma de preparo..."
    ], key="q9")
    st.session_state.responses['q9'] = q9

    st.subheader("10. Considerando as perguntas norteadoras...")
    q10 = st.text_area("Cole aqui sua resposta (até 2000 caracteres):", height=200, max_chars=2000, key="q10")
    st.session_state.responses['q10'] = q10

    submit_button = st.form_submit_button(label='Enviar Respostas')

    if submit_button:
        required_fields = ['q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9']
        missing_fields = [field for field in required_fields if not st.session_state.responses.get(field)]

        if missing_fields:
            st.error("Por favor, responda todas as questões obrigatórias (questões 2 a 9).")
        else:
            if save_responses(st.session_state.responses):
                if send_email(st.session_state.responses):
                    st.session_state.submitted = True
                    st.success("Respostas enviadas e salvas com sucesso!")

# Mensagem final
if st.session_state.submitted:
    st.balloons()
    st.write("✅ Obrigado por participar do Quiz sobre Programas de Gerenciamento de Antimicrobianos!")
    if st.button("Iniciar Novo Quiz"):
        st.session_state.responses = {}
        st.session_state.submitted = False
        st.experimental_rerun()

st.markdown("---")
st.markdown("© 2023 Quiz sobre Programas de Gerenciamento de Antimicrobianos")
