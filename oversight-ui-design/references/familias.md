# Familias y traducción a producto

Las observaciones siguientes proceden de las capturas enlazadas en `fuentes.md`. Las pautas de implementación son propuestas; no son medidas, CSS ni reglas oficiales de Oversight.

Usa cada familia como una gramática de composición. Las paletas y los recursos descritos identifican las muestras; puedes sustituirlos según marca y contenido. Explica brevemente qué relación visual conservas y qué cambias. Por ejemplo, una interfaz editorial puede mantener asimetría y jerarquía serif con una paleta fría, o prescindir de fotografía cuando no haya material adecuado.

## Editorial cálido: Calma / Stillpoint

**Observado.** Calma usa fondo marfil, texto verde oscuro, serif prominente y filete bajo la navegación. El hero contrapone texto a izquierda y un retrato grande a derecha; separa verticalmente la presentación del bloque de historia y CTA. Stillpoint pone el titular serif inclinado a izquierda, explicación y CTA a derecha y una fotografía ancha debajo. Un fragmento del titular y el CTA usan terracota. Su vista móvil apila titular, explicación, CTA y foto, manteniendo el fragmento de color.

**Aplicación.** Elige una de las dos composiciones según el material: retrato vertical para presentar a una persona; foto horizontal para una experiencia o contexto. Usa un solo énfasis dentro del titular. Relaciona los márgenes y la fotografía con el ritmo de lectura, no con una altura de pantalla fija.

**En UI.** Conserva superficies cálidas y jerarquía serena en formularios, reservas y lectura; usa sans legible para campos, etiquetas y datos. Reduce los vacíos en pantallas de trabajo. Una acción de cita necesita disponibilidad, confirmación y error comprensibles, además de un botón atractivo.

**Evitar.** Fotos de stock sin relación con el servicio, párrafos enteros en cursiva, bajo contraste beige sobre beige o testimonios inventados presentados como reales.

## Tipográfico arquitectónico: Mosby

**Observado.** El estado inicial capturado tiene fondo negro, identidad blanca en mayúsculas enormes y líneas apiladas a izquierda. Una lista pequeña de servicios crea contrapeso a derecha; propuesta breve y botón quedan abajo a izquierda. El thumbnail del catálogo incluye imágenes de proyectos; la captura de la demo no basta para determinar cuándo aparecen o cómo se mueven.

**Aplicación.** Usa el nombre o una frase breve como pieza gráfica. Diseña los saltos por significado y ritmo; permite adaptación cuando cambien idioma o ancho. Reserva un eje para identidad y otro para información de apoyo. Añade obra real cuando esté disponible, sin inventar una animación para reproducir el thumbnail.

**En UI.** Traslada escala y contraste a cabeceras de proyectos o resúmenes; vuelve a una escala compacta dentro de tablas, herramientas y paneles. La navegación y la siguiente acción deben encontrarse incluso con mucho espacio vacío.

**Evitar.** `nowrap` que rompa móvil, mayúsculas masivas en instrucciones, esperar a que termine una animación para mostrar información esencial.

## Producto oscuro: Pretty

**Observado.** Fondo casi negro, titular sans pesado a izquierda, explicación debajo y dos CTA a derecha. Un tablero de producto ancho ancla la mitad inferior: columnas, tarjetas, avatares y pequeños acentos de estado. En la vista móvil aparece navegación compacta; la captura es una comprobación del visor móvil, no una auditoría del producto completo.

**Aplicación.** Construye profundidad con niveles de superficie y bordes discretos. Usa la vista de producto para demostrar una tarea concreta; selecciona un recorte legible antes que un dashboard lleno de minitexto. Mantén la prioridad entre acción principal y secundaria al apilarlas.

**En UI.** El tablero real necesita columnas y estados identificables, acciones operables y una alternativa móvil útil (lista, pestañas o desplazamiento deliberado según el caso). Ofrece alternativa a arrastrar cuando exista drag and drop. La etiqueta de estado debe seguir siendo legible sin el acento verde o azul.

**Evitar.** Convertir una imagen de marketing en la aplicación, controles grises invisibles sobre negro, resplandores detrás de todo el texto y efectos metálicos en cada botón.

## Lanzamiento luminoso: Queue

**Observado.** Campo violeta luminoso, navegación superior redondeada y translúcida, promesa centrada en dos líneas, explicación breve, campo de email con flecha y prueba social debajo; una captura ancha de producto entra por la parte inferior. El nombre del catálogo es Queue; la demo muestra la marca Waiting.

**Aplicación.** Una sola acción de captación domina. El gradiente crea un escenario alrededor de la promesa y el producto; ajusta intensidad y contraste según su contenido. La secuencia útil es promesa, explicación, acción, evidencia y demostración. Usa prueba social solo si existen datos autorizados.

**En UI.** Limita el efecto luminoso a onboarding, bienvenida o zonas de promoción. Para uso sostenido, ofrece superficies estables y legibles. Un registro necesita etiqueta persistente, validación, estado pendiente, respuesta de éxito/error y envío real o simulación declarada.

**Evitar.** Usar placeholder como única etiqueta, copiar la cifra de inscritos de la demo, navegación de demostración como P1–P6 en un producto real, brillo que oculte foco o texto.

## Portfolio collage: Madeline

**Observado.** Fondo gris claro, navegación monoespaciada con corchetes y selección azul. Fotos superpuestas de tamaños muy distintos forman un campo descentrado; un retrato grande domina a derecha. La captura fija no permite atribuir parallax, física ni una interacción específica.

**Aplicación.** Asigna un papel a cada imagen: protagonista, apoyo o textura. Controla solapes, recortes y zonas de exclusión alrededor de navegación y texto. La estructura de lectura y enlaces de proyectos debe seguir existiendo aunque la composición sea libre.

**En UI.** Úsalo para explorar obra o medios. En móvil, una secuencia editorial o grid simple puede conservar variedad de escala sin reproducir todas las posiciones absolutas. Los enlaces necesitan objetivos de toque claros y descripciones; conserva un orden de foco coherente con el contenido.

**Evitar.** Posiciones aleatorias en cada render, imágenes decorativas que bloqueen enlaces, contenido esencial accesible solo al hover, collage de datos que el usuario debe comparar con precisión.

## Proponer tokens sin fingir extracción

Define los roles y elige valores adecuados al contenido. Ejemplo de nomenclatura, independiente de framework: `--canvas`, `--surface`, `--surface-raised`, `--ink`, `--ink-muted`, `--line`, `--accent`, `--action`, `--focus`, `--success`, `--danger`, `--font-display`, `--font-body`, `--font-data`, `--content-max`, `--space-*`, `--radius-*`.

En editorial, parte de un lienzo cálido y una tinta profunda; en producto oscuro, diferencia lienzo y tarjetas por luminancia; en collage, deja que las imágenes aporten la mayor parte del color. Elige tamaños fluidos con límites de lectura y comprueba el caso estrecho. Los valores concretos son decisiones del proyecto; ninguna paleta hexadecimal o escala numérica de este skill se atribuye a una demo.
