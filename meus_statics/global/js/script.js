let quant = 0
var buttonsClicked =[]
document.getElementById("finalizar").addEventListener("click", finalizar);
function finalizar(){
    window.location.href = "/pagamento?finalizar=" + buttonsClicked.join(",");
}

let valor_a1 = 0
document.getElementById("A1").addEventListener("click", a1);
function a1() {
    valor_a1 = valor_a1 + parseFloat(document.getElementById("A1").value)
    console.log(valor_a1)
    if (valor_a1 % 2 != 0) {
        document.getElementById("A1").classList.add("btn-dark");
        document.getElementById("A1").classList.remove("btn-danger");
        console.log('if')
        quant = quant + 1
        console.log('quant' + quant)
        buttonsClicked.push('a1')
    }
    else {
        console.log('else')
        document.getElementById("A1").classList.add("btn-danger");
        document.getElementById("A1").classList.remove("btn-dark");
        quant = quant - 1
        console.log('quant' + quant)
    }
}
let valor_a2 = 0
document.getElementById("A2").addEventListener("click", a2);
function a2() {
    valor_a2 = valor_a2 + parseFloat(document.getElementById("A2").value)
    console.log(valor_a2)
    if (valor_a2 % 2 != 0) {
        document.getElementById("A2").classList.add("btn-dark");
        document.getElementById("A2").classList.remove("btn-danger");
        console.log('if')
        quant = quant + 1
        console.log('quant' + quant)
        localStorage={"aceito":'a2'}
    }
    else {
        console.log('else')
        document.getElementById("A2").classList.add("btn-danger");
        document.getElementById("A2").classList.remove("btn-dark");
        quant = quant - 1
        console.log('quant' + quant)
    }
}
let valor_a3 = 0
document.getElementById("A3").addEventListener("click", a3);
function a3() {
    valor_a3 = valor_a3 + parseFloat(document.getElementById("A3").value)
    console.log(valor_a3)
    if (valor_a3 % 2 != 0) {
        document.getElementById("A3").classList.add("btn-dark");
        document.getElementById("A3").classList.remove("btn-danger");
        console.log('if')
        quant = quant + 1
        console.log('quant' + quant)
    }
    else {
        console.log('else')
        document.getElementById("A3").classList.add("btn-danger");
        document.getElementById("A3").classList.remove("btn-dark");
        quant = quant - 1
        console.log('quant' + quant)
    }
}
let valor_a4 = 0
document.getElementById("A4").addEventListener("click", a4);
function a4() {
    valor_a4 = valor_a4 + parseFloat(document.getElementById("A4").value)
    console.log(valor_a4)
    if (valor_a4 % 2 != 0) {
        document.getElementById("A4").classList.add("btn-dark");
        document.getElementById("A4").classList.remove("btn-danger");
        console.log('if')
        quant = quant + 1
        console.log('quant' + quant)
    }
    else {
        console.log('else')
        document.getElementById("A4").classList.add("btn-danger");
        document.getElementById("A4").classList.remove("btn-dark");
        quant = quant - 1
        console.log('quant' + quant)
    }
}
let valor_a5 = 0
document.getElementById("A5").addEventListener("click", a5);
function a5() {
    valor_a5 = valor_a5 + parseFloat(document.getElementById("A5").value)
    console.log(valor_a5)
    if (valor_a5 % 2 != 0) {
        document.getElementById("A5").classList.add("btn-dark");
        document.getElementById("A5").classList.remove("btn-danger");
        console.log('if')
        quant = quant + 1
        console.log('quant' + quant)
    }
    else {
        console.log('else')
        document.getElementById("A5").classList.add("btn-danger");
        document.getElementById("A5").classList.remove("btn-dark");
        quant = quant - 1
        console.log('quant' + quant)
    }
}
let valor_a6 = 0
document.getElementById("A6").addEventListener("click", a6);
function a6() {
    valor_a6 = valor_a6 + parseFloat(document.getElementById("A6").value)
    console.log(valor_a6)
    if (valor_a6 % 2 != 0) {
        document.getElementById("A6").classList.add("btn-dark");
        document.getElementById("A6").classList.remove("btn-danger");
        console.log('if')
        quant = quant + 1
        console.log('quant' + quant)
    }
    else {
        console.log('else')
        document.getElementById("A6").classList.add("btn-danger");
        document.getElementById("A6").classList.remove("btn-dark");
        quant = quant - 1
        console.log('quant' + quant)
    }
}
let valor_b1 = 0
document.getElementById("B1").addEventListener("click", b1);
function b1() {
    valor_b1 = valor_b1 + parseFloat(document.getElementById("B1").value)
    console.log(valor_b1)
    if (valor_b1 % 2 != 0) {
        document.getElementById("B1").classList.add("btn-dark");
        document.getElementById("B1").classList.remove("btn-danger");
        console.log('if')
        quant = quant + 1
        console.log('quant' + quant)
    }
    else {
        console.log('else')
        document.getElementById("B1").classList.add("btn-danger");
        document.getElementById("B1").classList.remove("btn-dark");
        quant = quant - 1
        console.log('quant' + quant)
    }
}
let valor_b2 = 0
document.getElementById("B2").addEventListener("click", b2);
function b2() {
    valor_b2 = valor_b2 + parseFloat(document.getElementById("B2").value)
    console.log(valor_b2)
    if (valor_b2 % 2 != 0) {
        document.getElementById("B2").classList.add("btn-dark");
        document.getElementById("B2").classList.remove("btn-danger");
        console.log('if')
        quant = quant + 1
        console.log('quant' + quant)
    }
    else {
        console.log('else')
        document.getElementById("B2").classList.add("btn-danger");
        document.getElementById("B2").classList.remove("btn-dark");
        quant = quant - 1
        console.log('quant' + quant)
    }
}
let valor_b3 = 0
document.getElementById("B3").addEventListener("click", b3);
function b3() {
    valor_b3 = valor_b3 + parseFloat(document.getElementById("B3").value)
    console.log(valor_b3)
    if (valor_b3 % 2 != 0) {
        document.getElementById("B3").classList.add("btn-dark");
        document.getElementById("B3").classList.remove("btn-danger");
        console.log('if')
        quant = quant + 1
        console.log('quant' + quant)
    }
    else {
        console.log('else')
        document.getElementById("B3").classList.add("btn-danger");
        document.getElementById("B3").classList.remove("btn-dark");
        quant = quant - 1
        console.log('quant' + quant)
    }
}
let valor_b4 = 0
document.getElementById("B4").addEventListener("click", b4);
function b4() {
    valor_b4 = valor_b4 + parseFloat(document.getElementById("B4").value)
    console.log(valor_b4)
    if (valor_b4 % 2 != 0) {
        document.getElementById("B4").classList.add("btn-dark");
        document.getElementById("B4").classList.remove("btn-danger");
        console.log('if')
        quant = quant + 1
        console.log('quant' + quant)
    }
    else {
        console.log('else')
        document.getElementById("B4").classList.add("btn-danger");
        document.getElementById("B4").classList.remove("btn-dark");
        quant = quant - 1
        console.log('quant' + quant)
    }
}
let valor_b5 = 0
document.getElementById("B5").addEventListener("click", b5);
function b5() {
    valor_b5 = valor_b5 + parseFloat(document.getElementById("B5").value)
    console.log(valor_b5)
    if (valor_b5 % 2 != 0) {
        document.getElementById("B5").classList.add("btn-dark");
        document.getElementById("B5").classList.remove("btn-danger");
        console.log('if')
        quant = quant + 1
        console.log('quant' + quant)
    }
    else {
        console.log('else')
        document.getElementById("B5").classList.add("btn-danger");
        document.getElementById("B5").classList.remove("btn-dark");
        quant = quant - 1
        console.log('quant' + quant)
    }
}
let valor_b6 = 0
document.getElementById("B6").addEventListener("click", b6);
function b6() {
    valor_b6 = valor_b6 + parseFloat(document.getElementById("B6").value)
    console.log(valor_b6)
    if (valor_b6 % 2 != 0) {
        document.getElementById("B6").classList.add("btn-dark");
        document.getElementById("B6").classList.remove("btn-danger");
        console.log('if')
        quant = quant + 1
        console.log('quant' + quant)
    }
    else {
        console.log('else')
        document.getElementById("B6").classList.add("btn-danger");
        document.getElementById("B6").classList.remove("btn-dark");
        quant = quant - 1
        console.log('quant' + quant)
    }
}
let valor_c1 = 0
document.getElementById("C1").addEventListener("click", c1);
function c1() {
    valor_c1 = valor_c1 + parseFloat(document.getElementById("C1").value)
    console.log(valor_c1)
    if (valor_c1 % 2 != 0) {
        document.getElementById("C1").classList.add("btn-dark");
        document.getElementById("C1").classList.remove("btn-danger");
        console.log('if')
        quant = quant + 1
        console.log('quant' + quant)
    }
    else {
        console.log('else')
        document.getElementById("C1").classList.add("btn-danger");
        document.getElementById("C1").classList.remove("btn-dark");
        quant = quant - 1
        console.log('quant' + quant)
    }
}
let valor_c2 = 0
document.getElementById("C2").addEventListener("click", c2);
function c2() {
    valor_c2 = valor_c2 + parseFloat(document.getElementById("C2").value)
    console.log(valor_c2)
    if (valor_c2 % 2 != 0) {
        document.getElementById("C2").classList.add("btn-dark");
        document.getElementById("C2").classList.remove("btn-danger");
        console.log('if')
        quant = quant + 1
        console.log('quant' + quant)
    }
    else {
        console.log('else')
        document.getElementById("C2").classList.add("btn-danger");
        document.getElementById("C2").classList.remove("btn-dark");
        quant = quant - 1
        console.log('quant' + quant)
    }
}
let valor_c3 = 0
document.getElementById("C3").addEventListener("click", c3);
function c3() {
    valor_c3 = valor_c3 + parseFloat(document.getElementById("C3").value)
    console.log(valor_c3)
    if (valor_c3 % 2 != 0) {
        document.getElementById("C3").classList.add("btn-dark");
        document.getElementById("C3").classList.remove("btn-danger");
        console.log('if')
        quant = quant + 1
        console.log('quant' + quant)
    }
    else {
        console.log('else')
        document.getElementById("C3").classList.add("btn-danger");
        document.getElementById("C3").classList.remove("btn-dark");
        quant = quant - 1
        console.log('quant' + quant)
    }
}
let valor_c4 = 0
document.getElementById("C4").addEventListener("click", c4);
function c4() {
    valor_c4 = valor_c4 + parseFloat(document.getElementById("C4").value)
    console.log(valor_c4)
    if (valor_c4 % 2 != 0) {
        document.getElementById("C4").classList.add("btn-dark");
        document.getElementById("C4").classList.remove("btn-danger");
        console.log('if')
        quant = quant + 1
        console.log('quant' + quant)
    }
    else {
        console.log('else')
        document.getElementById("C4").classList.add("btn-danger");
        document.getElementById("C4").classList.remove("btn-dark");
        quant = quant - 1
        console.log('quant' + quant)
    }
}
let valor_c5 = 0
document.getElementById("C5").addEventListener("click", c5);
function c5() {
    valor_c5 = valor_c5 + parseFloat(document.getElementById("C5").value)
    console.log(valor_c5)
    if (valor_c5 % 2 != 0) {
        document.getElementById("C5").classList.add("btn-dark");
        document.getElementById("C5").classList.remove("btn-danger");
        console.log('if')
        quant = quant + 1
        console.log('quant' + quant)
    }
    else {
        console.log('else')
        document.getElementById("C5").classList.add("btn-danger");
        document.getElementById("C5").classList.remove("btn-dark");
        quant = quant - 1
        console.log('quant' + quant)
    }
}
let valor_c6 = 0
document.getElementById("C6").addEventListener("click", c6);
function c6() {
    valor_c6 = valor_c6 + parseFloat(document.getElementById("C6").value)
    console.log(valor_c6)
    if (valor_c6 % 2 != 0) {
        document.getElementById("C6").classList.add("btn-dark");
        document.getElementById("C6").classList.remove("btn-danger");
        console.log('if')
        quant = quant + 1
        console.log('quant' + quant)
    }
    else {
        console.log('else')
        document.getElementById("C6").classList.add("btn-danger");
        document.getElementById("C6").classList.remove("btn-dark");
        quant = quant - 1
        console.log('quant' + quant)
    }
}
let valor_d1 = 0
document.getElementById("D1").addEventListener("click", d1);
function d1() {
    valor_d1 = valor_d1 + parseFloat(document.getElementById("D1").value)
    console.log(valor_d1)
    if (valor_d1 % 2 != 0) {
        document.getElementById("D1").classList.add("btn-dark");
        document.getElementById("D1").classList.remove("btn-danger");
        console.log('if')
        quant = quant + 1
        console.log('quant' + quant)
    }
    else {
        console.log('else')
        document.getElementById("D1").classList.add("btn-danger");
        document.getElementById("D1").classList.remove("btn-dark");
        quant = quant - 1
        console.log('quant' + quant)
    }
}
let valor_d2 = 0
document.getElementById("D2").addEventListener("click", d2);
function d2() {
    valor_d2 = valor_d2 + parseFloat(document.getElementById("D2").value)
    console.log(valor_d2)
    if (valor_d2 % 2 != 0) {
        document.getElementById("D2").classList.add("btn-dark");
        document.getElementById("D2").classList.remove("btn-danger");
        console.log('if')
        quant = quant + 1
        console.log('quant' + quant)
    }
    else {
        console.log('else')
        document.getElementById("D2").classList.add("btn-danger");
        document.getElementById("D2").classList.remove("btn-dark");
        quant = quant - 1
        console.log('quant' + quant)
    }
}
let valor_d3 = 0
document.getElementById("D3").addEventListener("click", d3);
function d3() {
    valor_d3 = valor_d3 + parseFloat(document.getElementById("D3").value)
    console.log(valor_d3)
    if (valor_d3 % 2 != 0) {
        document.getElementById("D3").classList.add("btn-dark");
        document.getElementById("D3").classList.remove("btn-danger");
        console.log('if')
        quant = quant + 1
        console.log('quant' + quant)
    }
    else {
        console.log('else')
        document.getElementById("D3").classList.add("btn-danger");
        document.getElementById("D3").classList.remove("btn-dark");
        quant = quant - 1
        console.log('quant' + quant)
    }
}
let valor_d4 = 0
document.getElementById("D4").addEventListener("click", d4);
function d4() {
    valor_d4 = valor_d4 + parseFloat(document.getElementById("D4").value)
    console.log(valor_d4)
    if (valor_d4 % 2 != 0) {
        document.getElementById("D4").classList.add("btn-dark");
        document.getElementById("D4").classList.remove("btn-danger");
        console.log('if')
        quant = quant + 1
        console.log('quant' + quant)
    }
    else {
        console.log('else')
        document.getElementById("D4").classList.add("btn-danger");
        document.getElementById("D4").classList.remove("btn-dark");
        quant = quant - 1
        console.log('quant' + quant)
    }
}
let valor_d5 = 0
document.getElementById("D5").addEventListener("click", d5);
function d5() {
    valor_d5 = valor_d5 + parseFloat(document.getElementById("D5").value)
    console.log(valor_d5)
    if (valor_d5 % 2 != 0) {
        document.getElementById("D5").classList.add("btn-dark");
        document.getElementById("D5").classList.remove("btn-danger");
        console.log('if')
        quant = quant + 1
        console.log('quant' + quant)
    }
    else {
        console.log('else')
        document.getElementById("D5").classList.add("btn-danger");
        document.getElementById("D5").classList.remove("btn-dark");
        quant = quant - 1
        console.log('quant' + quant)
    }
}
let valor_d6 = 0
document.getElementById("D6").addEventListener("click", d6);
function d6() {
    valor_d6 = valor_d6 + parseFloat(document.getElementById("D6").value)
    console.log(valor_d6)
    if (valor_d6 % 2 != 0) {
        document.getElementById("D6").classList.add("btn-dark");
        document.getElementById("D6").classList.remove("btn-danger");
        console.log('if')
        quant = quant + 1
        console.log('quant' + quant)
    }
    else {
        console.log('else')
        document.getElementById("D6").classList.add("btn-danger");
        document.getElementById("D6").classList.remove("btn-dark");
        quant = quant - 1
        console.log('quant' + quant)
    }
}
