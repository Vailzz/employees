<h2> Documentación: </h2>
Este proyecto se centra en desarrollar un sistema de gestión de empleados que realice un seguimiento preciso de los cambios en la estructura jerárquica. Cada empleado tiene un superior jerárquico, y cada cambio en esta relación incrementa la versión del empleado.

<h3>Decisiones de Diseño y Consideraciones Clave</h3>
 - Estructura de Datos: Se utilizó un modelo empleado con campos como nombre, posición, versión y una clave externa que se relaciona consigo mismo para representar las relaciones jerárquicas.

 - Serialización: Se empleó Django rest Framework para serializar los objetos “Empleado”, facilitando la representación en formato JSON.

 - Vistas y Lógica de Actualización: Se crearon vistas para consultar la jerarquía de empleados, actualizar jefes y manejar el versionamiento correspondiente.

 - Manejo de Nulos: Empleados sin jefe directo se representan adecuadamente en el sistema con la configuración de ForeignKey y null=True.

<h3>Enfoque de Solución</h3>
Estructura de Datos: Se diseñó un modelo “Empleado”con campos relevantes y métodos para gestionar la jerarquía.

 - Serialización y Vistas: Se utilizó un serializer para convertir objetos “Empleado”en datos JSON en las vistas correspondientes.

 - Lógica de Actualización: Se implementa la lógica de actualización de jefes y versionamiento en las vistas respectivas.
