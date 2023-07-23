document.addEventListener("DOMContentLoaded", function(){

    let lugares_selecionados = []

    const assentos = document.querySelectorAll('.assento');
    
    const seleciona_lugar = ({target}) => {
        // Colocar a interação do botão aqui dentro, oque ele deve fazer

        let assentoId = target.getAttribute('id')
        let inputLugaresSelecionados = document.getElementById('lugaresSelecionados');
        console.log(assentoId)
        // Alterna entre as classes que dão a cor para o assento
        target.classList.toggle("btn-danger");
        target.classList.toggle("btn-dark");

        // Verifica se o assento foi selecionado pelo usuário
        if(lugares_selecionados.includes(assentoId)){
            //Caso já tenha sido selecionado pelo usuário, será removido do array
            let index = lugares_selecionados.indexOf(assentoId);
            lugares_selecionados.splice(index, 1);
        }else{
            //Caso não tenha sido selecionado pelo usuário, será adicionado ao array
            lugares_selecionados.push(assentoId);
        }
        console.log(lugares_selecionados)
        inputLugaresSelecionados.value = lugares_selecionados;
        
    }

    //Atribui o evento de click a todos os botões de assento
    assentos.forEach((element) => {
        element.addEventListener('click', seleciona_lugar);
    })
});