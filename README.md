Quiz Interativo em Python
Este repositório contém um simples quiz interativo desenvolvido em Python. O programa apresenta uma série de perguntas de múltipla escolha ao usuário e, ao final, informa a pontuação baseada nas respostas corretas.

🚀 Funcionalidades
Apresenta perguntas de múltipla escolha.
Verifica automaticamente as respostas do usuário.
Calcula e exibe a pontuação final.
Suporte para adicionar novas perguntas com facilidade.

📋 Pré-requisitos
Para executar este projeto, você precisa ter:

Python 3.x instalado no seu sistema.

🛠️ Como Executar
Clone este repositório:

bash
Copiar código
git clone https://github.com/seu-usuario/nome-do-repositorio.git  
Navegue até o diretório do projeto:

bash
Copiar código
cd nome-do-repositorio  
Execute o arquivo principal:

bash
Copiar código
python quiz.py  
Siga as instruções exibidas no terminal para responder às perguntas do quiz.

🧩 Estrutura do Código
Pergunta: Uma classe que representa cada pergunta do quiz, contendo:
O texto da pergunta (prompt).
A resposta correta (resposta).
questao_prompts: Lista com os textos das perguntas.
perguntas: Lista de objetos Pergunta, vinculando cada pergunta ao texto e à resposta correta.
run_test: Função principal que executa o quiz, recebe as respostas do usuário e calcula a pontuação.
📝 Como Adicionar Mais Perguntas
Adicione o texto da nova pergunta à lista questao_prompts, seguindo o formato das perguntas existentes.
Crie um novo objeto da classe Pergunta na lista perguntas, vinculando o texto da pergunta e a resposta correta.
Exemplo:

python
Copiar código
questao_prompts.append("Qual a cor da uva?\n(a) Roxa\n(b) Vermelha\n(c) Azul\n\n")  
perguntas.append(Pergunta(questao_prompts[4], "a"))  
📂 Exemplo de Saída
text
Copiar código
Qual a cor da maçã ?  
(a) Vermelho/Verde  
(b) Rosa  
(c) Orange  

Resposta: a  

Qual a cor da Banana ?  
(a) Azul  
(b) Cinza  
(c) Amarelo  

Resposta: c  

Você acertou 2/2 Correto  
🤝 Contribuindo
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.
