// ouvinte de eventos de clique
document.addEventListener("DOMContentLoaded", function(event){

    let lugares_selecionados = []

    // seleciona todos os elementos do html que possuem a class assentos e armazena em assentos
    const assentos = document.querySelectorAll('.assento');
    
    // função que recebe um obj de evento como paramentro (executa quando um btn for clicado)
    const seleciona_lugar = ({target}) => {
        console.log(target);

        // Verifica se o botão já possui a classe "btn-dark" ou seja, verifica se foi selecionado
        // se sim isSelected recebe true
       const isSelected = target.classList.contains('btn-dark');

        // Adiciona ou remove o elemento target de lugares_selecionados com base no estado atual do botão
        //  se true adiciona o target em lugares_selecionados
        if (!isSelected) {
            lugares_selecionados.push(target);
        }
        // se n, remove de lugares selecionados
        else {
            // coleta a posição do target
            const index = lugares_selecionados.indexOf(target);
            if (index > -1) {
                // remove de lugares selecionados
                lugares_selecionados.splice(index, 1);
            }
        }

        
        // Adiciona ou remove a classe "btn-dark" com base no estado atual do botão (selecionado ou não)
        target.classList.toggle('btn-dark', !isSelected);
        console.log('lugares selecionados: ', lugares_selecionados);
    }

    // ouvinte que verifica a interação com os botoes com class assento e encaminha para a função quando clicados
    assentos.forEach((element) => {
        element.addEventListener('click', seleciona_lugar)
    })

});