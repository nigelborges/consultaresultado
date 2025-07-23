import pandas as pd

EXCEL_FILE = 'candidatos.xlsx'

def validar_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11

def consultar_candidato_por_cpf(cpf, df):
    resultado = df[df['cpf'] == cpf]
    if resultado.empty:
        print("CPF não encontrado na base de dados.")
    else:
        for coluna, valor in resultado.iloc[0].items():
            print(f"{coluna}: {valor}")

def main():
    cpf = input("Digite o CPF (somente números, 11 dígitos): ").strip()
    
    if not validar_cpf(cpf):
        print("CPF inválido. Digite exatamente 11 números.")
        return

    try:
        df = pd.read_excel(EXCEL_FILE, dtype={'cpf': str})
        consultar_candidato_por_cpf(cpf, df)
    except FileNotFoundError:
        print(f"Arquivo '{EXCEL_FILE}' não encontrado.")
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")

if __name__ == "__main__":
    main()
