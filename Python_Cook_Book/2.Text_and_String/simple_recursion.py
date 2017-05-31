#!/usr/bin/env python
# coding=utf-8

'''
实现一个简单的递归下降分析器
据一组语法规则解析文本并执行命令，或者构造一个代表输入的抽象语法
树。如果语法非常简单，你可以自己写这个解析器，而不是使用一些框架。
你首先要以 BNF 或者 EBNF 形式指定一个标准语法。

'''

import re
import collections


# Token specification
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
MINUS = r'(?P<MINUS>-)'
TIMES = r'(?P<TIMES>\*)'
DIVIDE = r'(?P<DIVIDE>/)'
LPAREN = r'(?P<LPAREN>\()'
RPAREN = r'(?P<RPAREN>\))'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NUM, PLUS, MINUS, TIMES,DIVIDE, LPAREN, RPAREN, WS]))

Token = collections.namedtuple('Token', ['type', 'value'])

def generate_tokens(text):
    scanner = master_pat.scanner(text)
    for m in iter(scanner.match, None):
        tok = Token(m.lastgroup, m.group())
        if tok.type != 'WS':
            yield tok

class ExpressionEvaluator:
    '''
    递归下降解析器的实现。每个方法 实现一个语法规则。
    使用._accept()方法 测试并接受当前的look前瞻令牌。
    使用._expect() 方法完全匹配并在输入上丢弃下一个令牌 (如果不匹配，则会产生一个同步错误)。
    '''

    def parse(self, text):
        self.tokens = generate_tokens(text)

        self.tok = None  # Last symbol consumed
        self.nexttok = None  # Next symbol tokenized
        self._advance()  # Load first lookahead token
        return self.expr()

    def _advance(self):
        'Advance one token ahead'

        self.tok, self.nexttok = self.nexttok, next(self.tokens, None)

    def _accept(self, toktype):
        'Test and consume the next token if it matches toktype'

        if self.nexttok and self.nexttok.type == toktype:
            self._advance()
            return True
        else:
            return False

    def _expect(self, toktype):
        'Consume next token if it matches toktype or raise SyntaxError'

        if not self._accept(toktype):
            raise SyntaxError('Expected ' + toktype)

    # Grammar rules follow
    def expr(self):

        "expression ::= term { ('+'|'-') term }*"
        exprval = self.term()
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.tok.type
            right = self.term()
            if op == 'PLUS':
                exprval += right
            elif op == 'MINUS':
                exprval -= right
        return exprval

    def term(self):
        "term ::= factor { ('*'|'/') factor }*"

        termval = self.factor()
        while self._accept('TIMES') or self._accept('DIVIDE'):
            op = self.tok.type
            right = self.factor()
            if op == 'TIMES':
                termval *= right
            elif op == 'DIVIDE':
                termval /= right
        return termval

    def factor(self):
        "factor ::= NUM | ( expr )"

        if self._accept('NUM'):
            return int(self.tok.value)
        elif self._accept('LPAREN'):
            exprval = self.expr()
            self._expect('RPAREN')
            return exprval
        else:
            raise SyntaxError('Expected NUMBER or LPAREN')


def descent_parser():
    e = ExpressionEvaluator()
    print(e.parse('2'))
    print(e.parse('2 + 3'))
    print(e.parse('2 + 3 * 4'))
    print(e.parse('2 + (3 + 4) * 5'))
    # print(e.parse('2 + (3 + * 4)'))
    # Traceback (most recent call last):
    # File "<stdin>", line 1, in <module>
    # File "exprparse.py", line 40, in parse
    # return self.expr()
    # File "exprparse.py", line 67, in expr
    # right = self.term()
    # File "exprparse.py", line 77, in term
    # termval = self.factor()
    # File "exprparse.py", line 93, in factor
    # exprval = self.expr()
    # File "exprparse.py", line 67, in expr
    # right = self.term()
    # File "exprparse.py", line 77, in term
    # termval = self.factor()
    # File "exprparse.py", line 97, in factor
    # raise SyntaxError("Expected NUMBER or LPAREN")
    # SyntaxError: Expected NUMBER or LPAREN

if __name__ == '__main__':
    descent_parser()







