import seaborn as sns
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
import streamlit as st
import pandas as pd
import numpy as np
import pickle


import urllib.request
import pickle

# Descargar el archivo svm_hp.pkl desde GitHub
url = 'https://github.com/Madx-123/Madx123/raw/main/svm_hp.pkl'
filename = 'svm_hp.pkl'
urllib.request.urlretrieve(url, filename)

# Cargar el modelo
model = pickle.load(open(filename, 'rb'))


# Configuración de la página de Streamlit
st.set_page_config(
    page_title="Predicción del Autismo usando Machine Learning",
    page_icon="https://i0.wp.com/www.wi6labs.com/wp-content/uploads/2019/12/Machine-learning-logo-1.png?ssl=1",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados para darle color y estructura
st.markdown("""
    <style>
        body {
            background-color: #FFFFFF;  /* Fondo blanco */
        }
        .main { background-color: #FFFFFF; color: #333333; } /* Texto en color gris oscuro */
        .css-1lcbmhc { background-color: #8e24aa !important; color: #ffffff; } /* Barra lateral con fondo morado */
        .main-title {
            color: #8e24aa; 
            font-size: 50px; 
            font-weight: bold; 
            text-align: center;
            margin-bottom: 15px;
        }
        .formulario-title {
            font-size: 50px;
            color: #8e24aa;
            text-align: center;
            margin-top: 20px;
        }
        h2, h3, .subheader-title { 
            color: #8e24aa; 
            font-weight: bold; 
            font-size: 32px; 
        }
        .stButton > button { 
            color: #ffffff; 
            background-color: #8e24aa;
            border-radius: 5px;
            font-size: 18px;
        }
        .stImage {
            display: flex;
            justify-content: center;
        }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        .question-label {
            font-size: 20px; /* Un poco más grande */
            font-weight: bold;
            color: #FFFFFF; /* Color blanco */
            margin-bottom: -10px; /* Eliminar espacio extra entre pregunta y respuesta */
        }
        .stRadio > div > label {
            font-size: 18px; /* Aumentar tamaño de las opciones de respuesta */
            color: #333333; /* Color oscuro para las opciones */
        }
    </style>
""", unsafe_allow_html=True)

# Barra lateral de navegación
with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=["Inicio", "Medidas de Diagnóstico", "Evaluar Datos", "Acerca de Nosotros", "Cómo Funciona"],
        icons=["house", "clipboard-check", "cloud-upload", "people", "question-circle"],
        menu_icon="cast",
        default_index=0
    )



# Función principal de cada sección
def main_content():
    if selected == "Inicio":
        st.markdown('<h1 class="main-title">Predicción del Autismo usando Machine Learning</h1>', unsafe_allow_html=True)
        st.markdown(
            """
            <div class="stImage">
                <img src="https://img.freepik.com/fotos-premium/nino-autista-rompecabezas-conciencia-publica-sobre-trastorno-espectro-autista-ia-generativa_922357-2132.jpg" width="600">
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('<h2 class="subheader-title">¿Qué es el Autismo?</h2>', unsafe_allow_html=True)
        st.write(""" 
        El Trastorno del Espectro Autista (TEA) es un conjunto de afecciones del desarrollo del cerebro que afectan la forma en que una persona percibe e interactúa con el mundo. 
        El TEA es conocido por dificultades en la interacción social, patrones de comportamiento repetitivos y comunicación limitada. 
        El diagnóstico temprano y la intervención adecuada son cruciales para mejorar el pronóstico y la calidad de vida de las personas con autismo.
        """)
        st.markdown('<h2 class="subheader-title">¿Cómo apoya el Machine Learning en la detección de enfermedades?</h2>', unsafe_allow_html=True)
        st.write(""" 
        El Machine Learning (ML) se utiliza para analizar grandes cantidades de datos médicos y encontrar patrones complejos que a menudo son difíciles de detectar mediante métodos convencionales. 
        En el caso del autismo, los modelos de ML pueden ayudar a identificar signos tempranos del trastorno mediante la evaluación de respuestas a ciertas preguntas o comportamientos observables, permitiendo un diagnóstico rápido y eficaz.
        """)

    elif selected == "Medidas de Diagnóstico":
        st.markdown('<h1 class="main-title">Predicción de Autismo basada en medidas diagnósticas</h1>', unsafe_allow_html=True)
        
        # Imagen antes de la palabra "Formulario"
        st.markdown("""
            <div class="stImage">
                <img src="https://www.teknon.es/idcsalud-client/cm/images?locale=es_ES&idMmedia=662761" width="600">
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<h1 class="formulario-title">Formulario</h1>', unsafe_allow_html=True)

        # Función para obtener la entrada del usuario
        def get_user_input():
            questions = [
                '¿Hablas muy poco y das respuestas no relacionadas con la pregunta?',
                '¿No respondes a tu nombre o evitas el contacto visual?',
                '¿No participas en juegos de simulación con otros niños?',
                '¿Tienes dificultades para comprender los sentimientos de otras personas?',
                '¿Te molestas fácilmente por pequeños cambios?',
                '¿Tienes intereses obsesivos?',
                '¿Eres hiper o hiposensible a los olores, sabores o tacto?',
                '¿Tienes dificultades para socializar con otros niños?',
                '¿Evitas el contacto físico?',
                '¿Muestras poca paciencia ante situaciones peligrosas?',
                '¿Alguna vez o actualmente sufre de ictericia?'
            ]
            answers = []
            for i, q in enumerate(questions[:10], 1):
                st.markdown(f'<p class="question-label">{i}. {q}</p>', unsafe_allow_html=True)
                answers.append(st.radio("", ['Sí', 'No'], key=f"question_{i}"))
            
            st.markdown('<p class="question-label">11. ¿Alguna vez o actualmente sufre de ictericia?</p>', unsafe_allow_html=True)
            st.caption("La ictericia es una condición en la que la piel y los ojos adquieren una coloración amarilla, generalmente debido a problemas hepáticos.")
            answers.append(st.radio("", ['Sí', 'No'], key="question_11"))
            age = st.slider('Edad', 0, 100, 20)
            
            user_data = {f'A{i+1}_Score': 1 if answers[i] == 'Sí' else 0 for i in range(10)}
            user_data.update({'age': age, 'jundice': 1 if answers[10] == 'Sí' else 0})
            features = pd.DataFrame(user_data, index=[0])
            return features

        user_input = get_user_input()

        # Evaluar predicción cuando el usuario hace clic
        if st.button("Evaluar"):
            prediction = model.predict(user_input)
            probability = model.predict_proba(user_input)[0]

            st.subheader('Resultado')
            classification_result = "Autismo Detectado" if prediction == 1 else "No se Detectó Autismo"
            st.success(classification_result, icon="✅")

            st.subheader('Exactitud')
            st.success(f"{int(probability[prediction] * 100)}%", icon="🔍")

            # Nota de consulta con profesional
            st.warning("Nota: Este resultado no constituye un diagnóstico médico. Consulte a un profesional de salud para evaluación adicional.")

            # Esquema resumen de respuestas
            answer_counts = user_input.iloc[0][:-2].value_counts()
            st.write("**Esquema de respuestas ingresadas**")
            fig, ax = plt.subplots()
            sns.barplot(x=answer_counts.index.map({1: 'Sí', 0: 'No'}), y=answer_counts.values, palette="viridis", ax=ax)
            ax.set(title="Resumen de Respuestas", xlabel="Respuesta", ylabel="Cantidad")
            st.pyplot(fig)

    elif selected == "Evaluar Datos":
        st.header("Evaluar Datos CSV")
        uploaded_file = st.file_uploader("Sube tu archivo CSV para evaluar", type=["csv"])
        if uploaded_file:
            df = pd.read_csv(uploaded_file)
            st.write("Datos cargados:", df.head())
            st.write("Dimensiones del archivo:", df.shape)

    elif selected == "Acerca de Nosotros":
        st.header("Acerca de Nosotros")
        st.write("""
        Somos estudiantes de la Universidad Nacional del Santa, y esta aplicación es parte de nuestro proyecto para aplicar algoritmos de machine learning 
        en la detección temprana de autismo.
        """)
        st.write("""
        Este proyecto está dedicado a todas las familias y personas que trabajan por la inclusión y la mejora en la calidad de vida de quienes tienen autismo.
        """)
        st.markdown("""
            <div class="stImage" style="margin-top: 20px;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/1/1a/Universidad_Nacional_del_Santa_Logo.png" width="300" style="margin-right: 20px;">
                <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTuJeGsr5z7C0kqsE6EyVQmM2Vid7-pdv_aBw&s" width="150">
            </div>
        """, unsafe_allow_html=True)

    elif selected == "Cómo Funciona":
        st.header("Cómo Funciona la Aplicación")
        st.write("""
        Esta aplicación utiliza un modelo SVM (Support Vector Machine) para predecir la probabilidad de que una persona presente autismo, en función de sus respuestas a una serie de preguntas.
        Los usuarios responden preguntas sobre comportamientos, y el modelo evalúa el riesgo de autismo.

        El modelo procesará los datos proporcionados y generará un resultado basado en un análisis estadístico y patrones detectados previamente. 
        **Advertencia:** Esta herramienta es solo informativa y no sustituye un diagnóstico profesional. Se recomienda realizar una consulta profesional para obtener resultados oficiales y completos.
        """)
        
        # Imagen del modelo SVM
        st.markdown("""
            <div class="stImage">
                <img src="https://spotintelligence.com/wp-content/uploads/2024/05/support-vector-machine-svm.jpg" width="600">
            </div>
        """, unsafe_allow_html=True)

# Ejecutar la función principal
main_content()
