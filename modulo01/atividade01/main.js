/*1. Crie um programa que solicite ao usuário dois números e exiba o 
resultado da soma, subtração, multiplicação e divisão desses 
números.  

let n1 = Number(prompt("Digite um número"));
let n2 = Number(prompt("Digite outro Número"));

soma = n1 + n2;
subri = n1 - n2;
multi = n1 * n2;
div = n1 / n2;

alert(` soma: ${soma} 
    Subtração: ${subri}
    Multiplicação: ${multi}
    Divisão: ${div}`);
*/

/*2. Escreva um programa que pergunte ao usuário sua idade e 
imprima se ele é maior ou menor de idade. 

//usar o ternario: O operador ternário em JavaScript, também conhecido como operador condicional, é uma forma concisa de escrever uma expressão
//condicional if...else. Ele permite que você execute uma ação ou atribua um valor com base em uma condição em apenas uma linha.

let idade = Number(prompt("Digite sua idade"));
let resu = ((idade) >= 18) ? "Maior de idade" : "Menor de idade";
alert(resu);
*/

/*
3. Crie um programa que represente um livro, com propriedades 
para título, autor e número de páginas. Imprima cada propriedade 
no console.


let livro = {
    titulo: "O Pequeno Príncipe",
    autor: "Antoine de Saint-Exupéry",
    numPaginas: 96
  };
  
  console.log("Título:", livro.titulo);
  console.log("Autor:", livro.autor);
  console.log("Número de páginas:", livro.numPaginas); 
  */

/*
  4. Faça um script que pede duas notas de um aluno. Em seguida ele 
deve calcular a média do aluno e dar o seguinte resultado: 
 
•  A mensagem "Aprovado", se a média alcançada for maior ou 
igual a sete; 
•   A mensagem "Reprovado", se a média for menor do que sete; 
•   A mensagem "Aprovado com Distinção", se a média for igual a 
dez. 
  

let nota1 = 10;
let nota2 = 1;

let media = (nota1 + nota2) / 2;

if (media === 10) {
  console.log("Aprovado com Distinção");
} else if (media >= 7) {
  console.log("Aprovado");
} else if (media < 7) {
  console.log("Reprovado");
}
*/

/*
5.  Faça um script que leia três números inteiros e mostre o maior 
deles.


let n1 = 6;
let n2 = 4;
let n3 = 3;

if (n1 > n2 && n1 > n3) {
  console.log(n1);
} else if (n2 > n1 && n2 > n3) {
  console.log(n2);
} else {
  console.log(n3);
}
*/

/*
6. Crie um programa que peça ao usuário para digitar um número. O 
programa deve verificar se o número é: 
Par ou ímpar 
Positivo, negativo ou zero 


let n1 = -8;

let res = n1 % 2 === 0 ? "Numero PAR" : "Numero IMPAR";
if (n1 > 0) {
  console.log("Numero Positivo " + "e o  " + res);
} else if (n1 < 0) {
  console.log("Numero negativo " + "e o " + res);
} else if (n1 === 0) {
  console.log("Número igual a zero " + "e o  " + res);
}
  */
