import sys
import os
import subprocess

def run_build():
    """Chạy lệnh build để cập nhật grammar mới nhất"""
    print(f"--- Đang cập nhật grammar (python3 run.py build) ---")
    try:
        # Gọi script run.py với lệnh build sử dụng chính python đang chạy script này
        subprocess.run([sys.executable, "run.py", "build"], check=True)
        print(f"--- Cập nhật thành công ---\n")
    except subprocess.CalledProcessError:
        print(f"Lỗi: Không thể build grammar. Vui lòng kiểm tra lại file .g4")
        sys.exit(1)

def get_detailed_tokens(source):
    """Get detailed token information with name and value."""
    sys.path.insert(0, os.path.abspath("build"))
    from antlr4 import InputStream, CommonTokenStream
    from TyCLexer import TyCLexer
    
    input_stream = InputStream(source)
    lexer = TyCLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    
    tokens = []
    for token in token_stream.tokens:
        token_name = lexer.symbolicNames[token.type] if token.type >= 0 else "EOF"
        token_value = token.text
        tokens.append((token_name, token_value))
    
    return tokens


def print_token_table(tokens):
    """Print tokens in a formatted table."""
    print("┌─────┬─────────────────────┬──────────────────────────────┐")
    print("│ No. │ Token Name          │ Token Value                  │")
    print("├─────┼─────────────────────┼──────────────────────────────┤")
    
    for idx, (name, value) in enumerate(tokens, 1):
        # Escape special characters for display
        display_value = value.replace('\n', '\\n').replace('\t', '\\t').replace('\r', '\\r')
        if len(display_value) > 28:
            display_value = display_value[:25] + "..."
        
        print(f"│ {idx:3d} │ {name:19s} │ {display_value:28s} │")
    
    print("└─────┴─────────────────────┴──────────────────────────────┘")


def debug_lexer():
    # Thực hiện build trước khi import các module phụ thuộc vào build/
    run_build()

    # Add project root to path so we can import Tokenizer
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))
    from tests.utils import Tokenizer, Parser
    
    input_file = "input.tyc"
    print(f"--- TyC Debug Tool ---")
    
    if not os.path.exists(input_file):
        print(f"Lỗi: Không tìm thấy file {input_file}. Đang tạo file mẫu...")
        with open(input_file, "w") as f:
            f.write("// Dán code vào đây\n")
        return

    print(f"Đang đọc code từ file: {input_file}\n")
    
    try:
        with open(input_file, "r") as f:
            source = f.read()
            
        if not source.strip():
            print("File trống!")
            return
        
        # 1. Chạy Lexer - Simple format
        print("=" * 70)
        print("                    LEXER - TOKEN STRING")
        print("=" * 70)
        tokenizer = Tokenizer(source)
        output = tokenizer.get_tokens_as_string()
        print(output)
        print()
        
        # 2. Chạy Lexer - Detailed format
        print("=" * 70)
        print("                 LEXER - DETAILED TOKENS")
        print("=" * 70)
        tokens = get_detailed_tokens(source)
        print_token_table(tokens)
        print()
        
        # 3. Chạy Parser
        print("=" * 70)
        print("                      PARSER STATUS")
        print("=" * 70)
        parser = Parser(source)
        result = parser.parse()
        if result == "success":
            print("✅ Chúc mừng! Cú pháp hợp lệ (Success)")
        else:
            print(f"❌ LỖI CÚ PHÁP:\n{result}")
        print()
        
        # 4. Parse Tree (nếu thành công)
        if result == "success":
            print("=" * 70)
            print("                      PARSE TREE")
            print("=" * 70)
            # Reuse Parser.get_tree_str() from utils.py
            tree_str = parser.get_tree_str()
            print(tree_str)
            print()
        
        print("=" * 70)
        print("💡 Tip: Copy chuỗi token vào 'expect' trong test case của bạn")
        print("=" * 70)
        
    except Exception as e:
        import traceback
        print(f"❌ Lỗi thực thi: {e}")
        print("\nTraceback:")
        traceback.print_exc()

if __name__ == "__main__":
    debug_lexer()
