# agent_skill

Colección de skills para agentes, pensada para encapsular conocimientos, instrucciones, referencias y configuraciones reutilizables que puedan ser consumidas por agentes de IA.

## ¿Qué es este repositorio?

`agent_skill` centraliza definiciones de skills para agentes en formato estructurado. Cada skill puede incluir:

- instrucciones de uso y comportamiento
- contexto de dominio
- referencias y evidencias
- configuración o metadata del agente
- plantillas para tareas repetibles

El objetivo es facilitar la reutilización de conocimiento y capacidades entre distintos agentes sin duplicar lógica ni contexto.

## Estructura del proyecto

```text
agent_skill/
├── LICENSE
├── README.md
└── oversight-ui-design/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    └── references/
        ├── familias.md
        ├── fuentes.md
        └── evidence/
            └── catalog.json
```

## Skill incluida

### oversight-ui-design

Skill orientada a la creación de interfaces y diseños web con una dirección visual inspirada en referencias públicas de diseño editorial y de producto.

Incluye:

- instrucciones operativas para diseñar páginas, portfolios, landing pages y UI
- guías de composición, tipografía, jerarquía visual y responsive behavior
- referencias de familias visuales
- evidencias y fuentes de inspiración
- configuración del agente para integración con OpenAI

## Cómo usarlo

Cada skill vive en su propio directorio y normalmente incluye un archivo `SKILL.md` con la lógica principal del comportamiento. Si la skill requiere configuración específica para un agente, también puede incluir un archivo dentro de `agents/`.

La convención recomendada es:

1. Crear un directorio por skill.
2. Añadir `SKILL.md` con propósito, instrucciones y contexto.
3. Incluir referencias relevantes en `references/`.
4. Añadir configuración del agente si hace falta.

## Objetivo del repositorio

Este repositorio está pensado para actuar como un catálogo de capacidades reutilizables para agentes, especialmente para tareas de diseño, investigación, análisis y ejecución contextualizada.

## Licencia

Este proyecto se distribuye bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Estado

Proyecto en crecimiento, orientado a ir agregando nuevas skills para agentes según los casos de uso que se necesiten.
