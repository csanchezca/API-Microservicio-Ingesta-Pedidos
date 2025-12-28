Prueba Técnica – Fundamentos de Ingeniería

Microservicio de Ingesta de Pedidos

1. Principios SOLID – Inversión de Dependencias (DIP)

El Principio de Inversión de Dependencias (DIP) establece que los módulos de alto nivel (lógica de negocio) no deben depender de módulos de bajo nivel (infraestructura), sino que ambos deben depender de abstracciones.

En un microservicio, esto permite:

Cambiar tecnologías (base de datos, ERP, API externa) sin impactar la lógica de negocio.

Facilitar pruebas unitarias desacopladas de infraestructura.

Mantener una arquitectura extensible y mantenible.

Ejemplo aplicado en Python

Se define un puerto (interface) en el dominio:

# domain/ports.py
from abc import ABC, abstractmethod
from app.domain.entities import Order

class OrdersRepository(ABC):

    @abstractmethod
    def save(self, order: Order) -> None:
        pass


Implementación concreta en infraestructura:

# infrastructure/repositories.py
from sqlalchemy.orm import Session
from app.domain.ports import OrdersRepository

class SQLiteOrdersRepository(OrdersRepository):

    def __init__(self, db: Session):
        self.db = db

    def save(self, order: Order) -> None:
        ...


Uso en la capa de servicios:

# services/orders_service.py
from app.domain.ports import OrdersRepository

class OrdersService:

    def __init__(self, repo: OrdersRepository):
        self.repo = repo

    def create_order(self, order):
        self.repo.save(order)

Conclusión

La lógica de negocio no conoce SQLAlchemy, SQLite ni FastAPI.

El cambio de infraestructura no requiere modificar la capa de servicios.

Se cumple DIP, Clean Architecture y se facilita el testing.

2. Odoo ORM – Diferencia entre _inherit y _inherits

En Odoo existen dos mecanismos para extender modelos existentes:

_inherit – Herencia clásica (misma tabla)
class SaleOrder(models.Model):
    _inherit = "sale.order"

    x_order_number = fields.Integer()


Características:

Extiende el modelo existente

No crea nuevas tablas

Permite agregar campos, sobrescribir métodos y lógica

Cuándo usarlo:

Extensión funcional estándar

Agregar validaciones o campos

Modificar comportamiento del modelo original

📌 Es el mecanismo más utilizado en Odoo.

_inherits – Herencia por composición (tablas separadas)
class CustomOrder(models.Model):
    _name = "custom.order"
    _inherits = {"sale.order": "sale_order_id"}

    sale_order_id = fields.Many2one("sale.order", required=True)


Características:

Delegación de campos

Relación entre tablas

Mayor complejidad estructural

Cuándo usarlo:

Reutilización de modelos completos

Modelos compuestos

Separación física de datos

📌 Se usa en escenarios específicos, no como práctica general.

3. Gestión de Dependencias y Git
Manejo de dependencias en Python

Aunque requirements.txt es funcional, se recomienda mejorar:

Separación por entorno:

requirements.txt

requirements-dev.txt

Versionado explícito para evitar incompatibilidades

Uso de herramientas modernas:

pip-tools (pip-compile)

poetry o pdm para:

lockfiles reproducibles

scripts

aislamiento de dependencias

Esto mejora:

Reproducibilidad

Seguridad

Mantenibilidad del proyecto

Flujo de trabajo Git (Branching Model)

Modelo recomendado:

main: versión estable

develop: integración

feature/*: nuevas funcionalidades

fix/*: correcciones

Ejemplo:

feature/orders-ingestion
fix/duplicate-external-id

Buenas prácticas de commits

Commits pequeños y atómicos

Mensajes claros y semánticos

Convención tipo Conventional Commits

feat(api): add orders ingestion endpoint
fix(repo): handle duplicate external_id
refactor(service): extract vip calculation logic

4. Tipado y Genéricos en Python

El uso de Generic[T] y TypeVar permite construir componentes reutilizables manteniendo seguridad de tipos.

Ejemplo
from typing import TypeVar, Generic

T = TypeVar("T")

class Repository(Generic[T]):

    def save(self, entity: T) -> None:
        ...

    def get(self, id: int) -> T:
        ...

Beneficios

Mejor autocompletado

Validación estática de tipos

Reutilización sin pérdida semántica

Código más robusto y expresivo

📌 Muy útil en repositorios, servicios y capas de dominio.

5. Arquitectura – Separación entre Services y Routers

La capa de services contiene la lógica de negocio, mientras que routers pertenece a la infraestructura web.

Razones clave para mantenerlas desacopladas

La lógica de negocio no debe depender de HTTP

Permite reutilizar servicios en:

APIs

workers

procesos batch

Facilita pruebas unitarias puras

Ejemplo incorrecto ❌
from fastapi import HTTPException

Ejemplo correcto ✅

Servicio lanza un error de dominio:

raise ValidationError("Invalid order")


El router decide cómo exponerlo:

except ValidationError as e:
    raise HTTPException(status_code=422, detail=str(e))

Conclusión

Se mantiene Clean Architecture

Se reduce acoplamiento

Se mejora extensibilidad y testabilidad