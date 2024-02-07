# MarketTrendAnalyzer

MarketTrendAnalyzer é um sistema de análise de tendências de mercado desenvolvido para fornecer aos traders e investidores insights valiosos sobre condições de mercado através de indicadores técnicos e análise de padrões de candlestick. Utilizando dados históricos de ações, o sistema calcula o Índice de Força Relativa (RSI) e a Convergência/Divergência de Médias Móveis (MACD), além de identificar padrões de candlestick, para ajudar na identificação de potenciais sinais de compra e venda.

Funcionalidades:
Importação de dados históricos de ações de um arquivo CSV.
Cálculo do RSI para identificar condições de sobrecompra ou sobrevenda.
Cálculo do MACD para reconhecimento de mudanças de tendência.
Detecção de padrões de candlestick comuns.
Visualização gráfica dos indicadores e dos padrões de candlestick.
Pré-requisitos
Para executar o MarketTrendAnalyzer, você precisa ter o Python instalado em sua máquina, bem como as seguintes bibliotecas Python:

pandas
numpy
matplotlib
As dependências podem ser instaladas usando o seguinte comando:
pip install pandas numpy matplotlib
Instalação
Clone o repositório do MarketTrendAnalyzer para o seu sistema local ou faça o download do arquivo fonte.
Instale os pré-requisitos listados acima.
Uso
Para usar o MarketTrendAnalyzer, siga os passos abaixo:

Prepare um arquivo CSV contendo os dados históricos das ações que deseja analisar. O arquivo deve incluir colunas para Date e Close, pelo menos.
Modifique a variável caminho_arquivo no script para referenciar o local do seu arquivo CSV de dados.
Execute o script usando o comando:
python market_trend_analyzer.py
O sistema processará os dados, calculará os indicadores técnicos e os padrões de candlestick, e exibirá gráficos relevantes para análise.
