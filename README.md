# Proyecto Django con Django Rest Framework (DRF)

Este proyecto utiliza Django junto con Django Rest Framework (DRF). Está dividido en tres aplicaciones principales: usuario, guion y actor. Utiliza la base de datos SQLite por defecto.

## Configuración

1. Clona este repositorio en tu máquina local.
2. Asegúrate de tener Python y Django instalados.
3. Instala los requisitos del proyecto ejecutando `pip install -r requirements.txt`.
4. Realiza las migraciones de la base de datos ejecutando `python manage.py migrate`.

## Correr el Servidor

Para correr el servidor de desarrollo de Django, ejecuta el siguiente comando:
python manage.py runserver

## Acceso al Admin

Se han creado archivos de administración para permitir la gestión de las tablas de la base de datos desde la ruta `/admin`. Para acceder, primero necesitas crear un superusuario ejecutando el siguiente comando:
`python manage.py createsuperuser`

## Modelos y Relaciones

### Usuario

- **nombre**: Nombre del usuario.
- **correo**: Correo electrónico del usuario (único).
- **contrasena**: Contraseña del usuario (cifrada automáticamente).
- **rol**: Rol del usuario, puede ser "Guionista" o "Usuario".
- **guiones_escritos**: Relación One-to-Many con Guion. Cada usuario puede escribir varios guiones.

### Guion

- **titulo**: Título del guion.
- **genero**: Género del guion.
- **usuario**: Relación ForeignKey con Usuario. Cada guion pertenece a un usuario.
- **descripcion**: Descripción del guion.
- **fecha_creacion**: Fecha de creación del guion.
- **escenas**: Relación One-to-Many con Escena. Cada guion puede tener varias escenas.
- **historial_cambios**: Relación One-to-Many con HistorialCambios. Cada guion puede tener varios registros de historial de cambios.

### Escena

- **guion**: Relación ForeignKey con Guion. Cada escena pertenece a un guion.
- **numero_escena**: Número de la escena.
- **descripcion**: Descripción de la escena.
- **actores**: Relación Many-to-Many con Actor. Varios actores pueden aparecer en una escena.

### Dialogo

- **escena**: Relación ForeignKey con Escena. Cada diálogo pertenece a una escena.
- **texto**: Texto del diálogo.
- **actor**: Relación ForeignKey con Actor. Cada diálogo puede ser dicho por un actor.

### HistorialCambios

- **guion**: Relación ForeignKey con Guion. Cada registro de historial de cambios pertenece a un guion.
- **fecha**: Fecha y hora del registro.
- **usuario**: Relación ForeignKey con Usuario. Cada registro de historial de cambios está asociado a un usuario.

### Actor

- **nombre**: Nombre del actor.
- **edad**: Edad del actor.
- **genero**: Género del actor.
- **escenas**: Relación Many-to-Many con Escena. Un actor puede aparecer en varias escenas.
- **poses**: Relación One-to-Many con Pose. Cada actor puede tener varias poses.
- **ubicaciones**: Relación One-to-Many con Ubicacion. Cada actor puede tener varias ubicaciones.

### Pose

- **nombre**: Nombre de la pose.
- **descripcion**: Descripción de la pose.
- **actor**: Relación ForeignKey con Actor. Cada pose pertenece a un actor.

### Ubicacion

- **actor**: Relación ForeignKey con Actor. Cada ubicación pertenece a un actor.
- **coordenada_x**: Coordenada X de la ubicación.
- **coordenada_y**: Coordenada Y de la ubicación.
- **coordenada_z**: Coordenada Z de la ubicación.
- **rotacion_x**: Rotación X de la ubicación.
- **rotacion_y**: Rotación Y de la ubicación.
- **rotacion_z**: Rotación Z de la ubicación.

### Endpoints

#### Usuarios

- Lista de usuarios:
  - `GET /api/usuarios/`
  - `POST /api/usuarios/`
  - `PUT /api/usuarios/<id>/`
  - `DELETE /api/usuarios/<id>/`

#### Guiones

- Lista de guiones:
  - `GET /api/guiones/`
  - `POST /api/guiones/`
  - `PUT /api/guiones/<id>/`
  - `DELETE /api/guiones/<id>/`

#### Dialogos

- Lista de diálogos:
  - `GET /api/dialogos/`
  - `POST /api/dialogos/`
  - `PUT /api/dialogos/<id>/`
  - `DELETE /api/dialogos/<id>/`

#### Escenas

- Lista de escenas:
  - `GET /api/escenas/`
  - `POST /api/escenas/`
  - `PUT /api/escenas/<id>/`
  - `DELETE /api/escenas/<id>/`

#### Historial de Cambios

- Lista de historial de cambios:
  - `GET /api/historial_cambios/`
  - `POST /api/historial_cambios/`
  - `PUT /api/historial_cambios/<id>/`
  - `DELETE /api/historial_cambios/<id>/`

#### Actores

- Lista de actores:
  - `GET /api/actores/`
  - `POST /api/actores/`
  - `PUT /api/actores/<id>/`
  - `DELETE /api/actores/<id>/`

#### Poses

- Lista de poses:
  - `GET /api/poses/`
  - `POST /api/poses/`
  - `PUT /api/poses/<id>/`
  - `DELETE /api/poses/<id>/`

#### Ubicaciones

- Lista de ubicaciones:
  - `GET /api/ubicaciones/`
  - `POST /api/ubicaciones/`
  - `PUT /api/ubicaciones/<id>/`
  - `DELETE /api/ubicaciones/<id>/`

# Nota Importante

- Se encontraron dificultades al intentar modificar el usuario predeterminado proporcionado por DRF Auth, lo que causó problemas con la autenticación en el proyecto.
- Además, debido a limitaciones de tiempo, no se pudo completar el desarrollo del frontend utilizando React ni implementar las solicitudes HTTP a los endpoints del backend.
