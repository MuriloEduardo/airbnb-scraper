# Verificador de Disponibilidade Airbnb 🏡

Um script Python modular que utiliza Selenium para verificar a disponibilidade e preços de listagens do Airbnb.

## 📋 Funcionalidades

- ✅ Verifica se uma acomodação está disponível para datas específicas
- 💰 Extrai o preço total da estadia
- 🏷️ Obtém o título da listagem
- 📅 Detecta mensagens de indisponibilidade e estadia mínima

## 🔧 Requisitos

- Python 3.6 ou superior
- Google Chrome instalado
- Bibliotecas Python listadas em `requirements.txt`

## ⚙️ Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/MuriloEduardo/airbnb-scraper.git
   cd verificador-disponibilidade-airbnb
   ```

2. Crie e ative um ambiente virtual (recomendado):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # No Linux/Mac
   # ou
   .venv\Scripts\activate  # No Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Como usar

Execute o script fornecendo o ID da listagem do Airbnb e as datas desejadas:

```bash
python main.py --id ID_DA_LISTAGEM --check_in DATA_CHECKIN --check_out DATA_CHECKOUT --adults NUMERO_ADULTOS
```

### Parâmetros:

- `--id`: ID da listagem do Airbnb (encontrado na URL da listagem)
- `--check_in`: Data de check-in no formato YYYY-MM-DD (ex: 2025-06-01)
- `--check_out`: Data de check-out no formato YYYY-MM-DD (ex: 2025-06-07)
- `--adults`: Número de adultos (padrão: 1)

### Exemplo:

```bash
python main.py --id 769729843373520689 --check_in 2025-06-01 --check_out 2025-06-07 --adults 1
```

### Saída de exemplo:

```
🔗 URL: https://www.airbnb.com.br/rooms/769729843373520689?check_in=2025-06-01&check_out=2025-06-07&adults=1
🏡 Título do anúncio: A cabana dos seus sonhos existe! Canela/Gramado
💰 Valor total: R$3.366 por 6 noites
✅ Imóvel disponível nas datas selecionadas.
```

Quando uma listagem não está disponível, você verá informações adicionais:

```
🏡 Título do anúncio: A cabana dos seus sonhos existe! Canela/Gramado
⚠️ Preço não encontrado.
❌ Imóvel indisponível nas datas selecionadas.
📝 Motivo: Essas datas não estão disponíveis
```

## 🧩 Estrutura do Projeto

O projeto segue uma estrutura modular:

- `main.py`: Script principal que coordena a execução
- `driver_manager.py`: Gerencia o WebDriver do Selenium
- `titulo_extractor.py`: Extrai o título da listagem
- `preco_extractor.py`: Extrai informações de preço
- `disponibilidade_extractor.py`: Verifica a disponibilidade da listagem

## 📝 Como obter o ID de uma listagem

O ID da listagem é o número que aparece na URL do Airbnb. Por exemplo, na URL:
`https://www.airbnb.com.br/rooms/769729843373520689?adults=1`

O ID é `769729843373520689`.

## ⚠️ Observações

- Este script é apenas para fins educacionais e pessoais
- O uso de web scrapers pode violar os Termos de Serviço do Airbnb
- O layout do site Airbnb pode mudar, exigindo atualizações no script
