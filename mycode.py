cat > hello.py << 'EOF'
#!/usr/bin/env python3

def greet(name="World"):
    """Simple greeting function"""
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet())
    name = input("Enter your name: ")
    print(greet(name))
EOF
