// Cria o botão
var button = document.createElement("button");
// Define um texto para o botão
button.innerText = "Botão";
// Captura a tag "body"
var body = document.getElementsByTagName("body")[0];
// Adiciona à tag body o botão
body.appendChild(button);
// Inicia um evento que captura o click no botao
button.addEventListener ("click", function() {
    //Remove o botão ao clicar
    body.removeChild(button)
});
