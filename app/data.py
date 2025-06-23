# Simula una base de datos de proyectos

proyectos = {
    "proy001": {
        "info": {
            "id": "proy001",
            "nombre": "Reforestación Amazonas 2025",
            "descripcion": "Sembrar 1000 árboles en 3 zonas del Amazonas.",
            "ejecutor": {
                "organizacion": "EcoAmazonas",
                "wallet": "0xabc123...",
                "responsable": "Laura Martínez"
            },
            "ubicacion": {
                "pais": "Colombia",
                "region": "Amazonas",
                "lat": -3.4653,
                "lon": -62.2159
            },
            "fecha_inicio": "2025-05-01",
            "fecha_fin": "2025-12-15"
        },
        "meta": {
            "meta_arboles": 1000,
            "meta_co2_toneladas": 5.0,
            "periodo_meses": 6
        },
        "progreso": {
            "arboles_plantados": 1234,
            "co2_reducido_toneladas": 8.5,
            "fecha_reporte": "2025-06-21",
            "verificado_por": "Dron_AZ9",
            "fuente_datos": "simulacion-api-v1"
        },
        "historico": {
            "anio_base": 2020,
            "datos": [
                {"anio": 2020, "arboles_perdidos": 850},
                {"anio": 2021, "arboles_perdidos": 920},
                {"anio": 2022, "arboles_perdidos": 1030},
                {"anio": 2023, "arboles_perdidos": 980}
            ]
        },
        "evidencias": {
            "fotos": [],
            "reportes_pdf": []
        },
        "votaciones": [],
        "recompensas": []
    },
    "proy002": {
        "info": {
            "id": "proy002",
            "nombre": "Reforestación Putumayo 2025",
            "descripcion": "Meta de 1500 árboles. Proyecto no cumplió metas mínimas.",
            "ejecutor": {
                "organizacion": "Bosque Vivo",
                "wallet": "0xdef456...",
                "responsable": "Carlos Ruiz"
            },
            "ubicacion": {
                "pais": "Colombia",
                "region": "Putumayo",
                "lat": -0.5074,
                "lon": -76.4995
            },
            "fecha_inicio": "2025-04-01",
            "fecha_fin": "2025-12-01"
        },
        "meta": {
            "meta_arboles": 1500,
            "meta_co2_toneladas": 6.5,
            "periodo_meses": 8
        },
        "progreso": {
            "arboles_plantados": 950,
            "co2_reducido_toneladas": 4.2,
            "fecha_reporte": "2025-06-21",
            "verificado_por": "Dron_BV7",
            "fuente_datos": "simulacion-api-v2"
        },
        "historico": {
            "anio_base": 2020,
            "datos": []
        },
        "evidencias": {
            "fotos": [],
            "reportes_pdf": []
        },
        "votaciones": [],
        "recompensas": []
    }
}
