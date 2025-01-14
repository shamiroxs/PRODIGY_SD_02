import screen1
import screen2
import screen3

def main():
    """Main function to run the Guessing Game."""
    current_screen = "screen1"  
    
    while True:
        if current_screen == "screen1":
            current_screen = screen1.main()
        
        elif current_screen == "screen2":
            current_screen = screen2.main()
        
        elif current_screen == "screen3":
            current_screen = screen3.main()

if __name__ == "__main__":
    main()

