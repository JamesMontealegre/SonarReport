# Microservicios Backend para el Poyecto ABCall

## Descripción
Este repositorio contiene el backend del proyecto final de la maestría en ingeniería de software. El backend está desarrollado en Python y sigue una arquitectura de microservicios. Cada microservicio se encarga de una parte específica del sistema y está diseñado para ser escalable, mantenible y testeable.

### Estructura del Proyecto
La estructura del repositorio es la siguiente:

```
backend-abcall/
├── microservices/                  # Contiene todos los microservicios
│   ├── auth/                       # Microservicio de Autenticación y Autorización
│   ├── user/                       # Microservicio de Gestión de Clientes y Usuarios
│   └── ...                         # Otros microservicios según sea necesario
├── config/                         # Configuraciones globales para diferentes entornos
├── docker-compose.yml              # Archivo Docker Compose para ejecutar todos los servicios
├── README.md                       # Este archivo
├── Makefile                        # Archivo make para simplificar comandos
├── .pre-commit-config.yaml         # Archivo de configuración para pre-commit hooks
├── .gitignore                      # Archivo de configuración para ignorar archivos/directorios en git
└── requirements.txt                # Dependencias compartidas del proyecto

```


### Descripción de los Microservicios
Cada microservicio tiene su propio directorio dentro de `microservices/` y sigue la siguiente estructura:

- `src/`: Contiene el código principal del microservicio, como:
  - `routes.py`: Define las rutas o endpoints de la API.
  - `services.py`: Contiene la lógica de negocio.
  - `events.py`: Define eventos (async) o señales de la base de datos.
  - `db.py`: Configuración de la base de datos.
  - `serializers.py`: Serializadores para validar y transformar datos de las solicitudes y respuestas.
  - `models/`: Contiene los modelos de base de datos del microservicio.
  - `commands/`: Contiene comando útiles para la ejecución del microservicio.
  - `fixtures/`: Contiene datos de prueba para el microservicio.
  - `common/`: Contiene código común a todos los microservicios.
- `tests/`: Tests unitarios e integrales específicos del microservicio.
- `app.py`: Inicializa el microservicio.
- `Dockerfile`: Configuración Docker para desplegar el microservicio.
- `requirements.txt`: Dependencias específicas del microservicio.
- `pytest.ini`: Configuración de pytest.
- `.coveragec`: Configuración del coverage.
- `README.md`: Documentación del microservicio.
### Cómo Ejecutar el Proyecto

#### Requisitos Previos
- Python 3.8+
- Docker
- Docker Compose

#### Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/MISW-Basinglo/abcall-backend.git abcall-backend
   cd abcall-backend
   ```

# Pre-commit Hooks
Usamos pre-commit para asegurar la calidad del código y la consistencia antes de realizar commits. Corre el siguiente comando para instalar los hooks de pre-commit:
```bash
make git_hooks
```

# Guía de Contribución
Sigue las guías de estilo PEP 8.
Asegúrate de que todos los cambios en el código tengan tests correspondientes.
Escribe mensajes de commit significativos, usando el estándar de [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/).

Adicionalmente, se debe tener en cuenta que en este repositorio se trabaja con el flujo de trabajo GitFlow. Por lo tanto, se deben seguir las siguientes reglas:
- La rama `main` es la rama de producción.
- La rama `develop` es la rama de desarrollo.
- Las ramas de feature se crean a partir de `develop` y se fusionan en `develop`.
- Las ramas de release se crean a partir de `develop` y se fusionan en `main` y `develop`.
- Las ramas de hotfix se crean a partir de `main` y se fusionan en `main` y `develop`.
- Las ramas de bugfix se crean a partir de `develop` y se fusionan en `develop`.
- Las ramas de refactor se crean a partir de `develop` y se fusionan en `develop`.
- Las ramas de docs se crean a partir de `develop` y se fusionan en `develop`.
- Las ramas permanetes son `main` y `develop`.
- Las ramas temporales son las demás ramas.
- Las ramas temporales se eliminan después de ser fusionadas.

Para más información sobre el flujo de trabajo GitFlow, puedes consultar [este enlace](https://www.atlassian.com/es/git/tutorials/comparing-workflows/gitflow-workflow).
