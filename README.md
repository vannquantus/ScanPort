### PROJETO SCANPORT ###


O projeto implementa um simples scanner de portas utilizando Python. O scanner verifica se determinadas portas de um servidor ou host estão abertas ou fechadas. A funcionalidade pode ser utilizada em qualquer host, incluindo servidores locais, sites na web ou endereços IP.

### TECNOLOGIAS UTILIZADAS ###
- **Python:** A linguagem de programação usada para escrever o código.
- **Socket:** Biblioteca utilizada para criar conexões de rede e verificar a disponibilidade de portas.

### COMO FUNCIONA ###

O código realiza uma varredura em uma faixa de portas especificada e verifica se as portas estão abertas ou fechadas. Para cada porta, o programa tenta estabelecer uma conexão com o host na porta indicada. Se a conexão for bem sucedida, o código imprime que a porta está aberta; caso conrtário, que a porta está fechada.

### FUNCIONALIDADES ###

- **Scan de Portas:** Permite escanear uma faixa de portas de um host, como por exemplo de 70 a 90.
- **Configuração de Timeout:** Permite definir um tempo limite para a tentativa de conexão, evitando que o processo de verificação de portas seja muito lento.
- **Exibição de Resultados:** O programa exibe no terminal se as portas estão abertas ou fechadas.

### COMO USAR ###

1. Cole o repositório ou faça download dos arquivos:
   git clone https://github.com/vannquantus/ScanPort.git

2. Navegue até o diretório do projeto
   cd ScanPort

3. Execute o código passando o nome do host e a faixa de portas:
   python ScanPort.py




