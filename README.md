# 📰 Blog API - Proyecto Final

**Autor:** Bruno Lezama Méndez  
**Bootcamp:** Django Avanzado  
**Empresa:** Código Facilito

---

## 📌 Descripción del Proyecto

Este proyecto es una **API RESTful para un blog**, construida con **Django** y **Django REST Framework**, que permite gestionar publicaciones, autores, categorías y etiquetas. Fue desarrollado como parte del Bootcamp de Django Avanzado de Código Facilito.

---

## 🎯 Objetivo

El objetivo del proyecto fue aplicar conceptos avanzados de Django REST Framework, como:

- Autenticación con JWT.
- Documentación automática con `drf-spectacular`.
- Middleware personalizado.
- Buenas prácticas con servicios desacoplados.
- Tests automáticos con integración CI/CD en GitHub Actions.
- Configuración profesional con `.env`, Redis y MySQL.

---

## 🔧 Funcionalidades Principales

- CRUD completo de publicaciones (posts).
- Asociaciones con autores, categorías y etiquetas.
- Filtro de publicaciones por estado (publicadas/activas).
- Endpoint para ver los últimos 5 posts activos.
- Middleware para medir el tiempo de respuesta.
- Documentación Swagger y Redoc.
- Tests automatizados en GitHub Actions.
- Soporte para CORS y cache con Redis.

---

## 🚀 Instalación y Uso

### 1. Clona el repositorio

```bash
git clone https://github.com/tu-usuario/blog-api.git
cd blog-api

2. Crea entorno virtual y activa

python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate

3. Instala dependencias

pip install -r requirements.txt


5. Migraciones y servidor

python manage.py migrate
python manage.py runserver


Endpoints de Interés

Swagger UI: /api/schema/swagger-ui/

Redoc: /api/schema/redoc/

Últimos posts publicados: /api/posts/latest/

Login JWT: /api/token/

Refresh token: /api/token/refresh/


Retos Presentados
Configuración correcta de servicios en GitHub Actions (MySQL + Redis).

Manejo de JWT y control de tokens expirados.

Organización del código en servicios (separando lógica de negocio).

Implementación de middleware personalizado y visualización de logs.

Cache con Redis sin interferir con la lógica de DRF.

Documentación extensiva con drf-spectacular.

Autor: Bruno Lezama Méndez