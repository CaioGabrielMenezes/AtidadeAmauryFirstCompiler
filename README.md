# RESPOSTAS CONCEITUAIS

### Alunos: Caio Gabriel Pereira Menezes e Caio Renato dos Santos Claudino

## a) Em que sentido essa atividade simula o funcionamento de um compilador?

O tradutor implementa as 4 etapas básicas de um compilador:

1. **Análise Léxica:** Divide a linha em tokens (operação, num1, num2)
2. **Análise Sintática:** Valida se tem 3 elementos
3. **Análise Semântica:** Verifica se a operação existe e se os números são válidos
4. **Geração de Código:** Converte para Python

Faltam: otimização, tabela de símbolos e código intermediário.

---

## b) Qual a diferença entre esse tradutor e um interpretador?

**Tradutor:**
- Gera arquivo Python (.py)
- NÃO executa o código
- Requer 2 passos: traduzir → executar

**Interpretador:**
- NÃO gera arquivo intermediário
- Executa o código diretamente
- Apenas 1 passo

---

## c) Que etapas adicionais seriam necessárias para transformar essa solução em um compilador mais completo?

1. **Tabela de símbolos** (para variáveis)
2. **Estruturas de controle** (IF, WHILE, FOR)
3. **Funções** (definir e chamar)
4. **Otimização de código**
5. **AST** (Árvore Sintática Abstrata)
6. **Mensagens de erro descritivas**
7. **Código intermediário**
8. **Múltiplos backends** (gerar C, JavaScript, etc)
