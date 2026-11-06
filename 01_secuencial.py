import time


def preparar_cafe_artesanal(orden_id, tipo_cafe, metodo, tiempos):
    print(f"\n>>> Iniciando preparación de Orden #{orden_id}: {tipo_cafe} (Método: {metodo})")

    # Etapa 1: Pesaje y molienda de grano
    print(f"[Orden #{orden_id}] [1/4] Moliendo granos de café de especialidad...")
    time.sleep(tiempos["molienda"])
    print(f"[Orden #{orden_id}]       Molienda completada ({tiempos['molienda']:.2f}s).")

    # Etapa 2: Calentamiento de agua a temperatura precisa
    print(f"[Orden #{orden_id}] [2/4] Calentando agua a temperatura controlada...")
    time.sleep(tiempos["calentamiento"])
    print(f"[Orden #{orden_id}]       Agua lista a temperatura óptima ({tiempos['calentamiento']:.2f}s).")

    # Etapa 3: Pre-infusión y extracción por goteo
    print(f"[Orden #{orden_id}] [3/4] Ejecutando pre-infusión y extracción filtrada...")
    time.sleep(tiempos["extraccion"])
    print(f"[Orden #{orden_id}]       Extracción artesanal finalizada ({tiempos['extraccion']:.2f}s).")

    # Etapa 4: Servido y control de calidad aromática
    print(f"[Orden #{orden_id}] [4/4] Sirviendo en taza y verificando notas de cata...")
    time.sleep(tiempos["servido"])
    print(f"[Orden #{orden_id}]       Taza servida y lista para entrega ({tiempos['servido']:.2f}s).")

    tiempo_orden = (
        tiempos["molienda"]
        + tiempos["calentamiento"]
        + tiempos["extraccion"]
        + tiempos["servido"]
    )
    print(f">>> Orden #{orden_id} ({tipo_cafe}) completada en {tiempo_orden:.2f}s.")


def main():
    print("=========================================================")
    print(" SISTEMA DE PREPARACIÓN DE CAFÉ ARTESANAL (SECUENCIAL)")
    print("=========================================================")
    print("Iniciando procesamiento secuencial de órdenes...")

    ordenes = [
        {
            "id": 1,
            "tipo": "Geisha de Altura",
            "metodo": "V60 Dripper",
            "tiempos": {
                "molienda": 0.8,
                "calentamiento": 1.2,
                "extraccion": 1.5,
                "servido": 0.5,
            },
        },
        {
            "id": 2,
            "tipo": "Bourbon Rosado",
            "metodo": "Aeropress",
            "tiempos": {
                "molienda": 0.7,
                "calentamiento": 1.0,
                "extraccion": 1.3,
                "servido": 0.5,
            },
        },
        {
            "id": 3,
            "tipo": "Típica Mejorado",
            "metodo": "Prensa Francesa",
            "tiempos": {
                "molienda": 0.9,
                "calentamiento": 1.3,
                "extraccion": 1.6,
                "servido": 0.5,
            },
        },
    ]

    tiempo_inicio = time.perf_counter()

    for orden in ordenes:
        preparar_cafe_artesanal(
            orden_id=orden["id"],
            tipo_cafe=orden["tipo"],
            metodo=orden["metodo"],
            tiempos=orden["tiempos"],
        )

    tiempo_fin = time.perf_counter()
    tiempo_total = tiempo_fin - tiempo_inicio

    print("\n=========================================================")
    print("Todas las órdenes han sido procesadas.")
    print(f"Tiempo total de ejecución: {tiempo_total:.2f} segundos.")
    print("=========================================================")


if __name__ == "__main__":
    main()

