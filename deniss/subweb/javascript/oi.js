function mos() {
    var aparecer = document.getElementById("olhe")
    var tam = document.getElementById("top")

    if(aparecer.style.display === "grid"){
        aparecer.style.display = "none"
        tam.style.width = "auto"
    }else{
        aparecer.style.display = "grid"
        tam.style.width = "477.5px"
    }
}
function mos1(){
    var apa1 = document.getElementById("olhe1")
}