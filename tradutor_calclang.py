#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tradutor CalcLang → Python
Simula o funcionamento básico de um compilador
"""

class CalcLangTranslator:    
    OPERATIONS = {
        'ADD': '+',
        'SUB': '-',
        'MUL': '*',
        'DIV': '/'
    }
    
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.errors = []
        
    def validate_line(self, line, line_number):
        line = line.strip()
        
        if not line:
            return None, None, None, None
        
        tokens = line.split()
        
        if len(tokens) != 3:
            self.errors.append(f"Erro na linha {line_number}")
            return False, None, None, None
        
        operation, num1_str, num2_str = tokens
        
        if operation not in self.OPERATIONS:
            self.errors.append(f"Erro na linha {line_number}")
            return False, None, None, None
        
        try:
            float(num1_str)
            float(num2_str)
        except ValueError:
            self.errors.append(f"Erro na linha {line_number}")
            return False, None, None, None
        
        return True, operation, num1_str, num2_str
    
    def translate(self):
        try:
            with open(self.input_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except FileNotFoundError:
            print(f"Erro: arquivo '{self.input_file}' não encontrado")
            return False
        
        python_code = []
        
        # Análise Léxica, Sintática e Semântica
        for line_number, line in enumerate(lines, start=1):
            valid, operation, num1, num2 = self.validate_line(line, line_number)
            
            if valid is None:
                continue
            
            # Geração de Código
            if valid:
                python_operator = self.OPERATIONS[operation]
                python_line = f"print({num1} {python_operator} {num2})"
                python_code.append(python_line)
        
        if self.errors:
            for error in self.errors:
                print(error)
            return False
        
        try:
            with open(self.output_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(python_code))
            print(f"✓ Tradução concluída com sucesso!")
            print(f"✓ Arquivo gerado: {self.output_file}")
            return True
        except Exception as e:
            print(f"Erro ao gravar arquivo de saída: {e}")
            return False


def main():
    print("=" * 60)
    print("TRADUTOR CALCLANG → PYTHON")
    print("=" * 60)
    
    input_file = "programa.calc"
    output_file = "programa.py"
    
    print(f"\nArquivo de entrada: {input_file}")
    print(f"Arquivo de saída: {output_file}\n")
    
    translator = CalcLangTranslator(input_file, output_file)
    success = translator.translate()
    
    if success:
        print("\n✓ Para executar o programa traduzido, use:")
        print(f"  python {output_file}")


if __name__ == "__main__":
    main()