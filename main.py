import screen1
import screen2
import screen3

def main():
    """Main function to run the Guessing Game."""
    current_screen = "screen1"  # Start with Screen 1
    
    while True:
        if current_screen == "screen1":
            # Run Screen 1 and get the next screen
            current_screen = screen1.main()
        
        elif current_screen == "screen2":
            # Run Screen 2 and get the next screen
            current_screen = screen2.main()
        
        elif current_screen == "screen3":
            # Run Screen 3 and get the next screen
            current_screen = screen3.main()

if __name__ == "__main__":
    main()

