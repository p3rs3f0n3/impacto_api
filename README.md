````markdown
# 🌳 Impacto API

API de simulación para validar impacto ambiental en proyectos de reforestación. 
Incluye metas, progreso, votaciones, evidencias y recompensas. Diseñada para ser integrada con Chainlink Functions, dashboards Web3 y sistemas de gobernanza automatizada.

---

## 🚀 Ejecutar localmente

1. Clona este repositorio:

```bash
git clone https://github.com/tu_usuario/impacto-api.git
cd impacto-api
````

2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

3. Ejecuta el servidor:

```bash
python -m uvicorn app.main:app --reload
```

4. Accede a la documentación en Swagger UI:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📚 Endpoints disponibles

| Método | Ruta                                 | Descripción                                                                                                                                                 |
| ------ | ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `GET`  | `/proyectos`                         | 🔍 Lista todos los proyectos registrados con su estado (`Validado` o `Bajo cumplimiento`) y si cumplieron las metas (`cumplido: true/false`).               |
| `GET`  | `/proyectos/{proyecto_id}`           | 📄 Devuelve información general del proyecto: nombre, ubicación, fechas y ejecutor.                                                                         |
| `GET`  | `/proyectos/{proyecto_id}/secciones` | 🧩 Lista todas las secciones disponibles del proyecto (`meta`, `progreso`, `evidencias`, `votaciones`, etc.). Útil para construir menús o vistas dinámicas. |
| `GET`  | `/proyectos/{proyecto_id}/{seccion}` | 📂 Devuelve una sección específica del proyecto (`meta`, `progreso`, `historico_deforestacion`, `evidencias`, `votaciones`, `recompensas`).                 |
| `GET`  | `/proyectos/{proyecto_id}/resultado` | ✅ Evalúa si el proyecto cumplió sus metas comparando `meta` vs `progreso`. Devuelve un booleano y detalles por criterio (`arboles`, `co2`).                 |

---

## 🧪 ¿Para qué sirve esta API?

* Simular validación automática de impacto ambiental real.
* Integrarse con Chainlink Functions, VRF, Automation y DAO voting.
* Probar dashboards o sistemas de recompensas basadas en cumplimiento.
* Ideal para hackathons Web3 o proyectos de sostenibilidad.

---

## 🌐 Despliegue en Render (opcional)

Puedes desplegar esta API públicamente de forma gratuita usando [https://render.com](https://render.com):

### 🛠 Pasos:

1. **Sube este proyecto a GitHub.**

2. Crea una cuenta en [https://render.com](https://render.com).

3. Clic en “**New Web Service**” y conecta tu cuenta de GitHub.

4. Selecciona el repositorio de tu API (`impacto-api`).

5. Configura:

   * **Environment:** Python 3.11
   * **Start Command:**

     ```bash
     python -m uvicorn app.main:app --host 0.0.0.0 --port 10000
     ```
   * **Port:** 10000 (Render lo detecta automáticamente)
   * **Build Command:**

     ```bash
     pip install -r requirements.txt
     ```
   * Plan: selecciona el plan **Free**.

6. Espera el despliegue. Render te dará una URL como:

```
https://impacto-api.onrender.com
```

Puedes acceder a:

* Documentación: `https://impacto-api.onrender.com/docs`
* Endpoint `/proyectos`, etc.

---

## 📜 Licencia

MIT

```

---
