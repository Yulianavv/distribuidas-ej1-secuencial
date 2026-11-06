# Ejercicio 1: Ejecución Secuencial

Simulación de un proceso secuencial y bloqueante: **Preparación artesanal de café por fases** (molienda, calentamiento de agua, extracción filtrada y servido).

---

## Requisitos
- Docker y Docker Compose (o Docker Desktop activo)

---

## Ejecución

1. Clona el repositorio y entra a la carpeta:
```bash
git clone https://github.com/tu-usuario/distribuidas-ej1-secuencial.git
cd distribuidas-ej1-secuencial
```

2. Ejecuta el contenedor con Docker Compose:
```bash
docker compose up
```

*(Opcional: Para ejecutarlo directamente con Python local sin Docker: `python 01_secuencial.py`)*

3. Para detener el contenedor al finalizar:
```bash
docker compose down
```

---

## Salida Esperada en Terminal

```text
=========================================================
 SISTEMA DE PREPARACIÓN DE CAFÉ ARTESANAL (SECUENCIAL)
=========================================================
Iniciando procesamiento secuencial de órdenes...

>>> Iniciando preparación de Orden #1: Geisha de Altura (Método: V60 Dripper)
[Orden #1] [1/4] Moliendo granos de café de especialidad...
[Orden #1]       Molienda completada (0.80s).
[Orden #1] [2/4] Calentando agua a temperatura controlada...
[Orden #1]       Agua lista a temperatura óptima (1.20s).
[Orden #1] [3/4] Ejecutando pre-infusión y extracción filtrada...
[Orden #1]       Extracción artesanal finalizada (1.50s).
[Orden #1] [4/4] Sirviendo en taza y verificando notas de cata...
[Orden #1]       Taza servida y lista para entrega (0.50s).
>>> Orden #1 (Geisha de Altura) completada en 4.00s.

>>> Iniciando preparación de Orden #2: Bourbon Rosado (Método: Aeropress)
[Orden #2] [1/4] Moliendo granos de café de especialidad...
[Orden #2]       Molienda completada (0.70s).
[Orden #2] [2/4] Calentando agua a temperatura controlada...
[Orden #2]       Agua lista a temperatura óptima (1.00s).
[Orden #2] [3/4] Ejecutando pre-infusión y extracción filtrada...
[Orden #2]       Extracción artesanal finalizada (1.30s).
[Orden #2] [4/4] Sirviendo en taza y verificando notas de cata...
[Orden #2]       Taza servida y lista para entrega (0.50s).
>>> Orden #2 (Bourbon Rosado) completada en 3.50s.

>>> Iniciando preparación de Orden #3: Típica Mejorado (Método: Prensa Francesa)
[Orden #3] [1/4] Moliendo granos de café de especialidad...
[Orden #3]       Molienda completada (0.90s).
[Orden #3] [2/4] Calentando agua a temperatura controlada...
[Orden #3]       Agua lista a temperatura óptima (1.30s).
[Orden #3] [3/4] Ejecutando pre-infusión y extracción filtrada...
[Orden #3]       Extracción artesanal finalizada (1.60s).
[Orden #3] [4/4] Sirviendo en taza y verificando notas de cata...
[Orden #3]       Taza servida y lista para entrega (0.50s).
>>> Orden #3 (Típica Mejorado) completada en 4.30s.

=========================================================
Todas las órdenes han sido procesadas.
Tiempo total de ejecución: 11.81 segundos.
=========================================================
```
