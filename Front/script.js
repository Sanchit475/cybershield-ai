const API = "https://YOUR-CODESPACE-3000.app.github.dev"

async function signup(){

let email=document.getElementById("email").value
let password=document.getElementById("password").value

await fetch(API+"/signup",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({email,password})
})

alert("User created")
}

async function scanURL(){

let url=document.getElementById("url").value

let res=await fetch(API+"/scan-url",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({url})
})

let data=await res.json()

document.getElementById("urlres").innerText=data.result
}

async function checkEmail(){

let email=document.getElementById("email2").value

let res=await fetch(API+"/check-email",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({email})
})

let data=await res.json()

document.getElementById("emailres").innerText=data.result
}

async function askAI(){

let q=document.getElementById("q").value

let res=await fetch(API+"/ai",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({question:q})
})

let data=await res.json()

document.getElementById("aires").innerText=data.answer
}