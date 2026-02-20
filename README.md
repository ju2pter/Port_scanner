Email Sender & Port Scanner

Este projeto consiste em dois scripts Python: um para envio de e-mails com suporte a anexos (email_sender.py) e outro para escanear portas em IPs ou redes (port_scanner.py). Ambos foram desenvolvidos com foco na simplicidade, modularidade e boas práticas.

Features

Email Sender

Envia e-mails com corpo de texto simples.

Suporte para anexar arquivos.

Configuração via variáveis de ambiente para maior segurança.

Tratamento de erros para melhor experiência do usuário.


Port Scanner

Verifica se portas específicas estão abertas em um IP ou faixa de IPs.

Suporte para range de portas ou listas de portas.

Utiliza ThreadPoolExecutor para execução paralela e maior eficiência.


Requisitos

Certifique-se de ter instalado:

Python 3.7+

As bibliotecas listadas em requirements.txt


Instalação

Clone o repositório:

git clone https://github.com/seuusuario/email-port-scanner.git
cd email-port-scanner

Instale as dependências:

pip install -r requirements.txt

Configure as variáveis de ambiente:

Copie o arquivo .env.var e renomeie para .env:

cp .env.example .env

Preencha os valores de EMAIL_USER e EMAIL_PASS com suas credenciais de e-mail.

Uso

Email Sender

Execute o script:

python email_sender.py

Insira as informações solicitadas:

Endereço de e-mail do destinatário.

Assunto e mensagem do e-mail.

Caminho do arquivo para anexar (opcional).

O script enviará o e-mail e exibirá o status na tela.


Port Scanner

Execute o script:

python port_scanner.py

Insira as informações solicitadas:

IP ou rede (ex.: 192.168.0.1 ou 192.168.0.0/24).

Portas para verificar (ex.: 22, 80, 443 ou 1-1024).

O scanner exibirá as portas abertas no terminal.

Estrutura do Projeto

project/
├── .env.var             # Exemplo de configuração para variáveis de ambiente
├── email_sender.py      # Script para envio de e-mails 
├── port_scanner.py      # Script para scanner de portas
├── requirements.txt     # Dependências do projeto
└── README.md            # Documentação do projeto


Contribuições

Contribuições são bem-vindas! Siga os passos abaixo para contribuir:

Fork este repositório.

Crie uma branch para sua feature ou correção:

git checkout -b minha-feature

Faça commit de suas alterações:

git commit -m "Adicionei minha feature"

Envie para a branch principal:

git push origin minha-feature

Abra um Pull Request.


Licença

Este projeto está licenciado sob a MIT License. Consulte o arquivo LICENSE para mais informações.
