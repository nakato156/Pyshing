var i = 0;
var width = window.screen.width
window.onload = init

function init(){
    let loader = document.getElementById("loader") 
    const field_password = document.getElementById("pass")
    const field_email = document.getElementById("email")
    const btn_login = document.getElementById("btnSend")
    const form_login = document.getElementById("logIn")

    form_login.addEventListener("submit", sendData)
    const view = document.getElementById("view")

    field_password.addEventListener("keypress", ()=>{
        view.style.display = field_password.value.length>1 ? "block" : "none";
    })
    let element = form_login.getBoundingClientRect()
    loader.style.left = `${element.x+(element.width/2)-70}px`
    view.addEventListener("click",()=>{
        let type = field_password.getAttribute("type")=="password" ? "text":"password"
        field_password.setAttribute("type", type)
    })
    field_email.parentElement.addEventListener("click", ()=> field_email.focus())
    field_password.parentElement.addEventListener("click", ()=> field_password.focus())
    
    async function sendData(e){
        e.preventDefault();
        reset_alerts()
        btn_login.style.backgroundColor = "#1670e5e0"
        let msg;
        const main = document.getElementById("main")
        if(!field_email.value.trim() || !field_password.value.trim()){
            let field = field_email.value.trim() ? "msgPass": "msgMail"
            main.classList.remove("main")
            main.classList.add("errorLogin")
            main.children[1].style.display = "none"

            field = field == "msgPass" ? "The password you've entered is incorrect" : "Complete field"
            msg =  document.getElementById(field)
            msg.innerHTML = field
            return
        }

        const body = {
            "username": field_email.value.trim(),
            "password": field_password.value.trim()
        }
        loader.style.display = "flex"
        const response = await fetch("/data",{
            method: "POST",
            body: JSON.stringify(body),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        let res = await response.json()
        res = await res
        
        loader.style.display = "none"
        if(res.status === 400){
            main.classList.remove("main")
            main.classList.add("errorLogin")
            main.children[1].style.display = "none"

            if(res.field=="pass"){
                msg = document.getElementById("msgPass")
            }else{
                msg = document.getElementById("msgMail")
            }
            msg.innerHTML = res.error
        }
        i=1
    }
}

const reset_alerts = ()=>{
    document.getElementById("msgPass").innerHTML = ""
    document.getElementById("msgMail").innerHTML = ""
}