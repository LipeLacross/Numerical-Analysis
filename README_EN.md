## 🌐 [Versão em Português (README)](README.md)

# Numerical-Analysis

Repository with **hands-on assignments** from the *Numerical Analysis* course taught by Prof. Marcos Maia. Each script demonstrates, in practice, one of the numerical methods covered in class—from machine precision to numerical integration and IVP solutions.

## 🔨 Project Features
- **Activity 01 – Machine Precision:** computes the smallest perturbation that changes \(1 + \varepsilon\).
- **Activity 02 – Zeros of Real Functions:** compares Bisection, False Position, Fixed Point, Newton and Secant methods.
- **Activity 03 – Gaussian Elimination & Hilbert Matrix:** solves linear systems \(H x = b\) and estimates determinants.
- **Activity 04 – Polynomial Interpolation:** interpolates the specific heat of water and finds roots via Bisection.
- **Activity 05 – Curve Fitting (Least Squares):** fits the WIN (B3) asset price with a quadratic model.
- **Activity 06 – Numerical Integration:** integrates \(e^{-x^{2}}\) on \([0,1]\) with the Trapezoidal Rule.
- **Activity 07 – Numerical IVP (SIR Model):** simulates an epidemic using 4th-order Runge–Kutta.

### 📸 Visual Example
	

  
  


## ✔️ Tools & Technologies
- **Python 3.11**
- **Libraries:** NumPy, Matplotlib
- **Environments:** Google Colab, Jupyter Notebook
- **Best practices:** virtual environments, `requirements.txt`, in-code comments, explanatory notebooks.

## 📁 Project Structure
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

## 🛠️ Running the Project Locally
1. **Clone the repository**  
   ```
   git clone https://github.com//Numerical-Analysis.git
   cd Numerical-Analysis
   ```

2. **(Optional) Create a virtual environment**  
   ```
   python -m venv .venv
   source .venv/bin/activate            # Linux/macOS
   .venv\Scripts\activate               # Windows
   ```

3. **Install the dependencies**  
   ```
   pip install -r requirements.txt
   ```

4. **Run the desired activity**  
   ```
   python "Atividade 06 - Integração Numérica.py"
   ```

> Each script prints results and/or displays plots that illustrate the numerical method in action.

## 🌐 Deployment
Because these are academic notebooks/scripts, the most convenient “deployment” is **Google Colab**:

1. Upload the `.py` or `.ipynb` files to Colab.  
2. Install dependencies in the first cell:  
   ```
   !pip install numpy matplotlib
   ```  
3. Run the cells and share the generated link.

For a static web showcase (e.g., GitHub Pages) you can convert notebooks to HTML (`jupyter nbconvert --to html`) and push them to the `gh-pages` branch.
```