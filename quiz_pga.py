import streamlit as st
import pandas as pd
from datetime import datetime

# Configuração da página
st.set_page_config(
    page_title="Quiz Interativo - Programas de Gerenciamento de Antimicrobianos",
    page_icon="💊",
    layout="centered"
)

# Título principal
st.title("Quiz Interativo - Programas de Gerenciamento de Antimicrobianos")

# Função para salvar respostas
def save_responses(responses):
    try:
        # Criar ou carregar dataframe existente
        try:
            df = pd.read_csv('respostas_quiz.csv')
        except:
            df = pd.DataFrame()
        
        # Adicionar timestamp
        responses['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Adicionar como nova linha
        df = pd.concat([df, pd.DataFrame([responses])], ignore_index=True)
        
        # Salvar
        df.to_csv('respostas_quiz.csv', index=False)
        return True
    except Exception as e:
        st.error(f"Erro ao salvar as respostas: {e}")
        return False

# Inicializar o dicionário de respostas na sessão
if 'responses' not in st.session_state:
    st.session_state.responses = {}

# Inicializar o estado de submissão
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# Formulário principal
with st.form(key='quiz_form'):
    # Questão 1
    st.subheader("1. Qual a sua instituição?")
    instituicao = st.text_input("Instituição", key="instituicao")
    st.session_state.responses['instituicao'] = instituicao
    
    # Questão 2
    st.subheader("2. Em relação aos componentes do Programa de Gerenciamento de Antimicrobianos, qual das opções abaixo NÃO se configura como intervenção descrita na diretriz da ANVISA?")
    q2_options = [
        "Formulários de Restrição de antimicrobianos, como em situações especiais de antibióticos reservados para o tratamento de bactérias multirresistentes.",
        "Substituição automática de antimicrobianos por outros de mesmo espectro.",
        "Auditoria prospectiva das prescrições de antimicrobianos com feedback aos prescritores",
        "Implementação de protocolos clínicos para síndromes infecciosas específicas"
    ]
    q2 = st.radio("Selecione uma opção", q2_options, key="q2")
    st.session_state.responses['q2'] = q2
    
    # Questão 3
    st.subheader("3. Considerando os conceitos apresentados na diretriz da ANVISA, qual afirmação melhor caracteriza a diferença entre \"Antimicrobial Stewardship\" e o Programa de Gerenciamento de Antimicrobianos (PGA)?")
    q3_options = [
        "São conceitos opostos, onde o \"Stewardship\" foca apenas na restrição de antimicrobianos, enquanto o PGA aborda apenas educação dos prescritores",
        "O \"Antimicrobial Stewardship\" refere-se ao conceito da gestão clínica do uso de antimicrobianos, por meio de uma seleção otimizada da terapia, enquanto o PGA é o conjunto estruturado de ações coordenadas/sistêmicas, que abrangem também a prevenção da resistência microbiana, e o uso custo-efetivo de recursos.",
        "O \"Antimicrobial Stewardship\" é aplicável apenas em países de língua inglesa, enquanto o PGA é o termo exclusivo para o contexto brasileiro",
        "O \"Antimicrobial Stewardship\" é uma prática exclusiva da enfermagem, enquanto o PGA é coordenado apenas por médicos infectologistas"
    ]
    q3 = st.radio("Selecione uma opção", q3_options, key="q3")
    st.session_state.responses['q3'] = q3
    
    # Questão 4
    st.subheader("4. Sobre a auditoria prospectiva com feedback em um Programa de Gerenciamento de Antimicrobianos, qual afirmação está INCORRETA?")
    q4_options = [
        "Pode ser associada com pré-autorização como estratégia complementar",
        "É mais efetiva quando realizada por profissionais treinados em doenças infecciosas",
        "Limita a liberdade clínica e deve ser aplicada apenas para antimicrobianos de alto custo",
        "Permite a reavaliação do tratamento com base em resultados microbiológicos"
    ]
    q4 = st.radio("Selecione uma opção", q4_options, key="q4")
    st.session_state.responses['q4'] = q4
    
    # Questão 5
    st.subheader("5. A equipe de enfermagem responsável pela assistência ao paciente pode iniciar as seguintes intervenções:")
    q5_options = [
        "Utilizando ou orientando a utilização das técnicas apropriadas para reduzir a contaminação de culturas no momento das coletas. Garantindo quase culturas sejam realizadas corretamente antes de iniciar o antimicrobiano.",
        "Informando se um paciente tem ou não sintomas que possam justificar a coleta de uma cultura de urina ou critérios para culturas de vigilância conforme protocolos locais.",
        "A equipe de enfermagem geralmente sabe há quanto tempo um paciente está recebendo um antimicrobiano e quando os resultados laboratoriais se tornam disponíveis, podendo desempenhar um papel fundamental no estímulo de revisão da prescrição após 2 dias de tratamento e/ou quando os resultados da cultura ficam disponíveis.",
        "Pode alertar o time do PGA ou prescritor sobre a possibilidade de mudança para antimicrobianos orais.",
        "Todas as alternativas acima."
    ]
    q5 = st.radio("Selecione uma opção", q5_options, key="q5")
    st.session_state.responses['q5'] = q5
    
    # Questão 6
    st.subheader("6. Considerando as atribuições do time gestor do PGA, assinale a alternativa que contém funções que NÃO são de sua responsabilidade direta:")
    q6_options = [
        "Definir políticas e normativas do programa",
        "Realizar o monitoramento contínuo das estratégias",
        "Revisar antimicrobianos de pacientes com antimicrobianos de uso restrito em até 72h",
        "Propor melhorias para o programa",
        "Discutir o alcance das metas pactuadas"
    ]
    q6 = st.radio("Selecione uma opção", q6_options, key="q6")
    st.session_state.responses['q6'] = q6
    
    # Questão 7
    st.subheader("7. Relacione os componentes essenciais do Programa de Gerenciamento de Antimicrobianos (PGA) listados na COLUNA I com suas respectivas descrições na COLUNA II.")
    
    st.markdown("""
    **COLUNA I**
    - Componente 1: Apoio das Lideranças
    - Componente 2: Definição de Responsabilidades
    - Componente 3: Educação
    - Componente 4: Ações para Melhorar o Uso de Antimicrobianos
    - Componente 5: Monitoramento
    - Componente 6: Divulgação dos Resultados

    **COLUNA II**
    ( ) Avaliar o impacto das intervenções do programa, por meio de indicadores próprios, e outros resultados importantes, além de identificar potenciais pontos de melhoria.

    ( ) Promover ações de treinamento e capacitação para os profissionais da instituição e pacientes sobre os temas "resistência microbiana aos antimicrobianos" e "uso de antimicrobianos".

    ( ) Implementar intervenções para melhorar o uso de antimicrobianos como, por exemplo, a auditoria prospectiva e feedback ou a pré-autorização.

    ( ) Garantir recursos humanos, financeiros e de tecnologia da informação para o programa.

    ( ) Nomear os componentes dos times do programa e definir seus líderes e funções específicas.

    ( ) Relatar regularmente informações sobre o uso de antimicrobianos e resistência microbiana aos antimicrobianos aos profissionais e às lideranças da instituição.
    """)
    
    q7_options = [
        "5, 3, 4, 1, 2, 6",
        "6, 3, 4, 1, 2, 5",
        "5, 3, 4, 2, 1, 6",
        "5, 4, 3, 1, 2, 6",
        "6, 4, 3, 1, 2, 5"
    ]
    q7 = st.radio("Selecione a sequência correta", q7_options, key="q7")
    st.session_state.responses['q7'] = q7
    
    # Questão 8
    st.subheader("8. No contexto das intervenções guiadas pela farmácia no Programa de Gerenciamento de Antimicrobianos (PGA), a terapia sequencial refere-se a:")
    q8_options = [
        "Substituição de um antimicrobiano por outro com mesmo espectro de ação",
        "Aumento gradual da dose do antimicrobiano conforme resposta clínica",
        "Conversão da via intravenosa para oral em situações apropriadas",
        "Alternância de diferentes classes de antimicrobianos para evitar resistência",
        "Administração de dois antimicrobianos em sequência ao longo do dia"
    ]
    q8 = st.radio("Selecione uma opção", q8_options, key="q8")
    st.session_state.responses['q8'] = q8
    
    # Questão 9
    st.subheader("9. Em relação à otimização da dose de antimicrobianos, qual das seguintes intervenções NÃO é considerada uma ação da farmácia no PGA?")
    q9_options = [
        "Administração de infusão prolongada de beta-lactâmicos para pacientes criticamente enfermos",
        "Ajuste posológico conforme características farmacocinéticas e farmacodinâmicas do medicamento",
        "Adaptação da dose conforme características clínicas do paciente, como peso e função renal",
        "Definição do diagnóstico da infecção e escolha do antimicrobiano mais apropriado",
        "Otimização da forma de preparo, incluindo reconstituição e diluição adequadas"
    ]
    q9 = st.radio("Selecione uma opção", q9_options, key="q9")
    st.session_state.responses['q9'] = q9
    
    # Questão 10
    st.subheader("10. Considerando as perguntas norteadoras abaixo:")
    st.markdown("""
    1. Na sua experiência ou percepção, quais as principais desafios para implementar um Programa de Gerenciamento de Antimicrobianos efetivo em uma instituição de saúde brasileira? Como esses desafios poderiam ser superados?

    2. Como o PGA poderia ser melhor integrado com outros programas institucionais, como o Programa de Prevenção e Controle de Infecções (PPCI), Núcleo de Segurança do Paciente e iniciativas de qualidade assistencial? Quais seriam os benefícios dessa integração?

    3. Como promover o engajamento efetivo dos diferentes profissionais de saúde (médicos, enfermeiros, farmacêuticos, microbiologistas) no PGA? Quais estratégias poderiam ser utilizadas para superar resistências à mudança de práticas de prescrição e uso de antimicrobianos?
    """)
    
    q10 = st.text_area("Selecione um recorte para abordar em texto de até 2000 caracteres e cole abaixo antes de enviar:", height=200, key="q10", max_chars=2000)
    st.session_state.responses['q10'] = q10
    
    # Botão de envio
    submit_button = st.form_submit_button(label='Enviar Respostas')
    
    if submit_button:
        # Verificar respostas obrigatórias
        required_fields = ['q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9']
        missing_fields = [field for field in required_fields if not st.session_state.responses.get(field)]
        
        if missing_fields:
            st.error("Por favor, responda todas as questões obrigatórias (questões 2-9).")
        else:
            # Salvar respostas
            if save_responses(st.session_state.responses):
                st.session_state.submitted = True
                st.success("Respostas enviadas com sucesso!")

# Exibir mensagem após submissão bem-sucedida
if st.session_state.submitted:
    st.balloons()
    st.write("Obrigado por participar do Quiz sobre Programas de Gerenciamento de Antimicrobianos!")
    
    if st.button("Iniciar Novo Quiz"):
        # Resetar estado
        st.session_state.responses = {}
        st.session_state.submitted = False
        st.experimental_rerun()

# Rodapé
st.markdown("---")
st.markdown("© 2023 Quiz sobre Programas de Gerenciamento de Antimicrobianos")
