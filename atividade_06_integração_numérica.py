# -*- coding: utf-8 -*-
"""Atividade 06 - Integração Numérica

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jHm8_UtF-9NZ_IRGEzM6OTMF_STwUxt2

# Cálculo da Integral $$\int_{0}^{1} e^{-x^2} \, dx$$ com Regra dos Trapézios

---

## 📈 **Passo 1: Determinação do Número de Subintervalos ($$n$$)**

### **Fórmula do Erro Máximo**
$$
E \leq \frac{(b-a)^3}{12n^2} \cdot \max_{x \in [a,b]} |f''(x)|
$$

### **Procedimento Detalhado**
1. **Segunda derivada de $$f(x) = e^{-x^2}$$**:
   $$
   f''(x) = (4x^2 - 2)e^{-x^2}
   $$

2. **Máximo de $$|f''(x)|$$ em $$$$**:
   - Em $$x = 0$$: $$|f''(0)| = 2$$
   - Em $$x = 1$$: $$|f''(1)| \approx 0.735$$
   - **Máximo absoluto**: $$\max |f''(x)| = 2$$.

3. **Cálculo de $$n$$ mínimo**:
   $$
   \frac{1}{6n^2} \leq \frac{1}{6} \times 10^{-4} \implies n^2 \geq 10^4 \implies n \geq 100
   $$
   **Resultado**: $$n_{\text{mín}} = 100$$.

---

## 💻 **Passo 2: Implementação em Python**


### **Explicação do Código**
| **Componente**         | **Matematicamente**                     | **No Código**               |
|-------------------------|-----------------------------------------|------------------------------|
| **Subintervalos**       | $$n = 100$$                             | `n = 100`                    |
| **Passo (h)**           | $$h = \frac{1}{100} = 0.01$$           | `h = (b - a)/n`              |
| **Pontos amostrados**   | $$x_i = 0 + ih$$                       | `x = np.linspace(a, b, n+1)` |
| **Soma ponderada**      | $$2\sum_{i=1}^{99} f(x_i)$$            | Loop `for i in range(1, n)`  |
| **Fator de ajuste**     | $$\frac{h}{2}$$                        | `integral *= h / 2`          |

---

## ✅ **Resultado e Verificação**
- **Saída do código**:
  ```
  Valor da integral: 0.7468180015
  ```
- **Erro máximo teórico**:
  $$
  E \leq \frac{1}{12 \cdot 100^2} \cdot 2 = 1.6667 \times 10^{-5} < \frac{1}{6} \times 10^{-4}
  $$
- **Erro absoluto** (vs. valor de referência ≈ 0.746824):
  $$
  |0.7468180015 - 0.746824| \approx 5.999 \times 10^{-6}
  $$
  **Precisão garantida!** ✅
"""

import numpy as np

# Parâmetros
n = 100       # Subintervalos calculados
a = 0         # Limite inferior
b = 1         # Limite superior
h = (b - a)/n # Largura dos trapézios

# Amostragem dos pontos
x = np.linspace(a, b, n+1)

# Função integranda
def f(r):
    return np.exp(-r**2)

# Cálculo da soma ponderada
integral = f(x[0]) + f(x[-1])  # Extremos f(a) + f(b)

for i in range(1, n):          # Termos internos (peso 2)
    integral += 2 * f(x[i])

integral *= h/2                # Fator de ajuste

print(f"Valor da integral: {integral:.10f}")

# code prof
import numpy as np

#dados
#quantidade de subintervalos
n=100

#limites de integração
a=0
b=1

#altura de cada trapézio
h=(b-a)/n

#amostra no eixo x:
x=np.linspace(a,b,n+1)

#amostra no eixo y:
y=np.exp(-x**2)

#defina a função a ser integrada
def f(r):
    return np.exp(-r**2)

integral = 0
for i in range(1,n):
  integral = integral + 2*f(x[i])
integral = integral + f(x[0]) + f(x[n])
integral = integral*h/2
print(integral)