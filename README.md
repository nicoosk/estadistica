# Estadistica
Esto es un repositorio hecho para guardar códigos de ejercicos estadísticos hechos en python. Es para uso personal y compartido, siéntase libre de copiar lo que sea necesario para sus estudios/trabajo.

## Descargar scipy
Scipy es una librería de python que tiene muchas formulas científicas disponibles para el uso personalizado de contextos de nuestro agrado. En el siguiente link hay una pequeña guía con algunas formas de instalar scipy en la maquina en la que estén. NOTA: Necesitan tener instalado python para poder ejecutar todo el codigo. Python se puede instalar en la pagina oficial de python.

### Requisitos previos
Estos son los requerimientos para que puedas tener una experiencia fluida y cómoda, tanto de ejecución de código como de actualización del mismo, ya que este repositorio se actualizará con el tiempo agregando más funciones.

- *Python (última versión es lo óptimo): https://www.python.org/downloads/
- *Scipy: https://scipy.org/install/
- Git: https://git-scm.com/downloads
- Visual Studio Code: https://code.visualstudio.com/download

*Los puntos marcados con asterisco son obligatorios*

# Como utilizar este proyecto
Para poder usar las funciones incluidas en este repositorio, deberás cumplir con los requisitos previos para que todo funcione correctamente.

Si tienes configurado Git y sabes como clonar de buena forma un proyecto, puedes saltarte todo lo que venga a continuación.

## Copiando el proyecto
No es necesario que copies todo el proyecto, pero sería lo ideal, es mucho más rápido y puedes mantener el código actualizado. Para poder copiar el código, solo debes seleccionar, copiar y pegar el código que necesites en tu editor de texto (de preferencia vscode) y listo. 

Si deseas, en cambio, clonar todo el proyecto, deberás descargar la herramienta Git en tu PC. Lo ideal es que lo configures con tus credenciales, aquí te dejo una pequeña guía de [como configurar Git y Github de la manera recomendada](https://www.youtube.com/watch?v=wHh3IgJvXcE "como configurar Git y Github de la manera recomendada") (sáltate la parte de llaves ssh, no es necesario).

## Clonando el proyecto
Una vez que tengas configurado Git, es momento de introducir comandos en la terminal. 

Primero, crea un directorio en el lugar que más te acomode (Escritorio, Documentos, etc). Este será el lugar donde almacenes todos tus proyectos. Luego, presiona el botón verde que dice *code* y vete al apartado donde dice *HTTPS*. Ahí es donde copiarás el link que te otorga Github.

Ahora abre tu terminal de Git y muévete al directorio que hayas creado. Por ejemplo, el mío está en Documentos y se llama */Proyectos/*.

`$ cd Documentos/Proyectos/`

Ahora que estás ubicado en tu directorio de proyectos, clona el repositorio con el comando `git clone`

`$ git clone https://github.com/nicoosk/estadistica.git`

Esto clonará el repositorio en el directorio de Proyectos. Debería quedarte otro directorio dentro de Proyectos que se llame */estadistica/*. Aquí es donde está toda la magia y puedes abrir esta ubicación en Visual Studio Code para poder utilizar las funciones disponibles.

## ¿Cómo actualizo mi copia del repositorio a la más reciente?
Para poder actualizar los directorios a la versión más reciente con las más nuevas funciones, deberás hacer uso del comando `pull` de Git de la siguiente manera:

`$ git pull origin main`

Comenzará la actualización del proyecto, poniéndose al día con la versión que exista en la rama *main* de Github. En el caso de que ya estés en la última versión del proyecto, Git te dará el siguiente mensaje:

	`Desde github.com:nicoosk/estadistica
 	* branch            main       -> FETCH_HEAD
	Ya está actualizado.`

# Agradecimientos
Quiero darle las gracias a mi profesor de estadística 2, Eliecer Peña, que nos entusiasmó a utilizar código para resolver ejercicios estadísticos complejos y por proveer gran cantidad del código disponible en este repositorio.

Fin de README
