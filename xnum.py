import random
import time
import os
from datetime import datetime

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    BLINK = '\033[5m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_logo():
    logo = f"""
{Colors.CYAN}{Colors.BOLD}
    ████████████████████████████████████████████████████
    █                                                  █
    █    ██████  ██   ██  ██████  ███   ██ ███████     █
    █    ██   ██ ██   ██ ██    ██ ████  ██ ██          █
    █    ██████  ███████ ██    ██ ██ ██ ██ █████       █
    █    ██      ██   ██ ██    ██ ██  ████ ██          █
    █    ██      ██   ██  ██████  ██   ███ ███████     █
    █                                                  █
    █           ████████ ███████ ███   ██              █
    █           ██       ██      ████  ██              █
    █           ██   ███ █████   ██ ██ ██              █
    █           ██    ██ ██      ██  ████              █
    █           ████████ ███████ ██   ███              █
    █                                                  █
    ████████████████████████████████████████████████████
    
    {Colors.YELLOW}           📱 GLOBAL PHONE NUMBER GENERATOR 📱
    {Colors.WHITE}                                     Created By : @Z4HAX
    {Colors.GREEN}                               Status: Ready for Generation
{Colors.END}
    """
    print(logo)

def loading_animation(text, duration=2):
    chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    end_time = time.time() + duration
    
    while time.time() < end_time:
        for char in chars:
            print(f"\r{Colors.YELLOW}{char} {text}{Colors.END}", end="", flush=True)
            time.sleep(0.1)
            if time.time() >= end_time:
                break
    print(f"\r{Colors.GREEN}✓ {text} Complete!{Colors.END}")

class PhoneNumberGenerator:
    def __init__(self):
        self.countries = {
            1: {
                "name": "France",
                "code": "fr",
                "patterns": ["+337", "+336"],
                "digit_count": 8
            },
            2: {
                "name": "Spain", 
                "code": "es",
                "patterns": ["+346"],
                "digit_count": 8
            },
            3: {
                "name": "Canada",
                "code": "ca", 
                "patterns": ["+1647"],
                "digit_count": 7
            },
            4: {
                "name": "Germany",
                "code": "de",
                "patterns": ["+49155", "+49157", "+49152"],
                "digit_count": 8
            },
            5: {
                "name": "Italy",
                "code": "it",
                "patterns": ["+39350", "+39351"],
                "digit_count": 7
            },
            6: {
                "name": "United Arab Emirates",
                "code": "ae",
                "patterns": ["+97152", "+97158"],
                "digit_count": 7
            },
            7: {
                "name": "Brazil",
                "code": "br",
                "patterns": ["+55"],
                "digit_count": 11
            },
            8: {
                "name": "United Kingdom",
                "code": "uk",
                "patterns": ["+4473", "+4474", "+4479", "+4477"],
                "digit_count": 8
            },
            9: {
                "name": "Switzerland",
                "code": "ch",
                "patterns": ["+4178"],
                "digit_count": 7
            },
            10: {
                "name": "Poland",
                "code": "pl",
                "patterns": ["+487", "+486", "+485", "+484"],
                "digit_count": 8
            },
            11: {
                "name": "Norway",
                "code": "no",
                "patterns": ["+47594"],
                "digit_count": 5
            },
            12: {
                "name": "Netherlands",
                "code": "nl",
                "patterns": ["+3161", "+3164", "+3165", "+3168", "+3162"],
                "digit_count": 7
            },
            13: {
                "name": "Israel",
                "code": "il",
                "patterns": ["+9725253", "+9725254", "+9725232"],
                "digit_count": 5
            },
            14: {
                "name": "China",
                "code": "cn",
                "patterns": ["+8613", "+8615", "+8618"],
                "digit_count": 9
            },
            15: {
                "name": "Russia",
                "code": "ru",
                "patterns": ["+7927", "+7937", "+7996", "+7923"],
                "digit_count": 7
            },
            16: {
                "name": "Australia",
                "code": "au",
                "patterns": ["+61432", "+61413", "+61466", "+61479", "+61480", "+61481"],
                "digit_count": 6
            },
            17: {
                "name": "Denmark",
                "code": "dk",
                "patterns": ["+4552", "+4549", "+4550", "+4581", "+4571"],
                "digit_count": 6
            },
            18: {
                "name": "Georgia",
                "code": "ge",
                "patterns": ["+995574", "+995592", "+995544", "+995500"],
                "digit_count": 6
            },
            19: {
                "name": "Iceland",
                "code": "is",
                "patterns": ["+354255", "+354655"],
                "digit_count": 5
            },
            20: {
                "name": "Mexico",
                "code": "mx",
                "patterns": ["+5259", "+5265", "+5258", "+5243"],
                "digit_count": 8
            }
        }

    def display_menu(self):
        print(f"\n{Colors.CYAN}{Colors.BOLD}{'='*60}")
        print(f"                    COUNTRY SELECTION MENU")
        print(f"{'='*60}{Colors.END}")
        
        for i in range(0, len(self.countries), 2):
            left_num = i + 1
            right_num = i + 2
            
            left_country = self.countries.get(left_num, {}).get("name", "")
            right_country = self.countries.get(right_num, {}).get("name", "")
            
            if left_country and right_country:
                print(f"{Colors.GREEN}{left_num:2d} - {left_country:<25} {Colors.BLUE}{right_num:2d} - {right_country}{Colors.END}")
            elif left_country:
                print(f"{Colors.GREEN}{left_num:2d} - {left_country}{Colors.END}")
        
        print(f"{Colors.CYAN}{Colors.BOLD}{'='*60}{Colors.END}")

    def generate_number(self, pattern, digit_count):
        """Generate a random phone number with the given pattern and digit count"""
        random_digits = ''.join([str(random.randint(0, 9)) for _ in range(digit_count)])
        return pattern + random_digits

    def save_numbers(self, numbers, country_code, country_name):
        """Save generated numbers to a file"""
        if not os.path.exists('Z4HAX'):
            os.makedirs('Z4HAX')
        
        filename = f"Z4HAX/{country_code}.txt"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"Generated Phone Numbers for {country_name}\n")
            f.write(f"Generated on: {timestamp}\n")
            f.write(f"Total Numbers: {len(numbers)}\n")
            f.write("="*50 + "\n\n")
            
            for number in numbers:
                f.write(number + "\n")
        
        return filename

    def generate_numbers_with_animation(self, country_choice, count):
        """Generate numbers with real-time display"""
        country = self.countries[country_choice]
        patterns = country["patterns"]
        digit_count = country["digit_count"]
        
        Z4HAX = []
        
        print(f"\n{Colors.YELLOW}{Colors.BOLD}Generating {count:,} numbers for {country['name']}...{Colors.END}")
        print(f"{Colors.CYAN}{'='*60}{Colors.END}")
        
        for i in range(count):
            pattern = random.choice(patterns)
            number = self.generate_number(pattern, digit_count)
            Z4HAX.append(number)
            
            if i % max(1, count // 100) == 0 or i == count - 1: 
                progress = (i + 1) / count * 100
                print(f"{Colors.GREEN}Success: {number} {Colors.CYAN}[{i+1:,}/{count:,}] {Colors.YELLOW}({progress:.1f}%){Colors.END}")
                time.sleep(0.01) 
        
        return Z4HAX

    def run(self):
        while True:
            clear_screen()
            display_logo()
            self.display_menu()
            
            try:
                print(f"\n{Colors.MAGENTA}{Colors.BOLD}Choose Which Country (1-{len(self.countries)}) or 0 to exit: {Colors.END}", end="")
                choice = int(input())
                
                if choice == 0:
                    print(f"{Colors.RED}Thank you for using Phone Number Generator!{Colors.END}")
                    break
                
                if choice not in self.countries:
                    print(f"{Colors.RED}Invalid choice! Please select a number between 1 and {len(self.countries)}{Colors.END}")
                    time.sleep(2)
                    continue
                
                print(f"\n{Colors.BLUE}{Colors.BOLD}How Many Numbers: {Colors.END}", end="")
                count = int(input())
                
                if count <= 0:
                    print(f"{Colors.RED}Please enter a positive number!{Colors.END}")
                    time.sleep(2)
                    continue
                
                if count > 1000000:
                    print(f"{Colors.YELLOW}Warning: Generating more than 1M numbers might take a while.{Colors.END}")
                    print(f"{Colors.BLUE}Continue? (y/n): {Colors.END}", end="")
                    confirm = input().lower()
                    if confirm != 'y':
                        continue
                
                start_time = time.time()
                loading_animation("Initializing Generator", 1)
                
                Z4HAX = self.generate_numbers_with_animation(choice, count)
                
                country = self.countries[choice]
                filename = self.save_numbers(Z4HAX, country["code"], country["name"])
                
                end_time = time.time()
                generation_time = end_time - start_time
                
                print(f"\n{Colors.GREEN}{Colors.BOLD}✓ Generation Complete!{Colors.END}")
                print(f"{Colors.CYAN}{'='*60}{Colors.END}")
                print(f"{Colors.WHITE}Country: {Colors.GREEN}{country['name']}{Colors.END}")
                print(f"{Colors.WHITE}Numbers Generated: {Colors.GREEN}{count:,}{Colors.END}")
                print(f"{Colors.WHITE}Time Taken: {Colors.GREEN}{generation_time:.2f} seconds{Colors.END}")
                print(f"{Colors.WHITE}Saved to: {Colors.GREEN}{filename}{Colors.END}")
                print(f"{Colors.CYAN}{'='*60}{Colors.END}")
                
                print(f"\n{Colors.BLUE}Press Enter to continue or type 'quit' to exit: {Colors.END}", end="")
                user_input = input()
                if user_input.lower() == 'quit':
                    break
                    
            except ValueError:
                print(f"{Colors.RED}Invalid input! Please enter a valid number.{Colors.END}")
                time.sleep(2)
            except KeyboardInterrupt:
                print(f"\n{Colors.RED}Operation cancelled by user.{Colors.END}")
                break
            except Exception as e:
                print(f"{Colors.RED}An error occurred: {str(e)}{Colors.END}")
                time.sleep(2)

if __name__ == "__main__":
    generator = PhoneNumberGenerator()
    generator.run()