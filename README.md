# Laboratorio 04 — Colaboración con Git y GitHub

Proyecto para practicar un flujo completo de colaboración científica mediante
issues, ramas, pull requests, revisión de código, integración continua y
protección de la rama principal.

## Objetivo

Construir un proyecto pequeño de análisis de datos biomédicos y desarrollar
sus funcionalidades mediante un flujo colaborativo reproducible.

## Tecnologías

- Python
- pandas
- NumPy
- Matplotlib
- pytest
- ruff
- GitHub Actions

## Estado

La función de resumen clínico está en desarrollo.

## Resumen de variables clínicas

La función `summarize_clinical_data()` calcula estadísticas descriptivas
para las columnas `age` y `hba1c`.

```python
import pandas as pd

from lab04_git import summarize_clinical_data


data = pd.DataFrame(
    {
        "age": [40, 50, 60],
        "hba1c": [6.5, 7.0, 7.5],
    }
)

summary = summarize_clinical_data(data)

print(summary)
```
