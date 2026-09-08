# Laboratorio 04 — Colaboración con Git y GitHub

Este proyecto incorpora herramientas reproducibles para resumir variables clínicas y visualizar la distribución de edad.

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

Las funciones de resumen clínico y visualización de edad están implementadas y cuentan con pruebas automatizadas.

## Resumen de variables clínicas

La función `summarize_clinical_data()` calcula estadísticas descriptivas para las columnas `age` y `hba1c`.

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

## Distribución de edad

La función `plot_age_distribution()` genera un histograma de edad y devuelve los ejes de Matplotlib para permitir personalizaciones adicionales.

```python
import pandas as pd

from lab04_git import plot_age_distribution

data = pd.DataFrame(
    {
        "age": [34, 42, 51, 63, 77],
    }
)

ax = plot_age_distribution(data)

ax.figure.savefig(
    "age_distribution.png",
    dpi=300,
    bbox_inches="tight",
)
```
