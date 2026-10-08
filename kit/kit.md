Este kit reúne lo que prometimos en la sesión: una lista de verificación para endurecer tus proyectos, el guion de preguntas que IT suele hacer con sus respuestas, y una guía para montar tu propio laboratorio aislado y practicar con responsabilidad.

**Contenido**

1. Uso responsable y marco legal
2. Checklist de hardening por fase del proyecto
3. Guion de preguntas de IT, con respuestas y evidencia
4. Guía del laboratorio: red aislada y USB de arranque
5. Referencias

---

## 1. Uso responsable y marco legal

Todo el contenido de este kit tiene fines educativos: aprender a diseñar, endurecer y defender instalaciones AV.

::: alerta
**Probar o analizar sistemas sin autorización escrita del dueño está penado por la ley. Hazlo únicamente sobre tu propio laboratorio, en una red aislada y con equipos que te pertenecen o para los que tienes autorización expresa y por escrito. Nunca sobre la red de un evento, de tu empresa o de un cliente.**
:::

Referencias legales, a modo de ejemplo y sin pretender ser asesoría legal:

- Colombia: Ley 1273 de 2009, artículo 269A.
- Argentina: Ley 26.388, artículo 153 bis del Código Penal.
- México: Código Penal Federal, artículos 211 bis 1 a 211 bis 7.

Consulta la legislación vigente de tu país. Las opiniones de este material son de los presentadores y no representan a fabricantes ni a los organizadores.

---

## 2. Checklist de hardening por fase del proyecto

Úsala proyecto por proyecto. Cada punto cumplido es una pregunta menos de IT.

::: nota
Esta lista es una **base, no un checklist exhaustivo**. Adáptala a cada proyecto y a las políticas del cliente. Fuera de tu laboratorio, aplícala solo sobre sistemas para los que tengas autorización.
:::

Proyecto: ____________________   Cliente: ____________________   Fecha: __________

### Diseño

☐ La segmentación está en el plano: VLAN AV, VLAN de control, red corporativa y red de invitados, con las reglas entre ellas definidas.  
☐ Los requisitos de seguridad están en el pliego: cifrado del control, cuentas gestionadas, registro de eventos y plan de firmware.  
☐ Los equipos elegidos soportan gestión cifrada, cuentas con roles y actualización de firmware firmada.  
☐ Está definido qué tráfico necesita cruzar entre segmentos y qué queda bloqueado.  
☐ Está definido quién administra el equipo después de la entrega.  

### Implementación

☐ Se cambiaron todas las credenciales de fábrica; no queda ninguna cuenta por defecto activa.  
☐ Las cuentas son nominales o gestionadas; nada de una contraseña compartida.  
☐ Los servicios y protocolos sin uso están apagados.  
☐ La gestión del equipo va por canal cifrado, con certificado válido donde el equipo lo permita.  
☐ El firmware está en la última versión estable y quedó anotada.  
☐ El equipo está en su VLAN y se verificó que no alcanza la red corporativa ni la de invitados.  
☐ El acceso físico al rack está controlado y los puertos de red sin uso están deshabilitados.  
☐ Se hizo una verificación sobre la red del proyecto, con autorización del cliente, y se guardó el resultado.  

### Entrega

☐ Está documentada la lista de puertos y servicios de cada equipo, para IT.  
☐ Los registros de eventos están activos y se envían a donde IT los pueda ver.  
☐ Hay responsable y calendario para las actualizaciones de firmware.  
☐ Existe respaldo de la configuración de cada equipo, guardado fuera del propio equipo.  
☐ El cliente recibió el inventario: equipo, ubicación, dirección, versión de firmware y cuenta administradora.  
☐ Quedó acordado qué hacer ante un incidente: a quién se avisa y qué se aísla primero.  
☐ Las credenciales de administración se entregaron de forma segura.  

---

## 3. Guion de preguntas de IT, con respuestas y evidencia

Llega a la reunión con estas respuestas listas.

| Pregunta de IT | Respuesta que debes tener | Evidencia que conviene llevar |
|---|---|---|
| ¿Qué puertos y servicios usa cada equipo? | Lista por equipo, con el motivo de cada uno. | Tabla de puertos y servicios. |
| ¿En qué red va a estar? | En la VLAN AV, separada de corporativa e invitados, con reglas explícitas. | Diagrama de segmentación y reglas. |
| ¿Qué tráfico cruza a la red corporativa? | Solo lo acordado, por puertos concretos. | Lista de flujos: origen, destino, puerto, propósito. |
| ¿Cómo se gestionan las credenciales? | Cuentas gestionadas y con roles; ninguna de fábrica activa. | Inventario de cuentas por equipo. |
| ¿La gestión va cifrada? | Sí; los protocolos sin cifrar están apagados. | Configuración de servicios de cada equipo. |
| ¿Cómo se actualizan? | Versión anotada, responsable y calendario. | Inventario con versiones y acuerdo de mantenimiento. |
| ¿Cómo se monitorea? | Registros activos enviados al sistema de monitoreo de IT. | Destino de los registros y muestra de eventos. |
| ¿Qué acceso remoto tiene el fabricante o el integrador? | Solo el acordado, por canal cifrado y revocable. | Lista de accesos y cómo se desactivan. |
| ¿Hay respaldo de la configuración? | Sí, fuera del equipo, con fecha. | Ubicación y fecha del último respaldo. |
| ¿Qué pasa si un equipo se compromete? | Está aislado en su segmento; hay un contacto definido. | Procedimiento breve de respuesta. |
| ¿Quién administra el equipo tras la entrega? | Definido en el contrato. | Acta de entrega con responsabilidades. |

---

## 4. Guía del laboratorio: red aislada y USB de arranque

El objetivo es tener un entorno propio y separado para practicar lo del taller sin tocar ninguna red ajena.

### Regla de oro

::: alerta
**Practica solo aquí. Nunca sobre la red de un recinto, de tu empresa o de un cliente. Un laboratorio aislado no es una recomendación de estilo: es lo que mantiene tu práctica dentro de la ley.**
:::

### La red aislada

- Un router propio, de uso exclusivo para el laboratorio, sin ningún cable ni enlace hacia tu red de casa, de la oficina o de internet si no lo necesitas.
- Un equipo AV de prueba que te pertenezca, con su configuración de fábrica, para observar cómo se anuncia y qué expone.
- Tu equipo de análisis conectado a esa misma red.
- Tu teléfono, si quieres repetir la parte de participación desde el navegador.

Mantén este laboratorio físicamente y lógicamente separado. Si reutilizas un router viejo, restablécelo de fábrica y cámbiale la contraseña de administración antes de empezar.

### USB de arranque para el equipo de análisis

Una memoria USB arrancable con una distribución de seguridad te da las herramientas del taller, como el escaneo de red y el análisis de tráfico, sin instalar nada en tu equipo. Una opción común y gratuita es Kali Linux.

Pasos generales, usando siempre la documentación oficial para no fijar una versión que luego quede vieja:

1. **Descarga la imagen oficial.** Ve a [kali.org/get-kali](https://www.kali.org/get-kali/) y descarga la imagen de instalador o "Live" más reciente. La versión Live permite arrancar desde la USB sin instalar.
2. **Verifica la integridad.** Compara la suma de verificación SHA-256 de tu archivo con la que publica el sitio oficial. Si no coinciden, no uses esa descarga. El procedimiento está en [kali.org/docs/introduction/download-official-kali-linux-images](https://www.kali.org/docs/introduction/download-official-kali-linux-images/).
3. **Graba la USB.** Usa una memoria de 8 GB o más; se borra por completo.
   - **Windows:** la herramienta recomendada es balenaEtcher o Rufus.
   - **macOS:** balenaEtcher, o el comando `dd` desde la Terminal.
   - **Linux:** balenaEtcher, o `dd` indicando con cuidado el dispositivo correcto.
   La guía oficial está en [kali.org/docs/usb/](https://www.kali.org/docs/usb/).
4. **Arranca desde la USB.** Entra al menú de arranque de tu equipo, normalmente con F12, F2, Esc o Supr según el fabricante, y elige la memoria USB. Trabaja solo contra tu laboratorio aislado.

Alternativa sin USB: si prefieres no arrancar desde la memoria, puedes correr la misma distribución dentro de una máquina virtual con VirtualBox, conectada a una red interna aislada. Kali publica imágenes ya preparadas para máquinas virtuales.

### Qué practicar

- Observar cómo un equipo AV se anuncia en la red con protocolos de descubrimiento, y leer ese tráfico con un analizador de paquetes.
- Mapear qué hay en tu red de laboratorio y qué puertos y servicios expone cada equipo.
- Repetir el checklist de hardening sobre tu equipo de prueba y comprobar el antes y el después.

---

## Contacto

¿Dudas, un proyecto o seguir la conversación? Escríbenos.

- **Juan Pineda** · Pyxis — [juan.pineda@pyxis.tech](mailto:juan.pineda@pyxis.tech) · [linkedin.com/in/jdpinedac](https://www.linkedin.com/in/jdpinedac/)
- **Eduardo Travi** · AVI SPL — [Eduardo.Travi@avispl.com](mailto:Eduardo.Travi@avispl.com) · [linkedin.com/in/eduardotravi](https://www.linkedin.com/in/eduardotravi/)

## 5. Referencias

- NIST Cybersecurity Framework 2.0: [nist.gov/cyberframework](https://www.nist.gov/cyberframework)
- MITRE ATT&CK: [attack.mitre.org](https://attack.mitre.org)
- MITRE ATT&CK explicado, con video: [ibm.com/mx-es/think/topics/mitre-attack](https://www.ibm.com/mx-es/think/topics/mitre-attack)
- Cyber Kill Chain, Lockheed Martin: [lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html](https://lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html)
- CIS Critical Security Controls v8.1: [cisecurity.org/controls/cis-controls-list](https://www.cisecurity.org/controls/cis-controls-list)
- Nmap: [nmap.org](https://nmap.org)
- Wireshark: [wireshark.org](https://www.wireshark.org)
- Kali Linux: [kali.org/get-kali](https://www.kali.org/get-kali/)

---

*Material educativo del taller. Las marcas de equipos se omiten a propósito. Esto no es asesoría legal: consulta la normativa vigente de tu país.*
