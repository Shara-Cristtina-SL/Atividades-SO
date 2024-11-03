import time 

def executando_tarefa (tempo_de_execucao):
    print("Iniciando tarefa...")

    for i in range(tempo_de_execucao):
        time.sleep(1)
        print(f"Tarefa em progresso: {i+1}/{tempo_de_execucao}")

    print("Tarefa concluida!")

def main():
    tarefa_em_execucao = executando_tarefa(4)

main()
