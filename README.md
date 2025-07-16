## 🌐 [English Version of README](README_EN.md)

# Numerical-Analysis

Repositório com **atividades práticas** da disciplina de *Cálculo Numérico* ministrada pelo Prof. Marcos Maia. Cada script demonstra, na prática, os métodos numéricos estudados em sala — de precisão de máquina a integração numérica e solução de PVIs.

## 🔨 Funcionalidades do Projeto
- **Atividade 01 – Precisão da Máquina:** calcula a menor perturbação que altera \(1 + \varepsilon\).
- **Atividade 02 – Zeros de Funções Reais:** compara Bissecção, Posição Falsa, Ponto Fixo, Newton e Secante.
- **Atividade 03 – Eliminação Gaussiana & Matriz de Hilbert:** resolve sistemas lineares \(H x=b\) e estima determinantes.
- **Atividade 04 – Interpolação Polinomial:** interpola calor específico da água e obtém raízes via Bissecção.
- **Atividade 05 – Ajuste de Curva (MMQ):** ajusta preço do ativo WIN (B3) por mínimos quadrados.
- **Atividade 06 – Integração Numérica:** integra \(e^{-x^{2}}\) em \([0,1]\) com a Regra dos Trapézios.
- **Atividade 07 – PVI Numérico (Modelo SIR):** simula epidemia usando Runge–Kutta de 4ª ordem.

## ✔️ Técnicas e Tecnologias Utilizadas
- **Python 3.11**
- **Bibliotecas:** NumPy, Matplotlib
- **Ferramentas:** Google Colab, Jupyter Notebook
- **Boas práticas:** ambientes virtuais, `requirements.txt`, comentários de código e notebooks explicativos.

## 📁 Estrutura do Projeto
```
├── Atividade 01 - Precisão da Máquina.py
├── Atividade 02 - Comparativo dos Métodos de Zeros de Funções Reais.py
├── atividade_03_eliminação_gaussiana_e_a_matriz_de_hilbert.py
├── atividade_04_interpolação_polinomial.py
├── atividade_05_ajuste_de_curva_de_mmq.py
├── atividade_06_integração_numérica.py
├── atividade_07_pvi_numérico.py
├── requirements.txt
├── README.md
└── README_EN.md
```

## 🛠️ Abrir e rodar o projeto
Para executar localmente:

1. **Clone o repositório**  
   ```
   git clone https://github.com//Numerical-Analysis.git
   cd Numerical-Analysis
   ```

2. **Crie um ambiente virtual (opcional, recomendado)**  
   ```
   python -m venv .venv
   source .venv/bin/activate            # Linux/macOS
   .venv\Scripts\activate               # Windows
   ```

3. **Instale as dependências**  
   ```
   pip install -r requirements.txt
   ```

4. **Execute a atividade desejada**  
   ```
   python "Atividade 06 - Integração Numérica.py"
   ```

> Cada script possui *prints* e/ou *plots* que ilustram o método numérico em ação.

## 🌐 Deploy
Por serem notebooks/scripts acadêmicos, a forma mais prática de “deploy” é via **Google Colab**:

1. Faça *upload* dos arquivos `.py` ou `.ipynb` no Colab.  
2. Instale as dependências na primeira célula:  
   ```
   !pip install numpy matplotlib
   ```  
3. Execute as células e compartilhe o link gerado.

Para publicação web estática (ex.: GitHub Pages) basta converter notebooks em HTML (`jupyter nbconvert --to html`) e subir na branch `gh-pages`.
```
