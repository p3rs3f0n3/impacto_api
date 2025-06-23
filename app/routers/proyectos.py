from fastapi import APIRouter, HTTPException
from app.data import proyectos

router = APIRouter()

@router.get("/proyectos")
def get_lista_proyectos():
    return [
        {
            "id": pid,
            "nombre": p["info"]["nombre"],
            "estado": "Validado" if p["progreso"]["arboles_plantados"] >= p["meta"]["meta_arboles"] else "Bajo cumplimiento",
            "cumplido": p["progreso"]["arboles_plantados"] >= p["meta"]["meta_arboles"]
        }
        for pid, p in proyectos.items()
    ]


@router.get("/proyectos/{proyecto_id}")
def get_info(proyecto_id: str):
    if proyecto_id in proyectos:
        return proyectos[proyecto_id]["info"]
    raise HTTPException(status_code=404, detail="Proyecto no encontrado")


@router.get("/proyectos/{proyecto_id}/secciones")
def get_secciones(proyecto_id: str):
    if proyecto_id not in proyectos:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    
    # Excluye "info" porque ya se entrega aparte
    secciones = [k for k in proyectos[proyecto_id].keys() if k != "info"]
    
    return {
        "proyecto_id": proyecto_id,
        "secciones_disponibles": secciones
    }


@router.get("/proyectos/{proyecto_id}/{seccion}")
def get_detalle(proyecto_id: str, seccion: str):
    if proyecto_id not in proyectos:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    if seccion not in proyectos[proyecto_id]:
        raise HTTPException(status_code=404, detail="Sección no disponible")
    return proyectos[proyecto_id][seccion]


@router.get("/proyectos/{proyecto_id}/resultado")
def get_resultado(proyecto_id: str):
    if proyecto_id not in proyectos:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")

    meta = proyectos[proyecto_id]["meta"]
    progreso = proyectos[proyecto_id]["progreso"]

    resultado_arboles = progreso["arboles_plantados"] >= meta["meta_arboles"]
    resultado_co2 = progreso["co2_reducido_toneladas"] >= meta["meta_co2_toneladas"]

    return {
        "proyecto_id": proyecto_id,
        "cumplido": resultado_arboles and resultado_co2,
        "detalles": {
            "arboles": "superado" if resultado_arboles else "insuficiente",
            "co2": "superado" if resultado_co2 else "insuficiente"
        }
    }
