# Trabalho Prático 01 — Coding

**Curso:** Análise e Desenvolvimento de Sistemas
**Disciplina:** Coding
**Turma:** Bloco II (2026.2)

## 1. Classes identificadas
- Escola
- Sala de Aula
- Professor
- Aluno
- Endereço

## 2. Atributos e métodos

### Escola
Atributos: nome, endereço, cnpj
Métodos: adicionar_sala(), remover_sala()

### Sala de Aula
Atributos: numero, capacidade, andar
Métodos: reservar(), liberar()

### Professor
Atributos: nome, matricula, especialidade
Métodos: lecionar(), atualizar_dados()

### Aluno
Atributos: nome, matricula, curso
Métodos: matricular(), atualizar_dados()

### Endereço
Atributos: logradouro, numero, cidade
Métodos: atualizar(), exibir_endereco()

## 3. Relacionamentos
- Escola — Sala de Aula: **Composição**. A sala pertence ao ciclo de vida da escola. UML: losango preenchido no lado da Escola.
- Escola — Professor: **Associação**. Professor e escola podem existir independentemente. UML: linha simples.
- Aluno — Endereço: **Agregação**. O endereço pode existir independentemente do aluno. UML: losango vazado no lado do Aluno.

## 4. Diagrama de Classes UML
O arquivo diagrama-uml.mmd contém o diagrama em Mermaid.

## 5. Implementação em Python
A implementação está em main.py.

Execução:
python main.py
