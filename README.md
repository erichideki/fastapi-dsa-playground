# 🚀 FastAPI DSA Playground

Projeto criado para estudar **Estruturas de Dados e Algoritmos (DSA)** inspirados em problemas do **LeetCode**, implementando soluções em **Python** e expondo exemplos através de uma **API construída com FastAPI**.

A ideia é evoluir gradualmente pelas principais estruturas de dados utilizadas em **entrevistas técnicas e sistemas reais**, registrando cada implementação dentro do projeto.

---

# 🎯 Objetivo

Este repositório tem como objetivo:

- Praticar **Estruturas de Dados e Algoritmos**
- Resolver problemas inspirados no **LeetCode**
- Implementar soluções em **Python**
- Expor as soluções através de **endpoints FastAPI**
- Criar um **playground de estudo contínuo**
- Evoluir progressivamente pelas principais estruturas utilizadas em entrevistas técnicas

Cada problema implementado conterá:

- 📄 Descrição do problema
- 📏 Regras e restrições
- 🧠 Implementação da solução
- 🌐 Endpoint para execução via API

---

# 🧰 Stack do Projeto

- Python 3.12+
- FastAPI
- Uvicorn
- UV (gerenciador de dependências)
- Pytest *(futuramente para testes)*

---

# 📁 Estrutura do Projeto

dsa-fastapi/
│
├── app/
│ ├── main.py
│ │
│ ├── arrays/
│ │ ├── router.py
│ │ └── problems.py
│ │
│ ├── linked_lists/
│ │ ├── router.py
│ │ └── problems.py
│ │
│ ├── stacks/
│ │ ├── router.py
│ │ └── problems.py
│ │
│ ├── queues/
│ │ ├── router.py
│ │ └── problems.py
│ │
│ ├── trees/
│ │ ├── router.py
│ │ └── problems.py
│ │
│ ├── graphs/
│ │ ├── router.py
│ │ └── problems.py
│ │
│ └── dynamic_programming/
│ ├── router.py
│ └── problems.py
│
└── tests/


Cada pasta representa **uma estrutura de dados ou categoria de algoritmo**.

---

# 📚 Roadmap de Estruturas de Dados

A progressão seguirá aproximadamente esta ordem.

---

## 1️⃣ Arrays

- [ ] Two Sum  
- [ ] Best Time to Buy and Sell Stock  
- [ ] Contains Duplicate  
- [ ] Product of Array Except Self  

---

## 2️⃣ Hash Tables

- [ ] Two Sum (HashMap)  
- [ ] Group Anagrams  
- [ ] Top K Frequent Elements  

---

## 3️⃣ Stack

- [ ] Valid Parentheses  
- [ ] Min Stack  
- [ ] Daily Temperatures  

---

## 4️⃣ Queue / Deque

- [ ] Implement Queue using Stacks  
- [ ] Sliding Window Maximum  

---

## 5️⃣ Linked List

- [ ] Reverse Linked List  
- [ ] Merge Two Sorted Lists  
- [ ] Linked List Cycle  

---

## 6️⃣ Trees

- [ ] Maximum Depth of Binary Tree  
- [ ] Invert Binary Tree  
- [ ] Binary Tree Level Order Traversal  

---

## 7️⃣ Heap / Priority Queue

- [ ] Kth Largest Element in an Array  
- [ ] Merge K Sorted Lists  

---

## 8️⃣ Graphs

- [ ] Number of Islands  
- [ ] Clone Graph  
- [ ] Course Schedule  

---

## 9️⃣ Backtracking

- [ ] Subsets  
- [ ] Permutations  
- [ ] Combination Sum  

---

## 🔟 Dynamic Programming

- [ ] Climbing Stairs  
- [ ] Coin Change  
- [ ] Longest Increasing Subsequence  

---

# 🧩 Estrutura de um Problema

Cada problema segue um formato semelhante ao **LeetCode**, documentado diretamente no código:

```python
"""
Problem: Two Sum

Given an array of integers nums and an integer target,
return the indices of the two numbers such that they add up to target.

Rules:
- Each input has exactly one solution
- You may not use the same element twice
- You can return the answer in any order

Example:

Input:
nums = [2,7,11,15]
target = 9

Output:
[0,1]
"""
```
▶️ Como Executar o Projeto
1️⃣ Instalar dependências
uv sync
2️⃣ Rodar a aplicação
uv run uvicorn app.main:app --reload
3️⃣ Acessar documentação da API
http://localhost:8000/docs

A interface Swagger permitirá testar todos os problemas implementados.

🧪 Exemplo de Endpoint
Request
POST /arrays/two-sum
{
  "nums": [2,7,11,15],
  "target": 9
}
Response
{
  "problem": "Two Sum",
  "input": {
    "nums": [2,7,11,15],
    "target": 9
  },
  "result": [0,1]
}