"""
Lexer test cases for TyC compiler
TODO: Implement 100 test cases for lexer
"""

import pytest
from tests.utils import Tokenizer

# ====== KEYWORD ======
def test_lexer_001():
    """1. kw_default"""
    tokenizer = Tokenizer('default')
    assert tokenizer.get_tokens_as_string() == 'default,<EOF>'

def test_lexer_002():
    """2. kw_else"""
    tokenizer = Tokenizer('else')
    assert tokenizer.get_tokens_as_string() == 'else,<EOF>'

def test_lexer_003():
    """3. kw_float"""
    tokenizer = Tokenizer('float')
    assert tokenizer.get_tokens_as_string() == 'float,<EOF>'

def test_lexer_004():
    """4. kw_string"""
    tokenizer = Tokenizer('string')
    assert tokenizer.get_tokens_as_string() == 'string,<EOF>'

def test_lexer_005():
    """5. kw_switch"""
    tokenizer = Tokenizer('switch')
    assert tokenizer.get_tokens_as_string() == 'switch,<EOF>'

def test_lexer_006():
    """6. kw_void"""
    tokenizer = Tokenizer('void')
    assert tokenizer.get_tokens_as_string() == 'void,<EOF>'


# ====== IDENTIFIER ======
def test_lexer_007():
    """7. id_whilex"""
    tokenizer = Tokenizer('whilex')
    assert tokenizer.get_tokens_as_string() == 'whilex,<EOF>'

def test_lexer_008():
    """8. id_return_"""
    tokenizer = Tokenizer('return_')
    assert tokenizer.get_tokens_as_string() == 'return_,<EOF>'

def test_lexer_009():
    """9. id__while"""
    tokenizer = Tokenizer('_while')
    assert tokenizer.get_tokens_as_string() == '_while,<EOF>'

def test_lexer_010():
    """10. id_Auto123_"""
    tokenizer = Tokenizer('Auto123_')
    assert tokenizer.get_tokens_as_string() == 'Auto123_,<EOF>'

def test_lexer_011():
    """11. id_case0"""
    tokenizer = Tokenizer('case0')
    assert tokenizer.get_tokens_as_string() == 'case0,<EOF>'

def test_lexer_012():
    """12. id_structural"""
    tokenizer = Tokenizer('structural')
    assert tokenizer.get_tokens_as_string() == 'structural,<EOF>'

def test_lexer_013():
    """13. id_if_else"""
    tokenizer = Tokenizer('if_else')
    assert tokenizer.get_tokens_as_string() == 'if_else,<EOF>'

def test_lexer_014():
    """14. id_breakfast"""
    tokenizer = Tokenizer('breakfast')
    assert tokenizer.get_tokens_as_string() == 'breakfast,<EOF>'

def test_lexer_015():
    """15. id_continue2"""
    tokenizer = Tokenizer('continue2')
    assert tokenizer.get_tokens_as_string() == 'continue2,<EOF>'


# ====== NUMERIC ======
def test_lexer_016():
    """16. int_0001"""
    tokenizer = Tokenizer('0001')
    assert tokenizer.get_tokens_as_string() == '0001,<EOF>'

def test_lexer_017():
    """17. int_1234567890"""
    tokenizer = Tokenizer('1234567890')
    assert tokenizer.get_tokens_as_string() == '1234567890,<EOF>'

def test_lexer_018():
    """18. float_98dot"""
    tokenizer = Tokenizer('98.')
    assert tokenizer.get_tokens_as_string() == '98.,<EOF>'

def test_lexer_019():
    """19. float_dot0001"""
    tokenizer = Tokenizer('.0001')
    assert tokenizer.get_tokens_as_string() == '.0001,<EOF>'

def test_lexer_020():
    """20. float_6022e23"""
    tokenizer = Tokenizer('6.022e23')
    assert tokenizer.get_tokens_as_string() == '6.022e23,<EOF>'

def test_lexer_021():
    """21. float_2E0"""
    tokenizer = Tokenizer('2E0')
    assert tokenizer.get_tokens_as_string() == '2E0,<EOF>'

def test_lexer_022():
    """22. float_0eplus5"""
    tokenizer = Tokenizer('0e+5')
    assert tokenizer.get_tokens_as_string() == '0e+5,<EOF>'

def test_lexer_023():
    """23. float_7e_minus01"""
    tokenizer = Tokenizer('7e-01')
    assert tokenizer.get_tokens_as_string() == '7e-01,<EOF>'

def test_lexer_024():
    """24. float_1dot0Eplus000"""
    tokenizer = Tokenizer('1.0E+000')
    assert tokenizer.get_tokens_as_string() == '1.0E+000,<EOF>'

def test_lexer_025():
    """25. float_pi_e0"""
    tokenizer = Tokenizer('3.14159e0')
    assert tokenizer.get_tokens_as_string() == '3.14159e0,<EOF>'

def test_lexer_026():
    """26. num_1e_split"""
    tokenizer = Tokenizer('1e')
    assert tokenizer.get_tokens_as_string() == '1,e,<EOF>'

def test_lexer_027():
    """27. num_1E_minus_split"""
    tokenizer = Tokenizer('1E-')
    assert tokenizer.get_tokens_as_string() == '1,E,-,<EOF>'

def test_lexer_028():
    """28. num_0dot0e_split"""
    tokenizer = Tokenizer('0.0e')
    assert tokenizer.get_tokens_as_string() == '0.0,e,<EOF>'

def test_lexer_029():
    """29. float_5dot_dot6"""
    tokenizer = Tokenizer('5..6')
    assert tokenizer.get_tokens_as_string() == '5.,.6,<EOF>'

def test_lexer_030():
    """30. float_dot5_dot6"""
    tokenizer = Tokenizer('.5.6')
    assert tokenizer.get_tokens_as_string() == '.5,.6,<EOF>'

def test_lexer_031():
    """31. float_10dot20dot30"""
    tokenizer = Tokenizer('10.20.30')
    assert tokenizer.get_tokens_as_string() == '10.20,.30,<EOF>'

def test_lexer_032():
    """32. float_42eplus7_dot1"""
    tokenizer = Tokenizer('42e+7.1')
    assert tokenizer.get_tokens_as_string() == '42e+7,.1,<EOF>'

def test_lexer_033():
    """33. float_9e9e9"""
    tokenizer = Tokenizer('9e9e9')
    assert tokenizer.get_tokens_as_string() == '9e9,e9,<EOF>'

def test_lexer_034():
    """34. num_1_000_split"""
    tokenizer = Tokenizer('1_000')
    assert tokenizer.get_tokens_as_string() == '1,_000,<EOF>'

def test_lexer_035():
    """35. num_0x10_split"""
    tokenizer = Tokenizer('0x10')
    assert tokenizer.get_tokens_as_string() == '0,x10,<EOF>'

def test_lexer_036():
    """36. float_000dot111"""
    tokenizer = Tokenizer('000.111')
    assert tokenizer.get_tokens_as_string() == '000.111,<EOF>'

def test_lexer_037():
    """37. float_dot1e2"""
    tokenizer = Tokenizer('.1e2')
    assert tokenizer.get_tokens_as_string() == '.1e2,<EOF>'

def test_lexer_038():
    """38. float_5Eplus9"""
    tokenizer = Tokenizer('5E+9')
    assert tokenizer.get_tokens_as_string() == '5E+9,<EOF>'

def test_lexer_039():
    """39. float_7dot0e_minus0"""
    tokenizer = Tokenizer('7.0e-0')
    assert tokenizer.get_tokens_as_string() == '7.0e-0,<EOF>'


# ====== MIXTURE ======
def test_lexer_040():
    """40. mix_p_plusplus_plus_q"""
    tokenizer = Tokenizer('p+++q')
    assert tokenizer.get_tokens_as_string() == 'p,++,+,q,<EOF>'

def test_lexer_041():
    """41. mix_m_minusminus_minusminus_n"""
    tokenizer = Tokenizer('m----n')
    assert tokenizer.get_tokens_as_string() == 'm,--,--,n,<EOF>'

def test_lexer_042():
    """42. mix_u_le_v_lt_w"""
    tokenizer = Tokenizer('u<=v<w')
    assert tokenizer.get_tokens_as_string() == 'u,<=,v,<,w,<EOF>'

def test_lexer_043():
    """43. mix_g_ge_h_gt_i"""
    tokenizer = Tokenizer('g>=h>i')
    assert tokenizer.get_tokens_as_string() == 'g,>=,h,>,i,<EOF>'

def test_lexer_044():
    """44. mix_lhs_neq_assign_rhs"""
    tokenizer = Tokenizer('lhs!==rhs')
    assert tokenizer.get_tokens_as_string() == 'lhs,!=,=,rhs,<EOF>'

def test_lexer_045():
    """45. mix_k_eq_assign_l"""
    tokenizer = Tokenizer('k===l')
    assert tokenizer.get_tokens_as_string() == 'k,==,=,l,<EOF>'

def test_lexer_046():
    """46. mix_r_or_s_and_t"""
    tokenizer = Tokenizer('r||s&&t')
    assert tokenizer.get_tokens_as_string() == 'r,||,s,&&,t,<EOF>'

def test_lexer_047():
    """47. mix_not_flag"""
    tokenizer = Tokenizer('!flag')
    assert tokenizer.get_tokens_as_string() == '!,flag,<EOF>'

def test_lexer_048():
    """48. mix_preinc_stmt"""
    tokenizer = Tokenizer('++counter;')
    assert tokenizer.get_tokens_as_string() == '++,counter,;,<EOF>'

def test_lexer_049():
    """49. mix_postdec_comma"""
    tokenizer = Tokenizer('value--,')
    assert tokenizer.get_tokens_as_string() == 'value,--,,,<EOF>'

def test_lexer_050():
    """50. mix_paren_add_mul"""
    tokenizer = Tokenizer('(alpha+beta)*gamma')
    assert tokenizer.get_tokens_as_string() == '(,alpha,+,beta,),*,gamma,<EOF>'

def test_lexer_051():
    """51. mix_brace_list_semi"""
    tokenizer = Tokenizer('{p,q};')
    assert tokenizer.get_tokens_as_string() == '{,p,,,q,},;,<EOF>'

def test_lexer_052():
    """52. mix_member_chain"""
    tokenizer = Tokenizer('obj.field1.field2')
    assert tokenizer.get_tokens_as_string() == 'obj,.,field1,.,field2,<EOF>'

def test_lexer_053():
    """53. mix_member_call_args"""
    tokenizer = Tokenizer('foo.bar(baz,qux)')
    assert tokenizer.get_tokens_as_string() == 'foo,.,bar,(,baz,,,qux,),<EOF>'

def test_lexer_054():
    """54. mix_paren_empty_structlit_stmt"""
    tokenizer = Tokenizer('({});')
    assert tokenizer.get_tokens_as_string() == '(,{,},),;,<EOF>'

def test_lexer_055():
    """55. mix_assign_chain_simple"""
    tokenizer = Tokenizer('a=b=c')
    assert tokenizer.get_tokens_as_string() == 'a,=,b,=,c,<EOF>'

def test_lexer_056():
    """56. mix_mod_div"""
    tokenizer = Tokenizer('num%den/2')
    assert tokenizer.get_tokens_as_string() == 'num,%,den,/,2,<EOF>'

def test_lexer_057():
    """57. mix_rel_eq"""
    tokenizer = Tokenizer('1<2==3')
    assert tokenizer.get_tokens_as_string() == '1,<,2,==,3,<EOF>'

def test_lexer_058():
    """58. mix_double_not"""
    tokenizer = Tokenizer('!!ok')
    assert tokenizer.get_tokens_as_string() == '!,!,ok,<EOF>'

def test_lexer_059():
    """59. mix_dec_then_arrow"""
    tokenizer = Tokenizer('left--->right')
    assert tokenizer.get_tokens_as_string() == 'left,--,-,>,right,<EOF>'

def test_lexer_060():
    """60. mix_lt_minus"""
    tokenizer = Tokenizer('p<-q')
    assert tokenizer.get_tokens_as_string() == 'p,<,-,q,<EOF>'

def test_lexer_061():
    """61. mix_ge_neg_int"""
    tokenizer = Tokenizer('score>=-1')
    assert tokenizer.get_tokens_as_string() == 'score,>=,-,1,<EOF>'

def test_lexer_062():
    """62. mix_inc_dec_prefix_combo"""
    tokenizer = Tokenizer('++--mix')
    assert tokenizer.get_tokens_as_string() == '++,--,mix,<EOF>'

def test_lexer_063():
    """63. mix_dec_inc_prefix_combo"""
    tokenizer = Tokenizer('--++mix2')
    assert tokenizer.get_tokens_as_string() == '--,++,mix2,<EOF>'

def test_lexer_064():
    """64. mix_block_comment_between"""
    tokenizer = Tokenizer('id1/**/id2')
    assert tokenizer.get_tokens_as_string() == 'id1,id2,<EOF>'

def test_lexer_065():
    """65. mix_line_comment_between"""
    tokenizer = Tokenizer('first//ignore\nsecond')
    assert tokenizer.get_tokens_as_string() == 'first,second,<EOF>'

def test_lexer_066():
    """66. mix_block_comment_multiline"""
    tokenizer = Tokenizer('/*multi\nline*/token')
    assert tokenizer.get_tokens_as_string() == 'token,<EOF>'

def test_lexer_067():
    """67. mix_two_comments_split"""
    tokenizer = Tokenizer('to/*one*/ken')
    assert tokenizer.get_tokens_as_string() == 'to,ken,<EOF>'

def test_lexer_068():
    """68. mix_formfeed_ws"""
    tokenizer = Tokenizer('\x0cunique\x0cName')
    assert tokenizer.get_tokens_as_string() == 'unique,Name,<EOF>'

def test_lexer_069():
    """69. mix_comments_and_lines"""
    tokenizer = Tokenizer('A/*c*/B//d\nC')
    assert tokenizer.get_tokens_as_string() == 'A,B,C,<EOF>'

def test_lexer_070():
    """70. mix_colon_usage"""
    tokenizer = Tokenizer('case1:do;')
    assert tokenizer.get_tokens_as_string() == 'case1,:,do,;,<EOF>'

def test_lexer_071():
    """71. mix_double_colon"""
    tokenizer = Tokenizer('label::')
    assert tokenizer.get_tokens_as_string() == 'label,:,:,<EOF>'

def test_lexer_072():
    """72. mix_many_args_ids"""
    tokenizer = Tokenizer('fn(a,b,c,d)')
    assert tokenizer.get_tokens_as_string() == 'fn,(,a,,,b,,,c,,,d,),<EOF>'

def test_lexer_073():
    """73. mix_many_args_nums"""
    tokenizer = Tokenizer('sum(1,2,3,4,5)')
    assert tokenizer.get_tokens_as_string() == 'sum,(,1,,,2,,,3,,,4,,,5,),<EOF>'

def test_lexer_074():
    """74. mix_paren_assign"""
    tokenizer = Tokenizer('r1=(s2+t3);')
    assert tokenizer.get_tokens_as_string() == 'r1,=,(,s2,+,t3,),;,<EOF>'

def test_lexer_075():
    """75. mix_structlit_4"""
    tokenizer = Tokenizer('{1,2,3,4}')
    assert tokenizer.get_tokens_as_string() == '{,1,,,2,,,3,,,4,},<EOF>'

def test_lexer_076():
    """76. mix_nested_structlit"""
    tokenizer = Tokenizer('{{1},{2}}')
    assert tokenizer.get_tokens_as_string() == '{,{,1,},,,{,2,},},<EOF>'

def test_lexer_077():
    """77. mix_empty_nested_structlit"""
    tokenizer = Tokenizer('{{}}')
    assert tokenizer.get_tokens_as_string() == '{,{,},},<EOF>'

def test_lexer_078():
    """78. str_tab_newline"""
    tokenizer = Tokenizer('"A\\tB\\nC"')
    assert tokenizer.get_tokens_as_string() == 'A\\tB\\nC,<EOF>'

def test_lexer_079():
    """79. str_backspace_formfeed_return"""
    tokenizer = Tokenizer('"\\b\\f\\r"')
    assert tokenizer.get_tokens_as_string() == '\\b\\f\\r,<EOF>'

def test_lexer_080():
    """80. str_escaped_quotes"""
    tokenizer = Tokenizer('"She said: \\"Yes\\""')
    assert tokenizer.get_tokens_as_string() == 'She said: \\"Yes\\",<EOF>'

def test_lexer_081():
    """81. str_path_esc_backslash"""
    tokenizer = Tokenizer('"path\\\\to\\\\dir"')
    assert tokenizer.get_tokens_as_string() == 'path\\\\to\\\\dir,<EOF>'

def test_lexer_082():
    """82. str_spaces_only"""
    tokenizer = Tokenizer('"   "')
    assert tokenizer.get_tokens_as_string() == '   ,<EOF>'

def test_lexer_083():
    """83. str_punctuations"""
    tokenizer = Tokenizer('"[{}](),;:"')
    assert tokenizer.get_tokens_as_string() == '[{}](),;:,<EOF>'

def test_lexer_084():
    """84. str_row_crlf"""
    tokenizer = Tokenizer('"row1\\r\\nrow2"')
    assert tokenizer.get_tokens_as_string() == 'row1\\r\\nrow2,<EOF>'

def test_lexer_085():
    """85. str_mix_escapes"""
    tokenizer = Tokenizer('"mix\\t\\n\\r\\f\\b"')
    assert tokenizer.get_tokens_as_string() == 'mix\\t\\n\\r\\f\\b,<EOF>'

def test_lexer_086():
    """86. str_single_backslash"""
    tokenizer = Tokenizer('"\\\\"')
    assert tokenizer.get_tokens_as_string() == '\\\\,<EOF>'

def test_lexer_087():
    """87. str_tab_word"""
    tokenizer = Tokenizer('"tab\\tspace"')
    assert tokenizer.get_tokens_as_string() == 'tab\\tspace,<EOF>'

def test_lexer_088():
    """88. str_quote_and_slash"""
    tokenizer = Tokenizer('"quote\\"and\\\\slash"')
    assert tokenizer.get_tokens_as_string() == 'quote\\"and\\\\slash,<EOF>'

def test_lexer_089():
    """89. str_digits_symbols"""
    tokenizer = Tokenizer('"v2.0_#"')
    assert tokenizer.get_tokens_as_string() == 'v2.0_#,<EOF>'

def test_lexer_090():
    """90. mix_string_decl_assign"""
    tokenizer = Tokenizer('string msg="ok";')
    assert tokenizer.get_tokens_as_string() == 'string,msg,=,ok,;,<EOF>'

def test_lexer_091():
    """91. mix_call_string_int"""
    tokenizer = Tokenizer('log("msg",1);')
    assert tokenizer.get_tokens_as_string() == 'log,(,msg,,,1,),;,<EOF>'


# ====== ERROR ======
def test_lexer_092():
    """92. err_illegal_escape_z"""
    tokenizer = Tokenizer('"bad\\z"')
    assert tokenizer.get_tokens_as_string() == 'Illegal Escape In String: bad\\z'

def test_lexer_093():
    """93. err_illegal_escape_in_middle"""
    tokenizer = Tokenizer('"ok\\nbad\\q"')
    assert tokenizer.get_tokens_as_string() == 'Illegal Escape In String: ok\\nbad\\q'

def test_lexer_094():
    """94. err_unclosed_eof"""
    tokenizer = Tokenizer('"unfinished text')
    assert tokenizer.get_tokens_as_string() == 'Unclosed String: unfinished text'

def test_lexer_095():
    """95. err_unclosed_newline"""
    tokenizer = Tokenizer('"line one\n')
    assert tokenizer.get_tokens_as_string() == 'Unclosed String: line one'

def test_lexer_096():
    """96. err_dangling_backslash"""
    tokenizer = Tokenizer('"endswith\\')
    assert tokenizer.get_tokens_as_string() == 'Error Token "'

def test_lexer_097():
    """97. err_mid_error_char_dollar"""
    tokenizer = Tokenizer('alpha$beta')
    assert tokenizer.get_tokens_as_string() == 'alpha,Error Token $'

def test_lexer_098():
    """98. err_single_caret"""
    tokenizer = Tokenizer('^')
    assert tokenizer.get_tokens_as_string() == 'Error Token ^'

def test_lexer_099():
    """99. err_mid_error_char_tilde"""
    tokenizer = Tokenizer('void~func')
    assert tokenizer.get_tokens_as_string() == 'void,Error Token ~'

def test_lexer_100():
    """100. err_mid_illegal_escape_assignment"""
    tokenizer = Tokenizer('id="a\\y";')
    assert tokenizer.get_tokens_as_string() == 'id,=,Illegal Escape In String: a\\y'
