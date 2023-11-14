# Real Estate API

Este proyecto es una API de bienes raíces diseñada para proporcionar información sobre propiedades en los Estados Unidos. Utiliza Python 3.11.5, FastAPI para el desarrollo del backend y MongoDB como base de datos. Además, se ha configurado un entorno de desarrollo utilizando Docker y Docker Compose.

### Prerrequisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente:
- [Python 3.11.5](https://www.python.org/downloads/)
- [MongoDB](https://www.mongodb.com/try/download/community)
- [Docker](https://docs.docker.com/get-docker/) (opcional, si tu proyecto está dockerizado)


## Estructura del Proyecto

El proyecto se organiza de la siguiente manera:

```
real_state_company/
├── app/
│   ├── main.py
│   ├── api/
│   │   ├── endpoints/
│   │   │   ├── property.py
│   │   └── ...
│   ├── core/
│   │   ├── config.py
│   │   ├── exceptions.py
│   │   ├── logger.py
│   │   └── validations.py
│   ├── db/
│   │   └── mongodb.py
│   ├── images/
│   ├── models/
│   │   ├── owner.py
│   │   ├── property.py
│   │   ├── property_image.py
│   │   ├── property_trace.py
│   │   └── py_object_id.py
│   ├── repositories/
│   │   ├── owner.py
│   │   ├── property.py
│   │   ├── property_image.py
│   │   └── property_trace.py
│   ├── schemas/
│   │   ├── owner.py
│   │   ├── property.py
│   │   ├── property_image.py
│   │   └── property_trace.py
│   ├── services/
│   │   └── property_service.py
│   └── util/
│       └── file_utils.py
├── tests/
│   ├── integration/
│       └── ...
│   └── unit/
│       ├── test_property_api.py
│       └── ...
├── .env_example
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

La estructura del proyecto sigue las mejores prácticas de organización de código:

- `app/`: Contiene el código fuente de la aplicación FastAPI.
- `tests/`: Aquí se encuentran los casos de prueba unitarios.
- `docker-compose.yml`: Define la configuración de Docker Compose para el proyecto.
- `Dockerfile`: Define la configuración del contenedor Docker para la aplicación.
- `requirements.txt`: Lista las dependencias de Python necesarias para el proyecto.

## Configuración del entorno de desarrollo

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/JorgeEduardo17/real_state_company.git
   
   cd real-estate-api
   
2. Construir imagen, intalacion de dependencias (requirements.txt):
   ```bash
   docker-compose build

3. Inicia el entorno de desarrollo con Docker Compose:
   ```bash
   docker-compose up -d
   
   Esto configurará un contenedor de MongoDB y ejecutará la aplicación FastAPI en un servidor local.


4. Asegurate de tener variables de entorno (.env):
   ```bash
   # General
   ENVIRONMENT=development
   APP_NAME=real_state_company
   IMAGES_DIRECTORY="app/images"
   
   # Database
   MONGODB_URI=mongodb://db:27017/realStateCompany
   MONGODB_TEST_URI=mongodb://localhost:27017/realStateCompanyTest
   DATABASE_PORT=27017
   
   Estas variables son un ejemplo para correr en un ambiente local.


5. Accede a la documentación de la API en tu navegador web:
   http://localhost:8000/docs


## Funcionalidades

### Crear un Edificio de Propiedades
Puedes crear un nuevo edificio de propiedades utilizando la siguiente ruta:
   
``POST /buildings/``

Envía los datos del edificio en el cuerpo de la solicitud en formato JSON.


### Agregar Imágenes a una Propiedad
Puedes agregar imágenes a una propiedad existente utilizando la siguiente ruta:
   
``POST /properties/{property_id}/images/``

Envía la imagen como un archivo en la solicitud.


### Cambiar el Precio de una Propiedad
Puedes cambiar el precio de una propiedad utilizando la siguiente ruta:
   
``PUT /properties/{property_id}/price/``

Envía el nuevo precio en el cuerpo de la solicitud en formato JSON.

## Consideraciones 
Este proyecto se hizo según los siguientes criterios:

- **Arquitectura**: La estructura del proyecto y la organización del código deben seguir las mejores prácticas.
- **Documentación del Código**: El código debe estar bien documentado, incluyendo comentarios explicativos.
- **Mejores Prácticas**: Deben seguirse las mejores prácticas de desarrollo de Python y FastAPI.
- **Rendimiento**: La aplicación debe ser eficiente y responder de manera rápida a las solicitudes.
- **Pruebas Unitarias**: Se deben incluir pruebas unitarias para garantizar la calidad del código.

## Contribuciones

Si deseas contribuir a este proyecto, no dudes en enviar un pull request. Estamos abiertos a sugerencias y mejoras.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para obtener más detalles.

