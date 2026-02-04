"""
tests/test_parser.py

100 parser test cases for TyC.
- Valid: Parser(source).parse() must return "success"
- Invalid: must not be "success" and should contain "Error on line"
"""

import pytest
from tests.utils import Parser


def parse(source: str) -> str:
    return Parser(source).parse()


VALID = [
    # 1-10: minimal programs
    ("v01", "void main(){}"),
    ("v02", "void main(){return;}"),
    ("v03", "main(){}"),
    ("v04", "int main(){}"),
    ("v05", "struct Empty{}; void main(){}"),
    ("v06", "struct P{int x;}; void main(){}"),
    ("v07", "void main(){int x;}"),
    ("v08", "void main(){auto x;}"),
    ("v09", "void main(){auto x=1;}"),
    ("v10", "void main(){string s=\"hi\";}"),

    # 11-25: expressions
    ("v11", "void main(){auto x=1+2*3;}"),
    ("v12", "void main(){auto x=(1+2)*3;}"),
    ("v13", "void main(){auto x=1<2;}"),
    ("v14", "void main(){auto x=1<=2;}"),
    ("v15", "void main(){auto x=1==2;}"),
    ("v16", "void main(){auto x=1!=2;}"),
    ("v17", "void main(){auto x=1&&2||3;}"),
    ("v18", "void main(){auto x=!1;}"),
    ("v19", "void main(){int a;int b;int c; a=b=c=10;}"),
    ("v20", "void main(){int x=1; x++; ++x; x--; --x;}"),
    ("v21", "void main(){f();}"),
    ("v22", "void main(){f(1,2,3);}"),
    ("v23", "void main(){auto x = {1,2};}"),
    ("v24", "struct P{int x;int y;}; void main(){P p={1,2};}"),
    ("v25", "struct P{int x;}; void main(){P p={1}; p.x=2;}"),

    # 26-45: if/while/for/switch
    ("v26", "void main(){if(1) return;}"),
    ("v27", "void main(){if(1) return; else return;}"),
    ("v28", "void main(){if(1){int x;} else {int y;}}"),
    ("v29", "void main(){while(1){break;}}"),
    ("v30", "void main(){while(1){continue;}}"),
    ("v31", "void main(){for(;;){break;}}"),
    ("v32", "void main(){for(auto i=0;i<10;++i){break;}}"),
    ("v33", "void main(){int i=0; for(i=0;i<3;i++){continue;}}"),
    ("v34", "void main(){switch(1){}}"),
    ("v35", "void main(){switch(1){case 1: break;}}"),
    ("v36", "void main(){switch(1){case 1: break; default: break;}}"),
    ("v37", "void main(){switch(x){case 1+2: break;}}"),
    ("v38", "void main(){switch(x){case (4): break;}}"),
    ("v39", "void main(){switch(x){case +5: break;}}"),
    ("v40", "void main(){switch(x){case -6: break;}}"),
    ("v41", "void main(){for(;i<10;){i=i+1;}}"),
    ("v42", "void main(){for(i=0;;i++){break;}}"),
    ("v43", "void main(){for(i=0;i<10;i=i+1){break;}}"),
    ("v44", "void main(){while(i<10) i=i+1;}"),
    ("v45", "void main(){if(1) if(0) return; else return;}"),

    # 46-80: function/struct combos
    ("v46", "int add(int a,int b){return a+b;} void main(){add(1,2);}"),
    ("v47", "add(int a,int b){return a+b;} void main(){auto x=add(1,2);}"),
    ("v48", "void f(int x){return;} void main(){f(1);}"),
    ("v49", "struct A{int x;}; int get(A a){return a.x;} void main(){A a={1}; get(a);}"),
    ("v50", "struct P{int x;int y;}; void main(){P p={1,2}; p.x=p.y;}"),
    ("v51", "void main(){{{int x;}}}"),
    ("v52", "void main(){ {int x=1;} {float y=2.0;} }"),
    ("v53", "void main(){auto a=1; {auto b=2; a=b;} }"),
    ("v54", "void main(){printInt(1);}"),
    ("v55", "void main(){printString(\"hi\");}"),
    ("v56", "void main(){auto x=readInt();}"),
    ("v57", "void main(){auto x=readFloat();}"),
    ("v58", "void main(){auto x=readString();}"),
    ("v59", "struct E{}; void main(){E e={};}"),
    ("v60", "struct P{int x;}; void main(){P p; p.x=1; p.x++;}"),
    ("v61", "void main(){auto x=(1); auto y=((2));}"),
    ("v62", "void main(){auto x = (a=b=3) + 7;}"),
    ("v63", "void main(){auto x = f(g(1), h(2));}"),
    ("v64", "void main(){auto x = a.b.c;}"),
    ("v65", "void main(){auto x = a.b(1,2).c;}"),
    ("v66", "void main(){auto x = f()(1)(2);}"),
    ("v67", "void main(){auto x = (1<2) && (3<4) || 0;}"),
    ("v68", "void main(){auto x = --y;}"),
    ("v69", "void main(){auto x = ++y;}"),
    ("v70", "void main(){y++; y--; }"),
    ("v71", "void main(){auto x = (y++);}"),
    ("v72", "void main(){auto x = (y--);}"),
    ("v73", "void main(){int x=1; x = x * 2 / 3 % 4;}"),
    ("v74", "void main(){int x=1; x = +1 + -2;}"),
    ("v75", "void main(){return 1;}"),
    ("v76", "int f(){return 1;} void main(){auto x=f();}"),
    ("v77", "float f(){return 1.0;} void main(){auto x=f();}"),
    ("v78", "string f(){return \"a\";} void main(){auto x=f();}"),
    ("v79", "void main(){auto x={};}"),
    ("v80", "void main(){auto x={1,2,3};}"),
]

INVALID = [
    ("e01", "void main("),
    ("e02", "void main() {"),
    ("e03", "struct A{int x;} void main(){}"),       # missing ';' after struct
    ("e04", "void main(){int x}"),                   # missing ';'
    ("e05", "void main(){x=1}"),                     # missing ';'
    ("e06", "void main(){if() return;}"),
    ("e07", "void main(){while(){} }"),
    ("e08", "void main(){for(auto i=0 i<10;++i){} }"),
    ("e09", "void main(){switch(1){case 1 break;} }"),
    ("e10", "void main(){switch(1){case : break;} }"),
    ("e11", "void main(){break}"),
    ("e12", "void main(){return 1}"),
    ("e13", "void main(){auto x=1+;}"),
    ("e14", "void main(){printInt(1,);}"),
    ("e15", "int f(int x {return x;} void main(){}"),
    ("e16", "int f(x){return 1;} void main(){}"),
    ("e17", "struct {int x;}; void main(){}"),
    ("e18", "void main(){switch(){default: break;}}"),
    ("e19", "void main(){for(;;){ }"),               # missing '}'
    ("e20", "void main(){ { }"),                     # missing '}'
]

assert len(VALID) == 80
assert len(INVALID) == 20


@pytest.mark.parametrize("name,src", VALID)
def test_parser_valid_80(name, src):
    assert parse(src) == "success"


@pytest.mark.parametrize("name,src", INVALID)
def test_parser_invalid_20(name, src):
    out = parse(src)
    assert out != "success"
    assert "Error on line" in out


# def test_parser_total_count_guard():
#     assert len(VALID) + len(INVALID) == 100
#     assert True
