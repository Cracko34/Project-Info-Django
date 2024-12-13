
# Project-Info-Django
### Organizacion del directorio 

# Estructura del Proyecto

```plaintext
Project-Info-Django/
├── app/                            # Carpeta de la aplicación Django
│   ├── migrations/                 # Carpeta para las migraciones de la base de datos
│   ├── __init__.py                 # Indica que esta carpeta es un paquete Python
│   ├── admin.py                    # Configuración del panel de administración
│   ├── apps.py                     # Configuración de la aplicación
│   ├── forms.py                    # Formularios de la aplicación
│   ├── models.py                   # Modelos de la base de datos
│   ├── tests.py                    # Pruebas unitarias
│   ├── urls.py                     # Rutas de la aplicación
│   ├── views.py                    # Vistas de la aplicación
│   └── templates/                  # Carpeta para las plantillas HTML
│       ├── login.html              # Plantilla de inicio de sesión
│       ├── home.html               # Plantilla de la página de inicio
│       ├── notes.html              # Plantilla para mostrar notas
│       ├── asistencia.html         # Plantilla para mostrar asistencia
│       ├── estadisticas.html       # Plantilla para mostrar estadísticas
│       └── carga_archivo.html      # Plantilla para cargar archivos
├── static/                         # Carpeta para archivos estáticos (CSS, JS, imágenes)
│   └── css/
│       └── styles.css              # Archivo CSS para estilos
├── proyecto/                       # Carpeta del proyecto Django
│   ├── __init__.py                 # Indica que esta carpeta es un paquete Python
│   ├── settings.py                 # Configuración del proyecto
│   ├── urls.py                     # Rutas del proyecto
│   ├── wsgi.py                     # Configuración para WSGI
│   └── asgi.py                     # Configuración para ASGI
├── media/                          # Carpeta para archivos multimedia (subidos por usuarios)
├── db.sqlite3                      # Base de datos SQLite (si usas SQLite)
├── requirements.txt                # Archivo con las dependencias del proyecto
├── manage.py                       # Script para gestionar el proyecto Django
├── .gitignore                      # Archivos y carpetas que Git debe ignorar
└── README.md                       # Documentación del proyecto
