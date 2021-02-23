function func() {
    var privateVar = 10;

    function sumOne() {
        privateVar++;
        console.log(privateVar);
    }    
    return sumOne;
}

// Soma 1 a
var v = func();
v();

privateVar = 5;
console.log(privateVar);

v();

// Percebe-se que não é possível modificar a varíavel "privateVar" da funcao func() fora da função, a única maneira de modifica-la é usando func().
// A variavel "privateVar" da linha 15, é uma variavel global com o mesmo nome da variável privada de func(). Apesar de ter o mesmo nome não são a mesma.

