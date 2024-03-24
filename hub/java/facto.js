//botões do início
//hub

//Botão de cima
function mostre2(){
    var bloco2 = document.getElementById("pronto2")
    var bot2 = document.getElementById("bu")
    var est2 = getComputedStyle(document.documentElement).getPropertyValue("--branco")

    if(bloco2.style.display ==="none"){
        //seção
        bloco2.style.display = "block"
        bloco2.style.backgroundColor = "#d56a13"
        //botão
        //borda
        bot2.style.borderTopRightRadius = "0px"
        bot2.style.borderBottomRightRadius = "0px"
        //cor
        bot2.style.backgroundColor = "#292929"
        bot2.style.color = "#ffff"
    } else{
        //seção
        bloco2.style.display = "none"
        bloco2.style.backgroundColor = "#ff7f17"
        //botão
        bot2.style.borderTopRightRadius = "10px"
        bot2.style.borderBottomRightRadius = "10px"
         //cor
         bot2.style.backgroundColor = "#ffffff"
         bot2.style.color = "#292929" 
    }
}
//Botão debaixo
function mostre(){
    var bloco = document.getElementById("pronto");
    var bot = document.getElementById("bu1")

    if(bloco.style.display === "none"){
        //seção
        bloco.style.display = "block"
        bloco.style.backgroundColor = "#d56a13"
        //botão
        //borda
        bot.style.borderTopRightRadius = "0px"
        bot.style.borderBottomRightRadius = "0px"
        //cor
        bot.style.backgroundColor = "#292929"
        bot.style.color = "#ffff"
    }else{
        //seção
        bloco.style.display = "none"
        bloco.style.backgroundColor = "#ff7f17"
        //botão
        //borda
        bot.style.borderTopRightRadius = "10px"
        bot.style.borderBottomRightRadius = "10px"
        //cor
        bot.style.backgroundColor = "#ffff"
        bot.style.color = "#292929"
    };
}    
//hub

function mostre3() {
    var bloco3 = document.getElementById("pronto3")
    var div = document.getElementById("di1")

    if(bloco3.style.display === "none")
    {
        bloco3.style.display = "block"
        div.style.height = "auto"
        div.style.width = "533.073px"
    }else{
        bloco3.style.display = "none" 
        div.style.height = "115px"
        div.style.width = "auto"
    }
}