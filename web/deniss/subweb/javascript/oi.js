//Maais sobre
function mos() {
    var aparecer = document.getElementById("olhe")
    var tex = document.getElementById("ob1")
    var tam = document.getElementById("top")
    var bloq1 = document.getElementById("tampa1")
    var img = document.getElementById("locali")
    //informação
    var infob = document.getElementById("info_localb")
    var infom = document.getElementById("info_sobre")
    var info = document.getElementById("info")

    var a = 0

    if (aparecer.style.display === "flow") {
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
        //Info
        info.style.display = "none"
        info.style.animationName = "volta"
        //botão_info
        infob.style.animationName = "desa"
        infob.style.opacity = "0"
        infob.style.animationDuration = "2s"
        //cconteúdo_info
        info.style.display = ""
        infom.style.animationName = "desa"
        infom.style.opacity = "0"
        infom.style.animationDuration = "2s"
        //renicialzação das variáveis
        if (aparecer.style.animationName === "retrair1" && bloq1.style.animationName === "tampa1") {
            ++a
            if (a === 1) {
                aparecer.style.display = "none"
                bloq1.style.display = "none"
            }
        }
    } else {
        //texto expansão
        //tamanhos
        aparecer.style.display = "flow"
        aparecer.style.height = "843.562px"
        aparecer.style.width = "354.023px"
        aparecer.style.padding = "10px"
        //animações
        aparecer.style.animationName = "expandir1"
        tex.style.display = "grid"
        //img
        img.style.display = "flow"
        //Recuar bloqueador
        bloq1.style.display = "grid"
        bloq1.style.animationName = "tampa1"
        tam.style.width = "auto"
        //info
        info.style.display = "block"
        info.style.animationName = "tampar"
        info.style.width = "255.896px"
        //botão_info
        infob.style.display = "block"
        infob.style.animationName = "surgir"
        infob.style.opacity = "1"
        //conteúdo_info
        infom.style.animationName = "surgir"
        infom.style.opacity = "1"
    }
}
//Mais informações
function information() {
    //olhe
    var aparecero = document.getElementById("olhe")
    var aparecer = document.getElementById("info_mais")
    var preen = document.getElementById("informacao_con")
    var gira = document.getElementById("roda")
    //info_seta
    var locse = document.getElementById("info_local_seta")

    if (aparecero.style.display === "flow") {
        if (aparecer.style.display === "grid") {
            //preenchimentos
            preen.style.padding = "0px"
            //aparecerinfo
            aparecer.style.display = "none"
            //giragira
            gira.style.rotate = "0deg"
            gira.style.animationName = "retorna"
            //seta
            locse.style.display = "none"
        } else {
            //preenchimentos
            preen.style.padding = "20px"

            aparecer.style.display = "grid"
            gira.style.rotate = "180deg"
            gira.style.animationName = "rodaroda"
            locse.style.display = "flex"
        }
    }
}
//seta
//esquerda
var e = 0
function esq(){
    ++e 
    return e
}
//direita
function dir(){
    ++d
    return d
}
var di = e-d
//Ações
//infos
var mais = document.getElementById("info_mais")
var poli = document.getElementById("info_parti")
//<---
if(e === 1){
    //mais sobre
    mais.style.opacity = "0"
    mais.style.animationName = "esq"
    mais.style.width = "0px"
    mais.style.height = "0px"
    //politico
    poli.style.animationName = "dir"
    poli.style.width = "auto"
    poli.style.height = "auto"
    poli.style.opacity = "1"
}
//--->
if(e === 0){
    //mais sobre
    mais.style.opacity = "1"
    mais.style.animationName = "esdir"
    mais.style.width = "auto"
    mais.style.height = "auto"
    //politico
}
//Carreira política
function mos1() {
    var apa1 = document.getElementById("olhe1")

    if (apa1.style.display === "grid") {
        apa1.style.display = "none"
    } else {
        apa1.style.display = "grid"
    }
}