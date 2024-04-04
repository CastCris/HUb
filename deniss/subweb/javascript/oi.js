//Maais sobre
function mos() {
    var aparecer = document.getElementById("olhe")
    var tex = document.getElementById("ob1")
    var tam = document.getElementById("top")
    var bloq1 = document.getElementById("tampa1")
    var img = document.getElementById("locali")
    var lb = document.getElementById("localb1")
    var li = document.getElementById("geral")
    var uls = document.getElementById("conjunto")

    var a = 0
    var b = 0

    if(aparecer.style.display==="grid"){
        //Texto retração
        tex.style.display = "none"
        //tamanhos
        aparecer.style.height = "0px"
        aparecer.style.width = "0px"
        aparecer.style.padding = "0px"
        //animaçõs
        aparecer.style.animationName = "retrair1"
        //img
        img.style.display = "none"
        //Recuar//
        //bloquador
        bloq1.style.display = "grid"
        bloq1.style.animationName = "tampa1"
        //renicialzação das variáveis
        if(aparecer.style.animationName === "retrair1" && bloq1.style.animationName === "tampa1") {
            ++a
            if(a === 1){
                aparecer.style.display = "none"
                bloq1.style.display = "none"
            }
        }
    }else{
        //texto expansão
        //tamanhos
        aparecer.style.display = "grid"
        aparecer.style.height = "1100px"
        aparecer.style.width = "354.023px"
        aparecer.style.padding = "10px"
        //animações
        aparecer.style.animationName = "expandir1"
        tex.style.display = "grid"
        //img
        img.style.display = "grid"
        //Recuar bloqueador
        bloq1.style.display = "grid"
        bloq1.style.animationName = "tampa1"
        tam.style.width = "477.5px"
    }
    
}
//Mais informações
function information(){
    
}
//Carreira política
function mos1(){
    var apa1 = document.getElementById("olhe1")

    if(apa1.style.display === "grid"){
        apa1.style.display = "none"
    } else{
        apa1.style.display = "grid"
    }
}