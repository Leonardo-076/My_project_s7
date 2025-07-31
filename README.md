Proyecto: Análisis de Anuncios de Coches (US)

Una aplicación web interactiva desarrollada con Streamlit para explorar un conjunto de datos de anuncios de coches en Estados Unidos (vehicles_us.csv). Permite a emprendedores y analistas filtrar, visualizar y analizar dinámicamente las características y precios de vehículos usados.

🔍 Funcionalidades Principales

Filtros interactivos (barra lateral):

Rango de año de fabricación (model_year).

Condición del vehículo (condition).

Rango de precio (price).

Métricas rápidas:

Total de anuncios.

Precio promedio.

Kilometraje promedio.

Visualizaciones:

Scatter plot de Precio vs. Año de Fabricación.

Botón para generar Histograma de precios bajo demanda.

Botón para generar Scatter plot de Precio vs. Kilometraje.

Exploratory Data Analysis (EDA):

Notebook notebooks/EDA.ipynb con análisis exploratorio básico usando Plotly Express:

Histogramas de precios y kilometraje.

Box plots de precio por condición o combustible.

Gráficos de barras y matriz de correlación.

🗂 Estructura del Proyecto

My_project_s7/
├── app.py               # Script principal de Streamlit
├── vehicles_us.csv      # Dataset de anuncios de coches
├── notebooks/
│   └── EDA.ipynb        # Notebook de EDA con visualizaciones
├── validate.py          # Script para validar estructura de archivos
├── requirements.txt     # Dependencias del proyecto
└── README.md            # Documentación y guías de uso

⚙️ Requisitos e Instalación

Clonar el repositorio:

git clone https://github.com/Leonardo-076/My_project_s7.git
cd My_project_s7

Crear y activar entorno virtual:

python -m venv vehicles_env
# Windows PowerShell
.\vehicles_env\Scripts\Activate.ps1
# macOS/Linux
source vehicles_env/bin/activate

Instalar dependencias:

pip install -r requirements.txt

🚀 Ejecución de la Aplicación

streamlit run app.py

Luego abre en tu navegador:

http://localhost:8501

📊 Exploratory Data Analysis (EDA)

Abre el notebook en VS Code u otro entorno Jupyter:

# Desde la raíz del proyecto
jupyter lab notebooks/EDA.ipynb

☁️ Despliegue en Streamlit Cloud

Puedes publicar tu app gratuitamente en Streamlit Community Cloud:

Regístrate y autoriza GitHub.

Crea una nueva app apuntando a Leonardo-076/My_project_s7, rama main.

Despliega y comparte la URL pública.

📝 Autor

Leo (Leonardo-076)

Proyecto desarrollado como parte del bootcamp de análisis de datos
