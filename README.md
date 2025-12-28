📦 Microservicio de Ingesta de Pedidos

Microservicio desarrollado en FastAPI para la ingesta, validación y persistencia de pedidos provenientes de clientes externos.

La solución fue diseñada siguiendo principios de Arquitectura Limpia (Clean Architecture) y SOLID, con especial énfasis en la Inversión de Dependencias, garantizando desacoplamiento, extensibilidad y facilidad de mantenimiento.

🧠 Objetivo

Construir una API REST que permita:

Recibir pedidos de sistemas externos

Validar reglas de negocio

Persistir la información en una base de datos relacional

Generar reportes agregados por cliente

Mantenerse agnóstica al ERP de destino, permitiendo reemplazar integraciones futuras sin modificar la lógica de negocio

🏗️ Arquitectura

La solución sigue una Clean Architecture, separando claramente responsabilidades y aplicando inversión de dependencias.

src/
├── main.py                     # Entry point de la aplicación
└── app/
    ├── routers/                # Infraestructura HTTP (FastAPI)
    ├── schemas/                # DTOs / Contratos de entrada y salida (Pydantic)
    ├── services/               # Casos de uso / Lógica de negocio
    ├── domain/                 # Entidades y puertos (interfaces)
    └── infrastructure/         # Implementaciones concretas (SQLite, SQLAlchemy)

Principios aplicados

Inversión de Dependencias (DIP)

Separación de responsabilidades

Dominio independiente del framework

Infraestructura intercambiable

Código orientado a casos de uso

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

📑 Documentación de la API

Una vez levantado el servicio, la documentación interactiva está disponible en:

Swagger UI
👉 http://127.0.0.1:8000/docs

OpenAPI JSON
👉 http://127.0.0.1:8000/openapi.json

🔌 Endpoints
POST /orders

Ingesta y validación de pedidos externos.

Reglas de negocio aplicadas:

quantity > 0

price_unit >= 0

Email con formato válido

is_vip = True si el total del pedido es mayor a 300

Cálculo de arrival_date:

Cliente VIP → fecha + 3 días

Cliente no VIP → fecha + 5 días

GET /orders/report

Reporte agregado de pedidos por cliente, que retorna:

Correo del cliente

Total de órdenes

Monto total acumulado

Estado VIP

Fecha de llegada más reciente

🧪 Manejo de errores

La API diferencia claramente los tipos de error:

Errores de negocio / validación → 400 Bad Request

Recursos no encontrados → 404 Not Found

Errores de infraestructura o persistencia → 500 Internal Server Error

🧩 Decisiones de diseño

El dominio no depende de FastAPI ni de SQLAlchemy

La persistencia se abstrae mediante interfaces (puertos)

Las implementaciones concretas se inyectan mediante Dependency Injection

El microservicio puede integrarse con otro ERP o motor de persistencia sin modificar la lógica de negocio

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

## 🐳 Ejecución con Docker (Opcional)
“El Dockerfile está preparado para ejecutarse desde la raíz del proyecto como contexto de build. En mi entorno local no fue posible instalar Docker Desktop por restricciones del sistema, pero el contenedor fue diseñado siguiendo buenas prácticas y puede ejecutarse sin cambios en cualquier entorno Docker-compatible.”

El proyecto incluye un `Dockerfile` para ejecutar la aplicación de forma contenida.

### Construir imagen

```bash
docker build -t orders-ingestion-api .