📦 Microservicio de Ingesta de Pedidos

Microservicio desarrollado en FastAPI para la ingesta, validación y persistencia de pedidos de clientes externos.
La solución está diseñada bajo principios de Arquitectura Limpia y SOLID, garantizando desacoplamiento, extensibilidad y facilidad de mantenimiento.

🧠 Objetivo

Construir una API REST que:

Reciba pedidos externos

Valide reglas de negocio

Persista la información en una base de datos relacional

Genere reportes agregados por cliente

Sea agnóstica al ERP de destino, permitiendo cambios futuros sin afectar la lógica de negocio

🏗️ Arquitectura

La solución sigue una Clean Architecture con inversión de dependencias:

src/
├── main.py                     # Entry point de la aplicación
└── app/
    ├── routers/                # Capa de infraestructura (HTTP)
    ├── schemas/                # DTOs (Pydantic)
    ├── services/               # Lógica de negocio
    ├── domain/                 # Entidades y puertos (interfaces)
    └── infrastructure/         # Implementaciones concretas (SQLite, ORM)

Principios aplicados

Inversión de Dependencias (DIP)

Separación de responsabilidades

Dominio independiente del framework

Infraestructura intercambiable

🚀 Tecnologías utilizadas

Python 3.12+

FastAPI

SQLAlchemy

SQLite

Pydantic

Uvicorn

📦 Instalación y Ejecución
1️⃣ Crear y activar entorno virtual
Windows (PowerShell)
py -m venv .venv
.\.venv\Scripts\Activate.ps1


Si PowerShell bloquea la activación:

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

macOS / Linux
python3 -m venv .venv
source .venv/bin/activate

2️⃣ Instalar dependencias
pip install --upgrade pip
pip install -r requirements.txt

3️⃣ Ejecutar la aplicación
python -m uvicorn main:app --reload --app-dir src

📑 Documentación API

Swagger UI:
👉 http://127.0.0.1:8000/docs

OpenAPI:
👉 http://127.0.0.1:8000/openapi.json

🔌 Endpoints
POST /orders

Ingesta y validación de pedidos externos.

Reglas de negocio:

quantity > 0

price_unit >= 0

Email válido

is_vip = True si total > 300

arrival_date:

VIP → +3 días

No VIP → +5 días

GET /orders/report

Reporte agregado de pedidos por cliente:

Total de órdenes

Monto acumulado

Estado VIP

Fecha de llegada

🧪 Manejo de errores

Errores de negocio → 400 Bad Request

Recursos no encontrados → 404 Not Found

Errores de infraestructura → 500 Internal Server Error

🧩 Decisiones de diseño

El dominio no depende de FastAPI ni SQLAlchemy

La persistencia se abstrae mediante interfaces

El servicio puede conectarse a otro ERP o base de datos sin modificar la lógica de negocio

📂 Estructura del repositorio
.
├── src/
│   ├── main.py
│   └── app/
├── odoo_module_design/
│   └── models.py
├── requirements.txt
├── README.md
├── teoria.md
└── Dockerfile (opcional)

📌 Consideraciones finales

Este proyecto fue desarrollado como prueba técnica, priorizando:

Calidad del diseño

Claridad del código

Buenas prácticas de arquitectura

Escalabilidad y mantenibilidad