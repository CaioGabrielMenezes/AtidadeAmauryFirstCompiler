# Tradutor CalcLang → Python

## 📋 Descrição

Tradutor simples que converte código da linguagem fictícia **CalcLang** para **Python**, 
simulando o funcionamento básico de um compilador.

## 🎯 Funcionalidades

- ✅ Análise léxica (tokenização)
- ✅ Análise sintática (validação de estrutura)
- ✅ Análise semântica (validação de tipos)
- ✅ Geração de código Python
- ✅ Detecção e relatório de erros

## 📖 Linguagem CalcLang

### Sintaxe

```
OPERACAO numero numero
```

### Operações Suportadas

| Operação | Descrição | Exemplo |
|----------|-----------|---------|
| `ADD` | Adição | `ADD 10 20` |
| `SUB` | Subtração | `SUB 30 5` |
| `MUL` | Multiplicação | `MUL 2 3` |
| `DIV` | Divisão | `DIV 8 2` |

### Regras

1. Cada linha contém exatamente uma instrução
2. Formato obrigatório: `OPERACAO numero numero`
3. Operandos podem ser inteiros ou decimais
4. Linhas vazias são ignoradas

## 🚀 Como Usar

### 1. Criar arquivo CalcLang

Crie um arquivo com extensão `.calc`:

```
ADD 10 20
SUB 30 5
MUL 2 3
DIV 8 2
```

### 2. Executar o tradutor

```bash
python tradutor_calclang.py
```

### 3. Executar o código gerado

```bash
python programa.py
```

Saída:
```
30
25
6
4.0
```

## 📁 Arquivos do Projeto

```
tradutor-calclang/
├── tradutor_calclang.py       # Código do tradutor
├── programa.calc              # Exemplo de entrada válida
├── programa_com_erros.calc    # Exemplo com erros
├── teste_erros.py             # Script de teste
├── RESPOSTAS_CONCEITUAIS.md   # Respostas teóricas
└── README.md                  # Este arquivo
```

## 🧪 Exemplos

### Exemplo 1: Código Válido

**Entrada (programa.calc):**
```
ADD 10 20
SUB 30 5
MUL 2 3
DIV 8 2
```

**Saída (programa.py):**
```python
print(10 + 20)
print(30 - 5)
print(2 * 3)
print(8 / 2)
```

**Execução:**
```
30
25
6
4.0
```

### Exemplo 2: Detecção de Erros

**Entrada (programa_com_erros.calc):**
```
ADD 10 20
SUB 30          ← Faltam argumentos
MUL 2 3 5       ← Muitos argumentos
POTENCIA 2 3    ← Operação inválida
DIV 8 abc       ← Argumento não numérico
```

**Saída:**
```
Erro na linha 2
Erro na linha 3
Erro na linha 4
Erro na linha 5
```

## 🔧 Personalização

Para usar arquivos diferentes, modifique a função `main()`:

```python
def main():
    input_file = "meu_programa.calc"
    output_file = "meu_programa.py"
    
    translator = CalcLangTranslator(input_file, output_file)
    translator.translate()
```

## 🧠 Como Funciona

### Fluxo de Tradução

```
┌─────────────────┐
│  Arquivo .calc  │
└────────┬────────┘
         │
         ↓
┌─────────────────────┐
│  Análise Léxica     │ ← Quebra em tokens
│  (tokenização)      │
└────────┬────────────┘
         │
         ↓
┌─────────────────────┐
│  Análise Sintática  │ ← Valida estrutura
│  (parsing)          │
└────────┬────────────┘
         │
         ↓
┌─────────────────────┐
│  Análise Semântica  │ ← Valida tipos
│  (type checking)    │
└────────┬────────────┘
         │
         ↓
┌─────────────────────┐
│  Geração de Código  │ ← Produz Python
└────────┬────────────┘
         │
         ↓
┌─────────────────┐
│  Arquivo .py    │
└─────────────────┘
```

### Etapas Detalhadas

1. **Leitura**: Carrega arquivo `.calc`
2. **Tokenização**: Divide cada linha em tokens
3. **Validação**: 
   - Verifica número de elementos (deve ser 3)
   - Valida operação (ADD, SUB, MUL, DIV)
   - Verifica se operandos são números
4. **Geração**: Cria código Python equivalente
5. **Escrita**: Salva arquivo `.py`

## 📚 Respostas Teóricas

Consulte o arquivo `RESPOSTAS_CONCEITUAIS.md` para:

- a) Como este tradutor simula um compilador
- b) Diferença entre tradutor e interpretador
- c) Etapas para um compilador completo

## ⚠️ Limitações

- Não suporta variáveis
- Não suporta expressões complexas
- Não suporta estruturas de controle (if, while)
- Não suporta funções
- Sem otimização de código

## 🎓 Conceitos Aprendidos

- ✓ Análise léxica
- ✓ Análise sintática
- ✓ Análise semântica
- ✓ Geração de código
- ✓ Tratamento de erros
- ✓ Diferença entre tradutor e interpretador

## 📝 Testes

Execute os testes incluídos:

```bash
# Teste com código válido
python tradutor_calclang.py

# Teste com detecção de erros
python teste_erros.py
```

## 🤝 Contribuindo

Este é um projeto educacional. Sugestões de melhorias:

1. Adicionar suporte a variáveis
2. Implementar estruturas de controle
3. Criar um interpretador direto
4. Adicionar mais operações matemáticas
5. Implementar uma AST (Abstract Syntax Tree)

## 📄 Licença

Projeto educacional - livre para uso acadêmico.

---

**Desenvolvido para fins educacionais**  
Demonstra conceitos fundamentais de compiladores
