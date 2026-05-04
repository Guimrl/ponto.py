# 🕐 Calculadora de Horas Trabalhadas

Script simples em Python para calcular o total de horas trabalhadas a partir dos registros de ponto.

## Como usar

1. Execute o script:

   ```bash
   python ponto.py
   ```

2. Cole os registros de ponto quando solicitado:

   ```
   Insira os dados do ponto aqui:
   ex: hh:mm:ss hh:mm:ss
   > 08:00:00 12:00:00 13:00:00 17:30:00
   ```

3. O script exibirá o resumo do dia e o total trabalhado:
   ```
   Resumo do dia:
     08:00:00 -> 12:00:00 | Subtotal: 04h 00m
     13:00:00 -> 17:30:00 | Subtotal: 04h 30m
   ------------------------------
   TOTAL TRABALHADO: 08:30:00
   ------------------------------
   ```

## Requisitos

- Python 3.x

## Observações

- Os horários devem estar no formato `hh:mm:ss`
- Insira os horários em pares (entrada e saída)
- Caso haja um horário sem par, será exibido `[Falta saída]`
- Os horários devem estar no formato `hh:mm:ss`
- Insira os horários em pares (entrada e saída)
- Caso haja um horário sem par, será exibido `[Falta saída]`
- Caso haja um horário sem par, será exibido `[Falta saída]`
