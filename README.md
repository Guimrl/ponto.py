# Calculadora de Horas Trabalhadas

Script simples em Python para calcular o total de horas trabalhadas a partir dos registros de ponto do dia.
O projeto resolve um problema simples, a minha preguiça de calcular quantas horas eu trabalhei no dia.

## Como usar

<!-- criar o .env semelhante ao .env.example -->
<!-- pip install -r requirements.txt -->
1. Instale as dependencias do projeto:

   ```bash
   pip install -r requirements.txt
   ```

2. Execute o script:

   ```bash
   python ponto.py
   ```

3. Cole os registros de ponto quando solicitado:

   ```
   Insira os dados do ponto aqui:
   ex: hh:mm:ss hh:mm:ss
   > 08:00:00 12:00:00 13:00:00 17:30:00
   ```

## Requisitos

- Python 3.x

## Observações

- Os horários devem estar no formato `hh:mm:ss`
- Insira os horários em pares (entrada e saída)
- Caso haja um horário sem par, será exibido `[Falta saída]`
