# Proyecto Testeo urban routes sprint 8
- Consta de pruebas para comprobar la funcionalidad de la pagina de Urban Routes.
- Urban routes es una pagina con la que se puede solicitar un medio de transporte de acuerdo a las necesidades del solicitante
- Las pruebas utilizadas de este proyecto comprueban cada uno de los pasos del flujo completo de la solicitud de un taxi
- como parte del proyecto hay que clonar un repositorio 
- se usara Pycharm para trabajar en el proyecto
- Se utiliza Selenium
- El lenguaje utilizado es Python
- Se necesita tener instalado los paquetes pytest y request para ejecutar las pruebas.
- Hay que crear localizadores para cada item del codigo de la pagina que nos servira para las pruebas como imputs, botones y otros
- Se separan localizadores de metodos en 2 archivos separados y se aplican las pruebas en un tercer archivo llamado main
- Los localizadores para individualizar los items se buscan en el html del codigo de la pagina y se utilizan por medio de ID, Clase, Input, Xpath y CSS
- se utilizan esperas en las pruebas para darle tiempo al navegador que cargue elemntos de la pagina
- En total son 8 pruebas que validan que el flujo de solicitud de taxi sea exitoso, desde el ingreso de direccionde inicio-termino de viaje hasta que aparece el modal de busqueda de taxi
- se usa el comando pytest main.py para correr las pruebas desde la terminal