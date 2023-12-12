# Example script: example.py

def say_hello(name):
    print(f"Hello from the say_hello function! {name}")

# Check if the script is the main program
if __name__ == "__main__":
    print("This script is being run directly.")

    
    say_hello('narendra')
    
else:
    print("This script is being imported as a module.")