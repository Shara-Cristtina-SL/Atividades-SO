import threading
import time

lock = threading.Lock()

def tarefa(nome,tempo_parado):
    global lock
    contador = 1
#Cada tarefa tem 3 threads
    while contador !=4:
        print(f"Executando {nome}; contagem de thereads dessa tarefa = {contador}")
        time.sleep(tempo_parado)
        contador += 1


if __name__ == "__main__":
    threads = []
    tempo_parado = 1
    for i in range(3):
        t = threading.Thread(target=tarefa, args=(f"Tarefa {i}", tempo_parado))
        threads.append(t)
        t.start()
        tempo_parado+=1

    # Aguarde todas as threads terminarem
    for t in threads:
        t.join()

print("Todas as tarefas e suas threads foram executadas!")
