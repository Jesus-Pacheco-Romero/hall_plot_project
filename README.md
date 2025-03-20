# 📊 Hall Plot - Análisis de Inyección

Esta aplicación en **Streamlit** permite analizar la relación entre el agua inyectada y la presión de inyección en pozos, utilizando el **Gráfico de Hall** y su derivada. Es una herramienta clave para detectar posibles problemas de taponamiento y optimizar la gestión de inyección en yacimientos petroleros.

---

## 📌 Características principales
✅ Carga y procesamiento de datos de inyección y presión.  
✅ Generación automática del **Hall Plot** con su derivada.  
✅ Filtrado dinámico por pozo inyector.  
✅ Descarga de los datos analizados en formato CSV.  
✅ Interfaz intuitiva desarrollada en **Streamlit**.  

---

## 📂 Estructura del proyecto
```
hall_plot_project/
│── app.py                      # Archivo principal de Streamlit
│── requirements.txt             # Dependencias del proyecto
│── README.md                    # Descripción del proyecto
│
├── data/                        # Carpeta para archivos CSV
│   ├── inyeccion_diaria.csv            # Archivo con datos de inyección
│   ├── data_estatica.csv          # Archivo con datos de PMP y presión de yacimiento
│
├── scripts/                     # Código modular de funciones
│   ├── __init__.py              # Permite importar módulos
│   ├── graphs.py                # Clases y funciones para gráficos
│   ├── hall_plot.py             # Clases y funciones para cálculos de Hall Plot

```

---

## 🚀 Instalación y uso

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/usuario/hall_plot_project.git
cd hall_plot_project
```

### 2️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3️⃣ Ejecutar la aplicación
```bash
streamlit run app.py
```

---

## 📈 Concepto del Hall Plot
El **Gráfico de Hall** se utiliza para evaluar el comportamiento de los pozos inyectores en sistemas de **waterflooding**. Representa la relación entre la presión acumulada de inyección y el volumen de agua inyectado. Un comportamiento lineal en el gráfico indica condiciones estables, mientras que cambios en la pendiente pueden sugerir problemas como **taponamiento del pozo** o **daño a la formación**.

La **derivada del Gráfico de Hall** ayuda a identificar cambios en la resistencia al flujo, permitiendo detectar anomalías con mayor sensibilidad.

---

## 📥 Descarga de datos
Una vez generados los análisis, los datos pueden ser descargados en formato **CSV** para su posterior revisión.

---

## 📌 Contacto y soporte
Si tienes preguntas o sugerencias, puedes contactarme en **LinkedIn** o abrir un **issue** en el repositorio.

🚀 **Desarrollado por** [Jesús Pacheco](https://www.linkedin.com/in/jesus-pacheco/)

