# ==========================================================
# PROJETO: Matemática na Programação - Crescimento Exponencial
# Feira de Ciências do Ensino Médio
# ==========================================================

import time

def executar_simulacao():
    print("=" * 60)
    print(" 📊 MODELO COMPUTACIONAL DE CRESCIMENTO EXPONENCIAL 📊")
    print("=" * 60)
    
    # ENTRADA DE DADOS: Permite interação direta com o público na feira
    try:
        p0 = float(input("➔ Digite o Valor Inicial (P0) [ex: 100]: "))
        taxa_pct = float(input("➔ Digite a Taxa de Crescimento Diário (%) [ex: 20]: "))
        dias = int(input("➔ Digite o Período Total de Dias (t) [ex: 10]: "))
    except ValueError:
        print("\n❌ Erro: Por favor, insira apenas números válidos.")
        return

    # CONVERSÃO MATEMÁTICA: Porcentagem para número decimal (r)
    r = taxa_pct / 100

    print("\n" + "-" * 60)
    print(f"• Parâmetros Definidos: P0 = {p0} | r = {r} ({taxa_pct}%) | t = {dias} dias")
    print("• Aplicando a Equação: P(t) = P0 * (1 + r)^t")
    print("-" * 60)
    
    time.sleep(1)
    print("\nProcessando iterações...\n")

    # ESTRUTURA DE REPETIÇÃO: Computa e exibe a curva de crescimento dia a dia
    for t in range(1, dias + 1):
        # Aplicação direta da fórmula teórica
        p_t = p0 * ((1 + r) ** t)
        
        # Exibição dos resultados parciais
        print(f" 📅 Dia {t:2d} ➔ População Projetada: {round(p_t):,d} unidades")
        time.sleep(0.4) # Intervalo visual para acompanhamento da plateia

    print("\n" + "=" * 60)
    print(" ✅ PROCESSAMENTO CONCLUÍDO COM SUCESSO")
    print("=" * 60 + "\n")

# LOOP DE EXECUÇÃO: Permite realizar múltiplos testes sequenciais
while True:
    executar_simulacao()
    novo_teste = input("Deseja realizar uma nova simulação? (s/n): ").strip().lower()
    if novo_teste != 's':
        print("\nEncerrando o programa... Obrigado pela visita ao estande!")
        break
    print("\n" * 2)
# Executando a função com 100 itens iniciais, 25% de taxa e simulando por 7 dias
simular_crescimento(populacao_inicial=100, taxa_crescimento=0.25, dias_totais=7)
