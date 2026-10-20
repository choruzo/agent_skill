---
name: oversight-ui-design
description: Diseña o implementa webs e interfaces con dirección visual inspirada en las referencias públicas de Oversight Supply. Úsalo para landing pages, portfolios, servicios y UI de producto cuando se pida esta inspiración o una de sus familias visuales; adapta el estilo al producto y al sistema de diseño existente.
---

# Diseño web e interfaces inspirado en Oversight

Convierte una intención de producto en una composición con identidad: jerarquía marcada, imagen o producto protagonista, tipografía deliberada y relaciones espaciales coherentes. Usa las referencias como vocabulario compositivo, no como una plantilla que haya que reproducir.

## Elegir una dirección

Determina la tarea principal, público, contenido disponible, acción prioritaria y restricciones del proyecto. Reutiliza las respuestas y el stack ya indicados. Si falta información no esencial, declara una suposición breve y avanza.

Escoge una familia dominante según el contenido; respeta una elección explícita del usuario. Las familias son puntos de partida, no presets cerrados: puedes variar paleta, tipografía, composición y materiales conservando una jerarquía coherente. Cuando la elección esté abierta, decide y explica el motivo en una frase; muestra alternativas solo si ayudarían a resolver una decisión real.

| Familia | Referencias | Decisión distintiva | Encaja cuando |
| --- | --- | --- | --- |
| Editorial cálido | Calma, Stillpoint | Serif expresiva, neutros cálidos, verde profundo, fotografía humana y asimetría tranquila | Importan confianza, acompañamiento o relato personal |
| Tipográfico arquitectónico | Mosby | Identidad apilada de gran escala, lienzo sobrio, servicios pequeños en contrapeso y vacío deliberado | La identidad o la obra debe dominar |
| Producto oscuro | Pretty | Titular a izquierda, superficies oscuras y representación amplia del producto | La prueba principal es una herramienta o flujo |
| Lanzamiento luminoso | Queue | Promesa centrada, captación compacta y un campo luminoso detrás | Hay una acción de registro y una propuesta simple |
| Portfolio collage | Madeline | Imágenes de distintas escalas, solapes controlados y navegación discreta | La selección de trabajos comunica más que el texto |

Lee [familias.md](references/familias.md) para desarrollar la familia elegida y sus adaptaciones. No combines todas las firmas en una pantalla: un collage, un gran titular y un resplandor compiten si los tres intentan protagonizarla.

Si puedes interpretar imágenes con las herramientas y el modelo disponibles, abre al menos una captura de la familia elegida, enlazada en [fuentes.md](references/fuentes.md), antes de diseñar. Extrae dos o tres relaciones concretas que quieras adaptar: escala relativa, alineaciones, reparto del espacio o posición de la acción. Si no puedes ver imágenes, usa la sección correspondiente de `familias.md` y declara que trabajaste con la descripción; no afirmes haber inspeccionado capturas. No hace falta cargar el inventario completo ni todas las imágenes.

## Pasar de referencia a diseño

Antes de implementar, fija una especificación breve, proporcional a la tarea:

- Qué debe verse primero, segundo y tercero, y qué acción sigue.
- Composición y proporción entre contenido, imagen y espacio vacío.
- Roles tipográficos: display, lectura, etiquetas y datos. Usa fuentes disponibles o autorizadas con fallback; no atribuyas una fuente exacta a una captura.
- Tokens semánticos de fondo, superficie, texto, texto secundario, borde, acento, acción y estados. Define también escala de espacios, radios y ancho de contenido.
- Qué cambia al estrechar la pantalla: orden, columnas, navegación, imágenes y densidad.

Trata cualquier valor elegido como decisión propia, no como CSS extraído. Distingue la superficie del catálogo (sidebar, filtros, tarjetas y visor) del diseño de las demos. Usa la primera como referencia solo al construir un catálogo o explorador.

Adapta cada sección al contenido real. La repetición de un hero, tres tarjetas y FAQ no sustituye la arquitectura de información. Si hay un sistema de diseño existente, conserva sus componentes y modifica solo lo pedido.

## Aplicarlo a una interfaz funcional

Para una aplicación, usa el estilo en la jerarquía, el ritmo y los materiales. Da prioridad a navegación, datos y acciones. Reserva titulares enormes, fotografía y vacíos de gran tamaño para contextos que los justifiquen; una tabla de trabajo necesita densidad y lectura sostenida.

Representa con componentes reales aquello que el usuario deba operar. Una captura de tablero puede servir de demostración en una landing, pero no sustituye un tablero interactivo. Implementa acciones y estados pertinentes al alcance: carga, vacío, error, selección, éxito y permisos cuando correspondan. Si falta backend, identifica la simulación y su límite.

Cada control debe producir el efecto que promete su etiqueta. Por ejemplo, un botón de sonido debe reproducir o detener audio; cambiar únicamente su color no cumple esa función. Cuando una función no sea viable en el alcance, elimina el control, muestra por qué está deshabilitado o identifica explícitamente su carácter de demostración junto al propio control. Una operación local puede ser válida: un planificador sin servidor puede generar un recorrido, pero no debe confirmar una reserva inexistente. Comprueba la relación acción → efecto observable, no solo el cambio de aspecto o la aparición de un mensaje de éxito.

Los textos, cifras, testimonios y logotipos de las demos no son datos del proyecto. Usa contenido proporcionado; identifica como ficticios los ejemplos necesarios. Las capturas de `references/evidence/` sirven para consulta, no son activos para incluir en el producto final. No copies ni hotlinkees fotografías, logos, prompts comerciales o plantillas; usa materiales propios o con licencia adecuada.

## Verificar el resultado

Inspecciona la implementación en una vista ancha y otra estrecha, con el contenido real o un ejemplo representativo. Como punto de partida puedes usar 1440 × 900 y 390 × 844; adapta las dimensiones al producto. Registra los tamaños realmente utilizados, comprueba al menos una interacción principal en cada vista y captura el resultado cuando la herramienta lo permita. Comprueba que:

- La acción principal y la jerarquía siguen siendo claras sin depender de la imagen decorativa.
- El texto no queda cortado ni oculto por solapes; las columnas refluyen y no aparece scroll horizontal accidental.
- Navegación, formularios y controles funcionan con teclado, tienen nombres accesibles y foco visible. Los estados incluyen texto o icono además de color.
- El contraste permite leer texto secundario y controles; no reproduzcas deficiencias de las demos.
- Las animaciones, si se añaden, tienen propósito, respetan movimiento reducido y no bloquean la lectura ni la tarea.

Corrige los problemas observados. Distingue entre implementar CSS adaptable y verificar visualmente una pantalla estrecha: tener media queries no demuestra que el móvil funcione. Si no puedes fijar un viewport o ver la interfaz, usa otra vía disponible cuando sea razonable; si sigue sin ser posible, entrega lo construido e identifica la comprobación pendiente. No afirmes una validación que no ejecutaste. Entrega el resultado solicitado con una explicación breve de la familia aplicada, los cambios respecto a la referencia y la verificación realizada.

## Evidencia y alcance

La base es una captura pública del 20 de octubre de 2026: 192 fichas del catálogo y seis demos inspeccionadas, con vistas móviles de Pretty y Stillpoint. Las cinco familias son una síntesis de esas muestras, no una clasificación oficial ni un análisis visual exhaustivo de las 192 plantillas.

Para procedencia, demos y límites lee [fuentes.md](references/fuentes.md). El inventario completo está en [catalog.json](references/evidence/catalog.json); consúltalo para buscar nombres/categorías, no lo cargues por defecto. El skill funciona sin conexión y sin herramientas de navegador específicas; refresca las referencias públicas solo cuando la tarea lo requiera.
