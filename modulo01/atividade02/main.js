
//exercicio

/*
1. Função para somar dois números
Crie uma função chamada somar que recebe dois números como parâmetros e
retorna a soma deles. 

function soma(n1, n2) {
  return n1 + n2
}

let resul = soma(2, 2)
alert(resul)
*/

/*2. Função para verificar se um número é par ou ímpar
Crie uma função chamada verificarParidade que recebe um número e retorna
"Par" se for par ou "Ímpar" se for ímpar.  


function verificarParidade(numero) {
  if(numero % 2 === 0){
    return 'Par'
  }else{
    return 'Ímpar'
  }
}

alert(verificarParidade(3))

*/

/*3. Função para encontrar o maior de dois números
Escreva uma função chamada maiorNumero que recebe dois números e retorna
o maior deles.  

function maiorNumero(n1, n2){
  if(n1 > n2){
    return 'O primeiro número é maior que o segundo: ' + n1 + " > " + n2
  }else{
    return 'O segundo número é maior que o primeiro: ' + n1 + " < " + n2
  }
}
alert(maiorNumero(4, 5))

*/

/*4. Função para contar quantos itens há em um array
Crie uma função chamada contarItens que recebe um array como parâmetro e
retorna a quantidade de itens nele.

function contarItens(array) {
  let incre = 0;
  for (let i = 0; i < array.length; i++) {
    incre++;
  }
  return incre;
}
const meuArray = [1, 2, 3, "a", "b", "jh"];
const quantidadeDeItens = contarItens(meuArray);
alert(quantidadeDeItens);*/


/*6. Função que retorna "Bom dia", "Boa tarde" ou "Boa noite"
Crie uma função chamada saudacao que recebe um horário (em horas) e
retorna a saudação correspondente. 

function saudacao(horas) {
  if(horas >=0 && horas < 12){
    return 'Bom Dia'
  }else if(horas >= 12 && horas < 18){
    return 'Boa Tarde'
  }else if(horas >=18 && horas < 23)
    return 'Boa Noite'
}

alert(saudacao(12))

*/

/*7. Função para calcular a média de um array de números
Crie uma função chamada calcularMedia que recebe um array de números e
retorna a média deles. 

function calcularMedia(array) {
  let cont = 0;
  let quant = 0;
  for (let i = 0; i < array.length; i++) {
    cont += array[i];
    quant = quant + 1;
  }
  return cont / quant;
}
let Myarray = [1, 2, 3, 4];
let quantidadeDeItens = calcularMedia(Myarray);
console.log(quantidadeDeItens.toFixed(2));
*/

/*8. Função que valida se um nome contém mais de 3 caracteres
Crie uma função chamada validarNome que recebe uma string e retorna
"Válido" se o nome tiver mais de 3 caracteres ou "Inválido" caso contrário.

function validarNome(nome) {
  if (nome.length > 3) {
    return("Valido");
  } else {
    return("Invalido");
  }
}
let nome = "julio";
let quantCaractere = validarNome(nome)
console.log(quantCaractere);

*/
