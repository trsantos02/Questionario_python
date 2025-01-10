
from Pergunta import Pergunta


questao_prompts = [
    "Qual a cor da maçã ?\n(a) Vermelho/Verde\n(b) Rosa \n(c) Orange\n\n",
    "Qual a cor da Banana ?\n(a) Azul\n(b) Cinza \n(c) Amarelo\n\n",
    "Qual a cor do morango ?\n(a) Amarelo\n(b) Vermelho \n(c) Azul\n\n",
    "Qual a cor da melancia ?\n(a) Amarelo\n(b) Verde \n(c) Azul\n\n"
]

#Posso adicionar mais questões.
perguntas = [
    Pergunta(questao_prompts[0], "a"),
    Pergunta(questao_prompts[1], "c"),
    Pergunta(questao_prompts[2], "b"),
    Pergunta(questao_prompts[3], "b")
]

def run_test (perguntas):
    score = 0 
    for pergunta in perguntas:
        resposta = input(pergunta.prompt)
        if resposta == pergunta.resposta:
            score += 1
    print("Voce acertou " + str(score) + "/" + str(len(perguntas)) + " Correto")     


run_test(perguntas)    
