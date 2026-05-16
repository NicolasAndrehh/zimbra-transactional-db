🚀 Instrucciones de Configuración e Instalación
Para trabajar en este repositorio localmente, sigue estos pasos en orden:

1. Clonar el Repositorio
Bash
git clone [https://github.com/TU-USUARIO/zimbra-transactional-db.git](https://github.com/TU-USUARIO/zimbra-transactional-db.git)
cd zimbra-transactional-db
2. Configurar la Base de Datos (MySQL)
Abre tu gestor de base de datos local (XAMPP, MySQL Workbench, WAMP, etc.).

Asegúrate de que el servicio de MySQL esté corriendo.

Importa y ejecuta el script ubicado en bd/schema.sql para crear la base de datos y todas sus tablas estructuradas.

3. Configurar y Ejecutar el Backend (Python + Flask)
Abre una terminal en la raíz del proyecto y ejecuta:

Bash
cd backend
# 1. Crear el entorno virtual
python -m venv venv

# 2. Activar el entorno virtual (En Windows)
.\\venv\\Scripts\\activate

# 3. Instalar las dependencias necesarias
pip install -r requirements.txt

# 4. Iniciar el servidor de desarrollo
python app.py
El backend correrá en: http://localhost:5000

4. Configurar y Ejecutar el Frontend (React + Vite)
Abre otra terminal diferente en la raíz del proyecto y ejecuta:

Bash
cd frontend
# 1. Instalar los paquetes de Node.js (Recrea node_modules)
npm install

# 2. Iniciar el servidor frontend de Vite
npm run dev
El frontend correrá en: http://localhost:5173

🔒 Buenas Prácticas del Repositorio
¡NUNCA subas node_modules/ ni venv/! Ya están configurados en el .gitignore. Si agregas una nueva dependencia en Python, recuerda actualizar el archivo ejecutando pip freeze > requirements.txt dentro de la carpeta backend con el entorno activo.