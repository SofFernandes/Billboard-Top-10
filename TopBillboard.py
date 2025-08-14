from streamlit_elements import elements, mui, html
import billboard
import streamlit as st
import datetime
import requests


#INTERFACE DO USUÁRIO

def main():
    st.title(":rainbow[Top 10 músicas da Billboard]")
    body = ("Selecione o mês e ano desejados")
    st.header(body)
    
    # =========================================
    # SELEÇÃO DE MÊS/ANO
    # =========================================
    # Podemos usar dois selects (mês e ano) ou um date_input.
    # Exemplo: Selectbox para mês e ano
    meses = {
        "Janeiro": 1, "Fevereiro": 2, "Março": 3, "Abril": 4, "Maio": 5, "Junho": 6,
        "Julho": 7, "Agosto": 8, "Setembro": 9, "Outubro": 10, "Novembro": 11, "Dezembro": 12
    }
    mes_nome = st.selectbox("Selecione o mês", list(meses.keys()))
    ano = st.number_input("Selecione o ano", min_value=1958, max_value=datetime.datetime.now().year, value=2023)
 
    # Constrói data (ex: 2023-01-01)
    mes_num = meses[mes_nome]
    # Usaremos o dia 01 para simplificar
    date_str = f"{ano}-{mes_num:02d}-01"
    date_show = f"{mes_num}-{ano}"
 
    if st.button("Buscar Top 10"):
        with st.spinner("Carregando dados da Billboard..."):
            chart_data = billboard.get_music(date_str)
 
        if chart_data:
            st.success(f"Resultados para {mes_num} de {ano} (Billboard Hot 100)")
 
            # Exibe resultados em formato de tabela ou lista
            table_data = []
            for e in chart_data:
                table_data.append(billboard.spotify_music(e['title']))
 
            # Podemos exibir em formato de DataFrame
            # Se preferir, podemos formatar melhor o link, mas aqui vai um exemplo simples
            st.table(table_data)
        else:
            st.error("Não foi possível obter dados para a data selecionada.")
 
if __name__ == "__main__":
    main()