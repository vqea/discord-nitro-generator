import time, requests, string, numpy, colorama
from colorama import Fore, Back, Style

def check(nitro:str):
    url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
    response = requests.get(url)

    if response.status_code == 200: 
        print(f"valid | {nitro} \n")
        with open("nitro.txt", "w") as file:
            file.write(nitro + "\n")
        return True
    else:
        print(f"invalid | {nitro} \n")
        return False
        
class nitrogen:  # Initialise the class
    def __init__(self):
    
    def main(self): 
      print(f"""{Fore.TEAL}
         _ _                                
   _ __ (_) |_ _ __ ___     __ _  ___ _ __  
  | '_ \| | __| '__/ _ \   / _` |/ _ \ '_ \ 
  | | | | | |_| | | (_) | | (_| |  __/ | | |
  |_| |_|_|\__|_|  \___/   \__, |\___|_| |_|
                           |___/           
-------------------------------------------------------------------
            """
       
      valid = []
      invalid = 0
      chars = []
      chars[:0] = string.ascii_letters + string.digits
      
      c = numpy.random.choice(chars, size=[num, 16])
      for s in c:  # Loop over the amount of codes to check
          try:
              code = ''.join(x for x in s)
              url = f"https://discord.gift/{code}"
              result = check(url)
              if result:
                  valid.append(url)
              else: 
                  invalid += 1
          except KeyboardInterrupt:
              print("\ninterrupted by user")
              break
          except Exception as e:
                print(f"\nerror | {url} ") 
      print(f"""
        results:
         valid: {len(valid)}
         invalid: {invalid}
         valid codes: {', '.join(valid)}
            """)
            
if __name__ == '__main__':
    gen = nitrogen() 
    gen.main()
