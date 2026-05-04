import re
from datetime import datetime

def calculate_hours():
    print("--- Calculadora de Horas Trabalhadas ---")
    text = input("Insira os dados do ponto aqui:\nex: hh:mm:ss hh:mm:ss\n> ")
    
    times = re.findall(r'(\d{2}:\d{2}:\d{2})', text)
    
    if not times:
        print("Nenhum horário encontrado. Verifique o formato.")
        return

    times.sort()
    
    fmt = '%H:%M:%S'
    total_seconds = 0
    
    print("\nResumo do dia:")
    for i in range(0, len(times), 2):
        try:
            start_str = times[i]
            end_str = times[i+1]
            
            start = datetime.strptime(start_str, fmt)
            end = datetime.strptime(end_str, fmt)
            
            diff = (end - start).total_seconds()
            total_seconds += diff
            
            print(f"  {start_str} -> {end_str} | Subtotal: {int(diff//3600):02d}h {int((diff%3600)//60):02d}m")
            
        except IndexError:
            print(f"{times[i]} -> [Falta saída]")

    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)
    
    print("-" * 30)
    print(f"TOTAL TRABALHADO: {hours:02d}:{minutes:02d}:{seconds:02d}")
    print("-" * 30)

if __name__ == "__main__":
    calculate_hours()