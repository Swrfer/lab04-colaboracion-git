# Laboratorio 04 — Colaboración con Git y GitHub

Este proyecto incorpora visualizaciones reproducibles para explorar la distribución de edad.

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

La función de visualización de edad está en desarrollo.
## Distribución de edad

La función `plot_age_distribution()` genera un histograma de edad y devuelve
los ejes de Matplotlib para permitir personalizaciones adicionales.

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
