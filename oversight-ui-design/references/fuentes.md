# Procedencia y límites

- Fuente: https://supply.madebyoversight.com/?collection=all
- Captura: 20 de octubre de 2026, mediante Chrome y lectura del DOM renderizado.
- Catálogo: 192 botones públicos de preview; se guardaron nombre, texto de ficha y URL de miniatura en [catalog.json](evidence/catalog.json). Las URLs de miniatura son evidencia y pueden caducar; no se necesitan para utilizar el skill.
- Muestra visual: seis demos públicas en el visor, seleccionadas por diversidad compositiva. No se adquirieron ni extrajeron fuentes de plantillas comerciales, prompts ni contenidos de cuenta.
- Cobertura: principalmente primer pliegue de cada demo. Se inspeccionaron los selectores móviles de Pretty y Stillpoint. No se comprobaron todas las rutas, formularios, animaciones, breakpoints o accesibilidad de las demos.
- Las familias son síntesis propia. No existe afiliación ni una taxonomía oficial de Oversight en este skill.

## Evidencia consultable

| Referencia | Demo pública enlazada por el catálogo | Capturas |
| --- | --- | --- |
| Catálogo | [Oversight Supply](https://supply.madebyoversight.com/?collection=all) | [Escritorio](evidence/catalog-desktop.png) |
| Pretty | [Demo](https://ovo-pretty.webflow.io/) | [Escritorio](evidence/pretty-desktop.png), [visor móvil](evidence/pretty-mobile.png) |
| Calma | [Demo](https://ovo-calma.webflow.io/) | [Escritorio](evidence/calma-desktop.png) |
| Mosby | [Demo](https://ovo-mosby.webflow.io/) | [Escritorio inicial](evidence/mosby-desktop.png) |
| Queue | Consultar URL extraída en [live-links.json](evidence/live-links.json) | [Escritorio](evidence/queue-desktop.png) |
| Madeline | Consultar URL extraída en [live-links.json](evidence/live-links.json) | [Escritorio](evidence/madeline-desktop.png) |
| Stillpoint | [Demo](https://ovo-stillpoint.webflow.io/) | [Escritorio](evidence/stillpoint-desktop.png), [visor móvil](evidence/stillpoint-mobile.png) |

Las capturas incluyen el marco del visor y parte del catálogo detrás: esos elementos no pertenecen a las demos. Son evidencia interna de consulta; no reutilizarlas como activos gráficos del producto final. La presencia de un control en la captura no prueba su funcionalidad.

Medidas verificadas solo para el catálogo: viewport 1920 × 911; H1 de 32 px, familia declarada Tasa Orbiter con fallback Inter; entrada de búsqueda de 13 px con Inter. Estas medidas no se trasladan a las plantillas. No se extrajeron sus valores CSS ni nombres exactos de fuentes.
