# DuplaDeDois
### Trabalho de conclusão do curso de Python - Senac Tech RS

Este é um prototipo de um site de vendas de ingressos de cinema, realizado inicialmente em dupla (por isso o nome).
A ideia é simular todo o processo de compra dos ingressos e armazenar no banco de dados para resgate dos ingressos vendidos em futuras compras.
Permite que o usuário realize o cadastro e, posteriormente, o login e logout.

> Status do Projeto: Em desenvolvimento :warning:
> Embora o curso já tenha acabado, pretendo continuar desenvolvendo o projeto individualmente.


## Como executar:
### 1. Crie um clone em sua máquina 
> É necessário instalar o [Git](https://git-scm.com/downloads)
  
  Após instalado, abra o prompt (terminal) e digite:

   ```
   git clone https://github.com/LucasBoelter/Onibus
   ```

### 2. Criando Ambiente Virtual
  É necessario criar um ambiente virtual então, dentro do clone crie o venv.<br>
  Para criar o venv basta abrir o termina, entrar no clone e digitar:
 
    python -m venv .venv

### 3. Inicializando o Ambiente Virtual
  Para iniciar digite: **(windows)**<br>
    
    .venv\Scripts\activate
    
  Você verá que tem um "(.venv)" antes do caminho do diretorio em que você esta.
  <br>
  E para desativar, digite:
    
    deactivate

### 4. Instalando os requisitos:<br>
  > Arquivo: requisitos.txt
    
    python -r requisitos.txt

  Agora o ambiente esta pronto.

### 5. Executar:
  Para executar digite:<br>
  
    python manage.py runserver
    
### 6. Abra seu navegador em localhost:8000
