"""
tests/test_lexer.py

100 lexer test cases for TyC.
- Token stream format: TOKENNAME,lexeme,TOKENNAME,lexeme,...,EOF
- Lexer errors: we assert by ERROR MESSAGE (not exception class) to avoid module-dup issues.
"""

import pytest
from unittest import TestCase
from tests.utils import Tokenizer

_tc = TestCase()


def lex(source: str) -> str:
    """Return token stream or raise lexer exception."""
    return Tokenizer(source).get_tokens_as_string()


# -------------------------
# 70 VALID cases
# -------------------------
VALID_CASES = [
    # 1-10: whitespace/comments
    ("empty", "", "EOF"),
    ("ws_only", "   \t\r\n\f  ", "EOF"),
    ("line_comment", "// cmt", "EOF"),
    ("line_comment_nl", "// cmt\n", "EOF"),
    ("block_comment", "/* cmt */", "EOF"),
    ("block_comment_nl", "/* a\nb */", "EOF"),
    ("block_has_line", "/* // inside */", "EOF"),
    ("line_has_block", "// /* inside */\n", "EOF"),
    ("kw_after_line_comment", "//a\nint", "INT,int,EOF"),
    ("kw_after_block_comment", "/*a*/float", "FLOAT,float,EOF"),

    # 11-20: keywords
    ("kw_int", "int", "INT,int,EOF"),
    ("kw_float", "float", "FLOAT,float,EOF"),
    ("kw_string", "string", "STRING,string,EOF"),
    ("kw_void", "void", "VOID,void,EOF"),
    ("kw_auto", "auto", "AUTO,auto,EOF"),
    ("kw_if_else", "if else", "IF,if,ELSE,else,EOF"),
    ("kw_while_for", "while for", "WHILE,while,FOR,for,EOF"),
    ("kw_switch", "switch", "SWITCH,switch,EOF"),
    ("kw_case_default", "case default", "CASE,case,DEFAULT,default,EOF"),
    ("kw_break_continue_return", "break continue return", "BREAK,break,CONTINUE,continue,RETURN,return,EOF"),

    # 21-30: identifiers
    ("id_a", "a", "ID,a,EOF"),
    ("id_A", "A", "ID,A,EOF"),
    ("id_underscore", "_x", "ID,_x,EOF"),
    ("id_mix", "MyVar_01", "ID,MyVar_01,EOF"),
    ("id_keyword_prefix", "intx", "ID,intx,EOF"),
    ("id_struct_name", "Point", "ID,Point,EOF"),
    ("id_long", "a_b_c_d_123", "ID,a_b_c_d_123,EOF"),
    ("id_digits_tail", "x9", "ID,x9,EOF"),
    ("id_double__", "__", "ID,__,EOF"),
    ("id__9", "_9", "ID,_9,EOF"),

    # 31-38: numbers
    ("int_0", "0", "INTLIT,0,EOF"),
    ("int_100", "100", "INTLIT,100,EOF"),
    ("int_big", "2500", "INTLIT,2500,EOF"),
    ("float_3_14", "3.14", "FLOATLIT,3.14,EOF"),
    ("float_1dot", "1.", "FLOATLIT,1.,EOF"),
    ("float_dot5", ".5", "FLOATLIT,.5,EOF"),
    ("float_exp", "1e4", "FLOATLIT,1e4,EOF"),
    ("float_exp_sign", "2E-3", "FLOATLIT,2E-3,EOF"),

    # 39-50: strings (IMPORTANT: keep escapes as raw, NOT unescaped)
    ("str_empty", '""', "STRINGLIT,,EOF"),
    ("str_hello", '"hello"', "STRINGLIT,hello,EOF"),
    ("str_space", '"hello world"', "STRINGLIT,hello world,EOF"),
    ("str_quote_escape", r'"a\"b"', r'STRINGLIT,a\"b,EOF'),
    ("str_backslash_escape", r'"a\\b"', r"STRINGLIT,a\\b,EOF"),
    ("str_tab_escape", r'"a\tb"', r"STRINGLIT,a\tb,EOF"),
    ("str_newline_escape", r'"a\nb"', r"STRINGLIT,a\nb,EOF"),
    ("str_carriage_escape", r'"a\rb"', r"STRINGLIT,a\rb,EOF"),
    ("str_backspace_escape", r'"a\bb"', r"STRINGLIT,a\bb,EOF"),
    ("str_formfeed_escape", r'"a\fb"', r"STRINGLIT,a\fb,EOF"),
    ("str_mix", r'"\\\" \t \n"', r'STRINGLIT,\\\" \t \n,EOF'),
    ("str_symbols", r'"/* not comment */"', r"STRINGLIT,/* not comment */,EOF"),

    # 51-60: operators (match your token names: MUL/DIV/MOD)
    ("op_arith", "+ - * / %", "PLUS,+,MINUS,-,MUL,*,DIV,/,MOD,%,EOF"),
    ("op_rel", "< <= > >= == !=", "LT,<,LE,<=,GT,>,GE,>=,EQ,==,NEQ,!=,EOF"),
    ("op_logic", "&& || !", "AND,&&,OR,||,NOT,!,EOF"),
    ("op_incdec", "++ --", "INC,++,DEC,--,EOF"),
    ("op_assign_dot", "= .", "ASSIGN,=,DOT,.,EOF"),
    ("op_seq", "x&&y||!z", "ID,x,AND,&&,ID,y,OR,||,NOT,!,ID,z,EOF"),
    ("op_cmp_mix", "a<=b>=c", "ID,a,LE,<=,ID,b,GE,>=,ID,c,EOF"),
    ("op_eqmix", "a==b!=c", "ID,a,EQ,==,ID,b,NEQ,!=,ID,c,EOF"),
    ("op_inc_prefix", "++x", "INC,++,ID,x,EOF"),
    ("op_dec_postfix", "x--", "ID,x,DEC,--,EOF"),

    # 61-70: separators + mixed snippets
    ("seps_all", "{ } ( ) ; , :", "LBRACE,{,RBRACE,},LPAREN,(,RPAREN,),SEMI,;,COMMA,,,COLON,:,EOF"),
    ("mix_decl", "int x=1;", "INT,int,ID,x,ASSIGN,=,INTLIT,1,SEMI,;,EOF"),
    ("mix_expr", "x=x+1*2;", "ID,x,ASSIGN,=,ID,x,PLUS,+,INTLIT,1,MUL,*,INTLIT,2,SEMI,;,EOF"),
    ("call_args", "f(1,2);", "ID,f,LPAREN,(,INTLIT,1,COMMA,,,INTLIT,2,RPAREN,),SEMI,;,EOF"),
    ("member_access", "p.x;", "ID,p,DOT,.,ID,x,SEMI,;,EOF"),
    ("struct_lit_empty", "{}", "LBRACE,{,RBRACE,},EOF"),
    ("struct_lit_nonempty", "{1,2}", "LBRACE,{,INTLIT,1,COMMA,,,INTLIT,2,RBRACE,},EOF"),
    ("line_comment_after_code", "int x; //c\n", "INT,int,ID,x,SEMI,;,EOF"),
    ("block_comment_inside", "auto/*c*/x;", "AUTO,auto,ID,x,SEMI,;,EOF"),
    ("ws_formfeed", "int\fx;", "INT,int,ID,x,SEMI,;,EOF"),
]

assert len(VALID_CASES) == 70


# -------------------------
# 30 ERROR cases (assert by message)
# -------------------------
ERROR_CASES = [
    # 1-10: ErrorToken
    ("err_at", "@", "Error Token @"),
    ("err_hash", "#", "Error Token #"),
    ("err_tilde", "~", "Error Token ~"),
    ("err_backtick", "`", "Error Token `"),
    ("err_caret", "^", "Error Token ^"),
    ("err_dollar", "$", "Error Token $"),
    ("err_question", "?", "Error Token ?"),
    ("err_single_bar", "|", "Error Token |"),   # '||' valid, '|' invalid
    ("err_single_amp", "&", "Error Token &"),   # '&&' valid, '&' invalid
    ("err_euro", "€", "Error Token €"),

    # 11-20: UncloseString
    ("unclose_eof", '"abc', "Unclosed String: abc"),
    ("unclose_nl", '"abc\n', "Unclosed String: abc"),
    ("unclose_crlf", '"abc\r\n', "Unclosed String: abc"),
    ("unclose_with_valid_escape", r'"a\n', r"Unclosed String: a\n"),
    ("unclose_with_quote_escape", r'"a\"', r'Unclosed String: a\"'),
    ("unclose_only_quote", '"', "Unclosed String: "),
    ("unclose_space", '"a b c', "Unclosed String: a b c"),
    ("unclose_tabs", "\"a\tb", "Unclosed String: a\tb"),
    ("unclose_backslash_end", r'"abc\\', r"Unclosed String: abc\\"),
    ("unclose_mixed", r'"x\\y\n', r"Unclosed String: x\\y\n"),

    # 21-30: IllegalEscape (message prints backslash once, like in your log)
    ("illegal_q", r'"a\q"', r"Illegal Escape In String: a\q"),
    ("illegal_0", r'"\0"', r"Illegal Escape In String: \0"),
    ("illegal_x", r'"abc\x"', r"Illegal Escape In String: abc\x"),
    ("illegal_mid", r'"ab\qcd"', r"Illegal Escape In String: ab\q"),
    ("illegal_z", r'"\z"', r"Illegal Escape In String: \z"),
    ("illegal_A", r'"A\A"', r"Illegal Escape In String: A\A"),
    ("illegal_9", r'"x\9"', r"Illegal Escape In String: x\9"),
    ("illegal_under", r'"_\_"', r"Illegal Escape In String: _\_"),
    ("illegal_percent", r'"%\%"', r"Illegal Escape In String: %\%"),
    ("illegal_combo", r'"ab\\\q"', r"Illegal Escape In String: ab\\\q"),
]

assert len(ERROR_CASES) == 30


@pytest.mark.parametrize("name,source,expected", VALID_CASES)
def test_lexer_valid_70(name, source, expected):
    assert lex(source) == expected


@pytest.mark.parametrize("name,source,expected_msg", ERROR_CASES)
def test_lexer_error_30(name, source, expected_msg):
    try:
        _ = lex(source)
        assert False, "Expected lexer error but got tokens"
    except Exception as e:
        assert str(e) == expected_msg


# def test_lexer_total_count_guard():
#     assert len(VALID_CASES) + len(ERROR_CASES) == 100
#     assert True
