import re
from datetime import datetime, timedelta
from scrapper import getToday


def parse_time(t):
    fmt = '%H:%M:%S' if len(t) == 8 else '%H:%M'
    return datetime.strptime(t, fmt)


def calculate_hours():
    print("--- Calculadora de Horas Trabalhadas ---")
    text = input("Insira os dados do ponto aqui:\nex: hh:mm ou hh:mm:ss\n> ")

    times = re.findall(r'(\d{2}:\d{2}(?::\d{2})?)', text)

    if not times:
        print("Nenhum horário encontrado. Verifique o formato.")
        return

    times.sort()

    total_seconds = 0

    print("\nResumo do dia:")
    for i in range(0, len(times), 2):
        try:
            start_str = times[i]
            end_str = times[i+1]

            start = parse_time(start_str)
            end = parse_time(end_str)

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

def suggest_exit_time():
    print("--- Sugestão de Horário de Saída ---")

    def parse_duration(t):
        parts = t.strip().split(':')
        if len(parts) == 2:
            return int(parts[0]) * 3600 + int(parts[1]) * 60
        elif len(parts) == 3:
            return int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])
        return None

    target_str = input("Meta de horas a cumprir (ex: 8:45) [padrão: 08:45]: ").strip()
    if not target_str:
        target_str = "08:45"
    target_seconds = parse_duration(target_str)
    if target_seconds is None:
        print("Formato inválido. Use hh:mm ou hh:mm:ss.")
        return

    text = input("Insira os pontos já batidos hoje (ex: 08:00 12:00 13:00):\n> ")
    times = re.findall(r'(\d{2}:\d{2}(?::\d{2})?)', text)

    if not times:
        print("Nenhum horário encontrado. Verifique o formato.")
        return

    times.sort()

    worked_seconds = 0
    last_open = None

    print("\nPeríodos já registrados:")
    for i in range(0, len(times), 2):
        try:
            start_str = times[i]
            end_str = times[i + 1]
            start = parse_time(start_str)
            end = parse_time(end_str)
            diff = (end - start).total_seconds()
            worked_seconds += diff
            print(f"  {start_str} -> {end_str} | Subtotal: {int(diff//3600):02d}h {int((diff%3600)//60):02d}m")
        except IndexError:
            last_open = times[i]
            print(f"  {times[i]} -> [em aberto]")

    remaining_seconds = target_seconds - worked_seconds

    print("-" * 40)
    print(f"Meta:             {target_str}")
    w_h, w_m, w_s = int(worked_seconds//3600), int((worked_seconds%3600)//60), int(worked_seconds%60)
    print(f"Já trabalhado:    {w_h:02d}:{w_m:02d}:{w_s:02d}")

    if remaining_seconds <= 0:
        over = abs(remaining_seconds)
        o_h, o_m, o_s = int(over//3600), int((over%3600)//60), int(over%60)
        print(f"Meta já atingida! Você trabalhou {o_h:02d}h {o_m:02d}m {o_s:02d}s a mais.")
    else:
        r_h, r_m, r_s = int(remaining_seconds//3600), int((remaining_seconds%3600)//60), int(remaining_seconds%60)
        print(f"Faltam:           {r_h:02d}h {r_m:02d}m {r_s:02d}s")

        if last_open:
            ref = parse_time(last_open)
        else:
            ref = datetime.now().replace(second=0, microsecond=0)
            print(f"(Nenhum ponto em aberto. Usando horário atual: {ref.strftime('%H:%M')})")

        exit_time = ref + timedelta(seconds=remaining_seconds)
        print(f"Bata o ponto às: {exit_time.strftime('%H:%M:%S')}")

    print("-" * 40)


def menu():
    while True:
        print("\n========================================")
        print("        SISTEMA DE CONTROLE DE PONTO    ")
        print("========================================")
        print("  1. Calcular horas trabalhadas")
        print("  2. Buscar horas trabalhadas automaticamente")
        print("  3. Sugerir horário de saída")
        print("  0. Sair")
        print("----------------------------------------")
        choice = input("Escolha uma opção: ").strip()

        if choice == "1":
            calculate_hours()
        elif choice == "2":
            getToday()
        elif choice == "3":
            suggest_exit_time()
        elif choice == "0":
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
