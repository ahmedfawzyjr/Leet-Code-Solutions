
from typing import List
import collections

class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        eval_map = dict(zip(evalvars, evalints))
        
        # Tokenize the expression
        tokens = []
        i = 0
        n = len(expression)
        while i < n:
            if expression[i] == ' ':
                i += 1
            elif expression[i] in '+-()':
                tokens.append(expression[i])
                i += 1
            else:
                j = i
                while j < n and expression[j] not in ' +-()':
                    j += 1
                tokens.append(expression[i:j])
                i = j
        
        # Define term: dict where key is sorted tuple of variables, value is coefficient
        def parse_term(term_str):
            if term_str in eval_map:
                return {tuple(): eval_map[term_str]}
            elif term_str.isdigit():
                return {tuple(): int(term_str)}
            else:
                return {tuple(sorted(term_str.split('*'))): 1}
        
        # Combine two terms dictionaries
        def combine(a, b, op):
            res = collections.defaultdict(int)
            for k, v in a.items():
                res[k] += v
            for k, v in b.items():
                if op == '+':
                    res[k] += v
                else:
                    res[k] -= v
            # Remove zero coefficients
            return {k: v for k, v in res.items() if v != 0}
        
        # Multiply two terms dictionaries
        def multiply(a, b):
            res = collections.defaultdict(int)
            for k1, v1 in a.items():
                for k2, v2 in b.items():
                    new_k = tuple(sorted(k1 + k2))
                    res[new_k] += v1 * v2
            return {k: v for k, v in res.items() if v != 0}
        
        # Stack to hold terms, ops to hold operators
        terms_stack = []
        ops_stack = []
        
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token == '(':
                ops_stack.append(token)
            elif token == ')':
                while ops_stack and ops_stack[-1] != '(':
                    op = ops_stack.pop()
                    b = terms_stack.pop()
                    a = terms_stack.pop()
                    if op == '*':
                        terms_stack.append(multiply(a, b))
                    else:
                        terms_stack.append(combine(a, b, op))
                ops_stack.pop()
            elif token in '+-':
                while ops_stack and ops_stack[-1] in '+-*':
                    op = ops_stack.pop()
                    b = terms_stack.pop()
                    a = terms_stack.pop()
                    if op == '*':
                        terms_stack.append(multiply(a, b))
                    else:
                        terms_stack.append(combine(a, b, op))
                ops_stack.append(token)
            elif token == '*':
                ops_stack.append(token)
            else:
                terms_stack.append(parse_term(token))
            i += 1
        
        while ops_stack:
            op = ops_stack.pop()
            b = terms_stack.pop()
            a = terms_stack.pop()
            if op == '*':
                terms_stack.append(multiply(a, b))
            else:
                terms_stack.append(combine(a, b, op))
        
        # Now format the result
        res_dict = terms_stack[0]
        
        # Sort the terms: first by degree (length of key), then lex order
        sorted_keys = sorted(res_dict.keys(), key=lambda x: (-len(x), x))
        
        result = []
        for key in sorted_keys:
            coeff = res_dict[key]
            if coeff == 0:
                continue
            term_parts = []
            if coeff != 1 or not key:
                term_parts.append(str(coeff))
            for var in key:
                term_parts.append(var)
            result.append('*'.join(term_parts))
        return result
