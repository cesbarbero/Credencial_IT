# Credencial_IT
Este script fue desarrollado para agilizar el proceso de recolección de credenciales en el marco de una tarea interna de migración y reconfiguración de sistemas. Está diseñado para que usuarios no técnicos puedan ingresar su contraseña de forma segura, sin intervención directa del área de sistemas.

¿Qué hace?
Identifica automáticamente al usuario que ejecuta el script.
Solicita únicamente la contraseña desde la consola.
Oculta la contraseña mientras se escribe (modo seguro).
Consulta si fue escrita correctamente antes de guardarla.
Guarda los datos en un archivo .txt propio por usuario.
Evita mostrar rutas internas o errores técnicos en caso de fallos.
Puede distribuirse como un .exe, sin requerir Python instalado.

¿Por qué se diseñó?
Durante una migración crítica, se necesitaba recopilar credenciales de múltiples usuarios de forma:
Automatizada
Segura
Auditada
Sin intervención directa del área de sistemas
Otras alternativas como formularios o correos electrónicos no ofrecían la privacidad ni la trazabilidad necesarias. Esta implementación resolvió ese cuello de botella de forma eficiente.

Seguridad aplicada
La contraseña se ingresa en modo oculto (no se visualiza ni con asteriscos).
Se guarda junto al usuario y timestamp en un archivo separado por usuario.
El archivo generado tiene permisos NTFS que impiden su lectura incluso al propio usuario.
El script maneja errores sin mostrar rutas o información sensible.
El .exe final incluye un ícono personalizado para mejorar la identificación del sistema.

Resultados
Se implementó en un entorno real con más de 60 usuarios.
Redujo a minutos una tarea que antes requería coordinación individual.
Eliminó errores humanos y mejoró la seguridad en la captura de credenciales.
El .exe se ejecutó en cualquier equipo sin necesidad de Python instalado.
