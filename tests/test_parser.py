"""
Parser test cases for TyC compiler
TODO: Implement 100 test cases for parser
"""

import pytest
from tests.utils import Parser

# ====== VALID ======

def test_parser_001():
    """1. valid: minimal_void_func"""
    result = Parser('void bootstrap() { }').parse()
    assert result == 'success'

def test_parser_002():
    """2. valid: inferred_func_with_auto_and_assign"""
    result = Parser('launch() { auto x = 0; x = x + 1; }').parse()
    assert result == 'success'

def test_parser_003():
    """3. valid: struct_empty_and_use"""
    result = Parser('struct Empty { }; void make(){ Empty e; }').parse()
    assert result == 'success'

def test_parser_004():
    """4. valid: struct_pair_and_factory"""
    result = Parser('struct Pair { int first; int second; }; Pair buildPair(int left, int right){ Pair p = {left, right}; return p; }').parse()
    assert result == 'success'

def test_parser_005():
    """5. valid: float_avg"""
    result = Parser('float avg(float x, float y){ return (x + y) / 2.0; }').parse()
    assert result == 'success'

def test_parser_006():
    """6. valid: string_echo"""
    result = Parser('string echo(string msg){ return msg; }').parse()
    assert result == 'success'

def test_parser_007():
    """7. valid: if_else_blocks"""
    result = Parser('void choose(){ if (0) { action0(); } else { action1(); } }').parse()
    assert result == 'success'

def test_parser_008():
    """8. valid: dangling_else"""
    result = Parser('void nested(){ if(1) if(2) doA(); else doB(); }').parse()
    assert result == 'success'

def test_parser_009():
    """9. valid: while_block"""
    result = Parser('void counterLoop(){ int k = 0; while (k < 3) { k = k + 1; } }').parse()
    assert result == 'success'

def test_parser_010():
    """10. valid: while_single_stmt"""
    result = Parser('void counterLoop2(){ int k = 0; while (k < 3) k = k + 1; }').parse()
    assert result == 'success'

def test_parser_011():
    """11. valid: for_no_cond"""
    result = Parser('void forNoCond(){ for(int i=0; ; i=i+1) { if(i==5) break; } }').parse()
    assert result == 'success'

def test_parser_012():
    """12. valid: for_no_update"""
    result = Parser('void forNoUpdate(){ int i=0; for(i=0; i<4; ) { i = i + 1; } }').parse()
    assert result == 'success'

def test_parser_013():
    """13. valid: for_all_empty"""
    result = Parser('void forAllEmpty(){ for( ; ; ) { break; } }').parse()
    assert result == 'success'

def test_parser_014():
    """14. valid: switch_empty"""
    result = Parser('void switchEmpty(){ switch(mode) { } }').parse()
    assert result == 'success'

def test_parser_015():
    """15. valid: switch_full"""
    result = Parser('void switchFull(){ switch(2){ case 0: call0(); break; case 1+1: call1(); break; default: callD(); break; } }').parse()
    assert result == 'success'

def test_parser_016():
    """16. valid: switch_empty_case_body"""
    result = Parser('void switchEmptyBodyCase(){ switch(tag){ case 10: case 11: done(); break; default: done2(); break; } }').parse()
    assert result == 'success'

def test_parser_017():
    """17. valid: inc_dec_statements"""
    result = Parser('void incDec(){ int n=1; ++n; n--; --n; n++; }').parse()
    assert result == 'success'

def test_parser_018():
    """18. valid: postfix_chain_with_inc"""
    result = Parser('void chainPostfix(){ obj.step().next(2).value++; }').parse()
    assert result == 'success'

def test_parser_019():
    """19. valid: assign_member_chain"""
    result = Parser('void assignMember(){ data.item.count = 7; }').parse()
    assert result == 'success'

def test_parser_020():
    """20. valid: assign_paren_member"""
    result = Parser('void assignParenMember(){ (root).leaf = 1; }').parse()
    assert result == 'success'

def test_parser_021():
    """21. valid: assign_weird_lhs"""
    result = Parser('void assignWeirdLHS(){ (a+b).c = 2; }').parse()
    assert result == 'success'

def test_parser_022():
    """22. valid: assign_chain"""
    result = Parser('void assignChain(){ x = y = z = 9; }').parse()
    assert result == 'success'

def test_parser_023():
    """23. valid: struct_literal_stmt"""
    result = Parser('void structLitStmt(){ ({1,2,3}); }').parse()
    assert result == 'success'

def test_parser_024():
    """24. valid: empty_struct_literal_stmt"""
    result = Parser('void structLitEmptyStmt(){ ({}); }').parse()
    assert result == 'success'

def test_parser_025():
    """25. valid: nested_struct_literal_stmt"""
    result = Parser('void nestedStructLitStmt(){ ({{1},{2,3}}); }').parse()
    assert result == 'success'

def test_parser_026():
    """26. valid: call_with_complex_args"""
    result = Parser('void callComplexArgs(){ f(1+2, (3*4), {5,6}); }').parse()
    assert result == 'success'

def test_parser_027():
    """27. valid: float_return_exponent"""
    result = Parser('float expo(){ return 1e-2; }').parse()
    assert result == 'success'

def test_parser_028():
    """28. valid: inferred_return_stmt"""
    result = Parser('inferReturn(){ return; }').parse()
    assert result == 'success'

def test_parser_029():
    """29. valid: nested_struct_types"""
    result = Parser('struct Inner { int v; }; struct Outer { Inner in; float w; }; void useOuter(){ Outer o; o.in.v = 7; }').parse()
    assert result == 'success'

def test_parser_030():
    """30. valid: unknown_type_var_decl"""
    result = Parser('void unknownTypeVar(){ Widget w; }').parse()
    assert result == 'success'

def test_parser_031():
    """31. valid: struct_init_3_fields"""
    result = Parser('struct Box { int a; int b; int c; }; void makeBox(){ Box b = {1,2,3}; }').parse()
    assert result == 'success'

def test_parser_032():
    """32. valid: for_init_call_cond_call_update_call"""
    result = Parser('void forInitCall(){ for(setup(); ok(); tick()) { run(); } }').parse()
    assert result == 'success'

def test_parser_033():
    """33. valid: for_update_postinc"""
    result = Parser('void forUpdatePostInc(){ int i=0; for(i=0; i<2; i++) { step(i); } }').parse()
    assert result == 'success'

def test_parser_034():
    """34. valid: while_postinc"""
    result = Parser('void whilePostInc(){ int i=0; while(i<2) i++; }').parse()
    assert result == 'success'

def test_parser_035():
    """35. valid: if_complex_cond"""
    result = Parser('void ifComplexCond(){ if(!a && b || c) act(); }').parse()
    assert result == 'success'

def test_parser_036():
    """36. valid: return_expr_in_void"""
    result = Parser('void give(){ return 42; }').parse()
    assert result == 'success'

def test_parser_037():
    """37. valid: return_empty_in_int"""
    result = Parser('int get(){ return; }').parse()
    assert result == 'success'

def test_parser_038():
    """38. valid: string_escape_in_return"""
    result = Parser('string esc(){ return "hi\\nthere"; }').parse()
    assert result == 'success'

def test_parser_039():
    """39. valid: decl_after_stmt"""
    result = Parser('void declAfterStmt(){ call(); int x=0; x=x+1; }').parse()
    assert result == 'success'

def test_parser_040():
    """40. valid: nested_blocks"""
    result = Parser('void nestedBlocks(){ { int a=1; { int b=2; } } }').parse()
    assert result == 'success'

def test_parser_041():
    """41. valid: multiple_var_decls"""
    result = Parser('void multipleDecls(){ int a=1; float b=2.5; string c="z"; }').parse()
    assert result == 'success'

def test_parser_042():
    """42. valid: unary_mix"""
    result = Parser('void unaryMix(){ x = --y + ++z - -w; }').parse()
    assert result == 'success'

def test_parser_043():
    """43. valid: postfix_on_chained_call"""
    result = Parser('void postfixOnCall(){ foo()(1,2)--; }').parse()
    assert result == 'success'

def test_parser_044():
    """44. valid: call_with_struct_literals"""
    result = Parser('void callWithStructLit(){ send({1,2}, {"a","b"}); }').parse()
    assert result == 'success'

def test_parser_045():
    """45. valid: nested_call_args"""
    result = Parser('void nestedCallArgs(){ h(g(1,2), f(3)(4)); }').parse()
    assert result == 'success'

def test_parser_046():
    """46. valid: member_then_call_chain"""
    result = Parser('void memberThenCall(){ obj.fn(1).g(2,3); }').parse()
    assert result == 'success'

def test_parser_047():
    """47. valid: big_precedence_expr"""
    result = Parser('void precedence(){ result = a + b * c < d && e == f || !g; }').parse()
    assert result == 'success'

def test_parser_048():
    """48. valid: paren_precedence"""
    result = Parser('void parenPrecedence(){ result = ((a+b) * (c-d)); }').parse()
    assert result == 'success'

def test_parser_049():
    """49. valid: relational_chain"""
    result = Parser('void relChain(){ ok = 1 < 2 <= 3 >= 4; }').parse()
    assert result == 'success'

def test_parser_050():
    """50. valid: equality_chain"""
    result = Parser('void eqChain(){ ok = a==b!=c==d; }').parse()
    assert result == 'success'

def test_parser_051():
    """51. valid: mod_div_mul"""
    result = Parser('void modDivMul(){ v = a%b* c / d; }').parse()
    assert result == 'success'

def test_parser_052():
    """52. valid: assign_to_nested_paren_member"""
    result = Parser('void assignToParenExpr(){ ((x)).y = 1; }').parse()
    assert result == 'success'

def test_parser_053():
    """53. valid: call_no_args"""
    result = Parser('void callNoArgs(){ ping(); }').parse()
    assert result == 'success'

def test_parser_054():
    """54. valid: call_many_args"""
    result = Parser('void callManyArgs(){ pack(a,b,c,d,e,f); }').parse()
    assert result == 'success'

def test_parser_055():
    """55. valid: switch_with_blocks"""
    result = Parser('void switchWithBlocks(){ switch(key){ case 1: { int t=0; } break; default: { } break; } }').parse()
    assert result == 'success'

def test_parser_056():
    """56. valid: loop_in_switch"""
    result = Parser('void loopInSwitch(){ switch(flag){ case 0: while(i<1) i=i+1; break; default: for(;i<2;i=i+1) { } break; } }').parse()
    assert result == 'success'

def test_parser_057():
    """57. valid: if_in_for"""
    result = Parser('void ifInFor(){ for(int i=0; i<3; i=i+1) if(i!=1) go(i); }').parse()
    assert result == 'success'

def test_parser_058():
    """58. valid: continue_in_for"""
    result = Parser('void continueInFor(){ for(int i=0; i<3; i=i+1){ if(i==1) continue; stop(i); } }').parse()
    assert result == 'success'

def test_parser_059():
    """59. valid: multi_return_void"""
    result = Parser('void multiReturn(){ if(a) return; else return; }').parse()
    assert result == 'success'

def test_parser_060():
    """60. valid: float_calc_sequence"""
    result = Parser('float calc(){ float x=1.5; x = x * (x + 2.0); return x; }').parse()
    assert result == 'success'

def test_parser_061():
    """61. valid: string_assignments"""
    result = Parser('void stringOps(){ string s="a"; s = "b"; }').parse()
    assert result == 'success'

def test_parser_062():
    """62. valid: call_string_escape"""
    result = Parser('void callStringEsc(){ write("tab\\tend"); }').parse()
    assert result == 'success'

def test_parser_063():
    """63. valid: double_not"""
    result = Parser('void unaryNotNot(){ x = !!y; }').parse()
    assert result == 'success'

def test_parser_064():
    """64. valid: prefix_plus_minus"""
    result = Parser('void prefixPlusMinus(){ x = + - +1; }').parse()
    assert result == 'success'

def test_parser_065():
    """65. valid: postfix_after_member"""
    result = Parser('void postfixAfterMember(){ obj.val--; }').parse()
    assert result == 'success'

def test_parser_066():
    """66. valid: expr_as_stmt"""
    result = Parser('void exprAsStmt(){ (a+b*c); }').parse()
    assert result == 'success'

def test_parser_067():
    """67. valid: paren_lvalue_assign"""
    result = Parser('void parenAsLvalueAssign(){ (a) = (b); }').parse()
    assert result == 'success'

def test_parser_068():
    """68. valid: for_init_decl_no_init"""
    result = Parser('void forInitVarNoInit(){ for(float x; ; ) { break; } }').parse()
    assert result == 'success'

def test_parser_069():
    """69. valid: for_init_auto_struct"""
    result = Parser('void forInitAutoStruct(){ for(auto tmp = {1,2}; ; ) { break; } }').parse()
    assert result == 'success'

def test_parser_070():
    """70. valid: switch_const_complex"""
    result = Parser('void switchConstComplex(){ switch(0){ case -(1+2): ok(); break; default: ok2(); break; } }').parse()
    assert result == 'success'


# ====== ERROR ======

def test_parser_071():
    """71. invalid: bad_struct_missing_semi_between_members"""
    result = Parser('struct Bad { int x int y; };').parse()
    assert result == 'Error on line 1 col 19: int'

def test_parser_072():
    """72. invalid: bad_struct_missing_trailing_semi"""
    result = Parser('struct NoSemi { int x; }').parse()
    assert result == 'Error on line 1 col 24: <EOF>'

def test_parser_073():
    """73. invalid: bad_func_missing_name"""
    result = Parser('void () { }').parse()
    assert result == 'Error on line 1 col 5: ('

def test_parser_074():
    """74. invalid: bad_param_auto"""
    result = Parser('void f(auto x) { }').parse()
    assert result == 'Error on line 1 col 7: auto'

def test_parser_075():
    """75. invalid: bad_param_trailing_comma"""
    result = Parser('void f(int x, ) { }').parse()
    assert result == 'Error on line 1 col 14: )'

def test_parser_076():
    """76. invalid: bad_param_missing_comma"""
    result = Parser('void f(int x int y) { }').parse()
    assert result == 'Error on line 1 col 13: int'

def test_parser_077():
    """77. invalid: bad_vardecl_missing_id"""
    result = Parser('void f(){ int ; }').parse()
    assert result == 'Error on line 1 col 14: ;'

def test_parser_078():
    """78. invalid: bad_auto_decl_missing_id"""
    result = Parser('void f(){ auto = 1; }').parse()
    assert result == 'Error on line 1 col 15: ='

def test_parser_079():
    """79. invalid: bad_assign_missing_semi"""
    result = Parser('void f(){ x = 1 }').parse()
    assert result == 'Error on line 1 col 16: }'

def test_parser_080():
    """80. invalid: bad_return_missing_semi"""
    result = Parser('int f(){ return 1 }').parse()
    assert result == 'Error on line 1 col 18: }'

def test_parser_081():
    """81. invalid: bad_if_missing_rparen"""
    result = Parser('void f(){ if (1 { call(); } }').parse()
    assert result == 'Error on line 1 col 16: {'

def test_parser_082():
    """82. invalid: bad_while_missing_paren"""
    result = Parser('void f(){ while 1 { call(); } }').parse()
    assert result == 'Error on line 1 col 16: 1'

def test_parser_083():
    """83. invalid: bad_for_missing_semi_after_init"""
    result = Parser('void f(){ for(i=0 i<10; i=i+1) { } }').parse()
    assert result == 'Error on line 1 col 18: i'

def test_parser_084():
    """84. invalid: bad_for_missing_rparen"""
    result = Parser('void f(){ for(i=0; i<10; i=i+1 { } }').parse()
    assert result == 'Error on line 1 col 31: {'

def test_parser_085():
    """85. invalid: bad_switch_missing_braces"""
    result = Parser('void f(){ switch(x) case 1: break; }').parse()
    assert result == 'Error on line 1 col 20: case'

def test_parser_086():
    """86. invalid: bad_case_missing_colon"""
    result = Parser('void f(){ switch(x){ case 1 break; } }').parse()
    assert result == 'Error on line 1 col 28: break'

def test_parser_087():
    """87. invalid: bad_default_missing_colon"""
    result = Parser('void f(){ switch(x){ default break; } }').parse()
    assert result == 'Error on line 1 col 29: break'

def test_parser_088():
    """88. invalid: bad_break_no_semi"""
    result = Parser('void f(){ break }').parse()
    assert result == 'Error on line 1 col 16: }'

def test_parser_089():
    """89. invalid: bad_continue_no_semi"""
    result = Parser('void f(){ continue }').parse()
    assert result == 'Error on line 1 col 19: }'

def test_parser_090():
    """90. invalid: bad_assign_missing_rhs"""
    result = Parser('void f(){ x = ; }').parse()
    assert result == 'Error on line 1 col 14: ;'

def test_parser_091():
    """91. invalid: bad_expr_dangling_plus"""
    result = Parser('void f(){ x = 1 + ; }').parse()
    assert result == 'Error on line 1 col 18: ;'

def test_parser_092():
    """92. invalid: bad_call_double_comma"""
    result = Parser('void f(){ g(1,,2); }').parse()
    assert result == 'Error on line 1 col 14: ,'

def test_parser_093():
    """93. invalid: bad_unclosed_block"""
    result = Parser('void f(){ int x=0; ').parse()
    assert result == 'Error on line 1 col 19: <EOF>'

def test_parser_094():
    """94. invalid: bad_extra_rbrace"""
    result = Parser('void f() { } }').parse()
    assert result == 'Error on line 1 col 13: }'

def test_parser_095():
    """95. invalid: bad_struct_literal_missing_rbrace"""
    result = Parser('void f(){ x = {1,2; }').parse()
    assert result == 'Error on line 1 col 18: ;'

def test_parser_096():
    """96. invalid: bad_forvardec_missing_id"""
    result = Parser('void f(){ for(auto = 1; ; ) { } }').parse()
    assert result == 'Error on line 1 col 19: ='

def test_parser_097():
    """97. invalid: bad_illegal_token_at"""
    result = Parser('int 1a = 123;').parse()
    assert result == 'Error on line 1 col 4: 1'

def test_parser_098():
    """98. invalid: bad_case_missing_expr"""
    result = Parser('void f(){ switch(x){ case : break; } }').parse()
    assert result == 'Error on line 1 col 26: :'

def test_parser_099():
    """99. invalid: bad_else_missing_stmt"""
    result = Parser('void f(){ if(1) call(); else }').parse()
    assert result == 'Error on line 1 col 29: }'

def test_parser_100():
    """100. invalid: bad_func_decl_with_semi_only"""
    result = Parser('void f();').parse()
    assert result == 'Error on line 1 col 8: ;'
