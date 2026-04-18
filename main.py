import os, random
from tkinter import *





def main():
  #cor de texto
  RED = "\033[31m"
  GREEN = "\033[32m"
  PRETO = "\033[30m"
  BLUE = "\033[34m"
  #cor de fundo
  BG_RED = "\033[41m"
  BG_GREEN = "\033[42m"
  BG_MAGENTA = "\033[45m"
  BG_PRETO = "\033[40m"
  RESET = "\033[0m"



  vidaplayer = 300
  vidabot = 300
  print(f"{BLUE}================================== {RESET}")
  print(f"{BLUE}  Bem-Vindo ao jogo de Pokemon! {RESET}  ")
  print(f"{BLUE}=================================={RESET}")
  print(f"{PRETO}Escolha seu Pokemon inicial: {RESET} ")
  pokeplayer=input(f"{PRETO}Escolha entre bulbasaur , charmander ou squirtle: {RESET}")
  print(os.system("cls"))
  if pokeplayer != "bulbasaur" and pokeplayer != "charmander" and pokeplayer != "squirtle":
      print("Escolha apenas entre um dos três pokemons iniciais, ou tente escrever o nome completamente minusculo!")
      print(os.system("cls"))
      return
  
  pokebot=random.choice(["bulbasaur", "charmander", "squirtle"])
  print(f"O oponente escolheu {pokebot} como seu Pokemon inicial!")
  print(f"Você escolheu {pokeplayer} como seu Pokemon inicial! e seus ataques são: ")
  if pokeplayer == "bulbasaur":
      print("1. Folha Navalha")
      print("2. Chicote de Cipó")
      print("3. Espelho de folha")
      print("4. Derrubar")
  elif pokeplayer == "charmander":
      print("1. Brasas")
      print("2. Arranhão")
      print("3. Lança Chamas")
      print("4. Pulo Ardente")
  elif pokeplayer == "squirtle":
      print("1. Jato de Água")
      print("2. Mordida")
      print("3. Hidro Bomba")
      print("4. Água Benta")
  while True:
      
      ataqueplayer=int(input("Escolha o número do ataque que deseja usar: "))
      if pokeplayer == "bulbasaur":
          if ataqueplayer == 1:
              print("Você usou Folha Navalha!")
              if pokebot == "bulbasaur":
                  vidabot -= 20
                  
              elif pokebot == "charmander":
                  vidabot -= 10
                  
              elif pokebot == "squirtle":
                  vidabot -=50
          elif ataqueplayer == 2:
              print("Você usou Chicote de Cipó!")
              if pokebot == "bulbasaur":
                  vidabot -= 15
              elif pokebot == "charmander":
                  vidabot -= 5
              elif pokebot == "squirtle":
                  vidabot -=55          
          elif ataqueplayer == 3:
              print("Você usou Espelho de folha")
              resu=random.randint(1,2)
              if resu == 1:
                  print("O ataque refletiu e causou dano ao oponente!")
                  vidabot -= ataqueplayer + (ataqueplayer * 0.5)
              elif resu == 2:
                  print("Você Errou o ataque!")
          elif ataqueplayer == 4:
              print("Você usou Derrubar!")
              if pokebot == "bulbasaur" or pokebot == "charmander" or pokebot == "squirtle":
                  vidabot -= 30
          else:
              print("Ataque inválido! Tente novamente.")
              continue
      elif pokeplayer == "charmander":
          if ataqueplayer == 1:
              print("Você usou Brasas!")
              if pokebot == "bulbasaur":
                  vidabot -= 80
              elif pokebot == "charmander":
                  vidabot -= 20
              elif pokebot == "squirtle":
                  vidabot -= 5
          elif ataqueplayer == 2:
              print("Você usou Arranhão!")
              if pokebot =="charmander":
                  
                  vidabot -= 25
                  print(f"A vida do oponente é {vidabot}")
              elif pokebot == "bulbasaur":
                  vidabot -= 25
                  print(f"A vida do oponente é {vidabot}")
              elif pokebot == "squirtle":
                  
                  vidabot -= 25
                  print(f"A vida do oponente é {vidabot}")
              
          elif ataqueplayer == 3:
              print("Você usou Lança Chamas!")
              if pokebot == "bulbasaur":
                  vidabot -= 65
              elif pokebot == "charmander":
                  vidabot -= 20
              elif pokebot == "squirtle":
                  vidabot -= 5
              
          elif ataqueplayer == 4:
              print("Você usou Pulo Ardente!")
              resu2=random.randint(1,4)
              if resu2 == 1:
                  print("O ataque acertou o oponente e causou dano!")
                  if pokebot == "bulbasaur":
                      vidabot -=100
                  elif pokebot == "charmander":
                      vidabot -= 50
                  elif pokebot == "squirtle":
                      vidabot -= 25
              elif resu2 == 2 or resu2 == 3 or resu2 == 4:
                  print("O ataque errou o oponente!")
          else:
              print("Ataque inválido! Tente novamente.")
              continue
      elif pokeplayer == "squirtle":
          if ataqueplayer == 1:
              print("Você usou Jato de Água!")
              if pokebot == "bulbasaur":
                  vidabot -= 10
              elif pokebot == "charmander":
                  vidabot -= 50
              elif pokebot == "squirtle":
                  vidabot -= 20
          elif ataqueplayer == 2:
              print("Você usou Mordida!")
              if pokebot == "bulbasaur" or pokebot == "charmander" or pokebot == "squirtle":
                  vidabot -= 30
                  
          elif ataqueplayer == 3:
              print("Você usou Hidro Bomba!")
              if pokebot == "bulbasaur":
                  vidabot -= 25
              elif pokebot == "charmander":
                  vidabot -= 65
              elif pokebot == "squirtle":
                  vidabot -= 25
          elif ataqueplayer == 4:
              resu6=random.randint(1,3)
              print("Você usou Água Benta!")
              if resu6 == 1:
                  
                vidaplayer += 60
              elif resu6 == 2 :
                  print("O ataque falhou!")
              else:
                  print("O ataque falhou!")
              
          else:
              print("Ataque inválido! Tente novamente.")
              
              continue
      
      ataquebot=random.randint(1,4)
      if pokebot == "bulbasaur":
          if ataquebot  == 1:
              print("O oponente usou Folha Navalha!")
              if pokeplayer == "bulbasaur":
                  vidaplayer -= 20
              elif pokeplayer == "charmander":
                  vidaplayer -= 10
              elif pokeplayer == "squirtle":
                  vidaplayer -=50
          elif ataquebot == 2:
              print("O oponente usou Chicote de Cipó!")
              if pokeplayer == "bulbasaur":
                  vidaplayer -= 15
              elif pokeplayer == "charmander":
                  vidaplayer -= 5
              elif pokeplayer == "squirtle":
                  vidaplayer -=55
                     
          elif ataquebot == 3:
              print("O oponente usou Espelho de folha")
              resu3=random.randint(1,2)
              if resu3 == 1:
                  print("O ataque refletiu e causou dano a você!")
                  vidaplayer -= ataqueplayer + (ataqueplayer * 0.5)
              elif resu3 == 2:
                  print("O oponente errou o ataque!")
          elif ataquebot == 4:
              print("O oponente usou Derrubar!")
              if pokeplayer == "bulbasaur" or pokeplayer == "charmander" or pokeplayer == "squirtle":
                  vidaplayer -= 30
      elif pokebot == "charmander":
          if ataquebot == 1:
              print("O seu Oponente usou Brasas!")
              if pokeplayer == "bulbasaur":
                  vidaplayer -= 80
              elif pokeplayer == "charmander":
                  vidaplayer -= 20
              elif pokeplayer == "squirtle":
                  vidaplayer -= 5
                  
          elif ataquebot == 2:
              print("O oponente usou Arranhão!")
              if pokeplayer == "bulbasaur" or pokeplayer == "charmander" or pokeplayer == "squirtle":
                  vidaplayer -= 25
                  
          elif ataquebot == 3:
              print("O oponente usou Lança Chamas!")
              if pokeplayer == "bulbasaur":
                 
                  vidaplayer -= 65
              elif pokeplayer == "charmander":
                  vidaplayer -= 20
              elif pokeplayer == "squirtle":
                  vidaplayer -= 5
                  
          elif ataquebot == 4:
              print("O oponente usou Pulo Ardente!")
              resu4=random.randint(1,4)
              
              if resu4 == 1:
                  print("O ataque acertou você e causou dano!")
                  if pokeplayer == "bulbasaur":
                      vidaplayer -=100
                  elif pokeplayer == "charmander":
                      vidaplayer -= 50
                  elif pokeplayer == "squirtle":
                      vidaplayer -= 25
              elif resu4 == 2 or resu4 == 3 or resu4 == 4:
                  print("O ataque errou você!")
                  
      elif pokebot == "squirtle":
          if ataquebot == 1:
              print("O oponente usou Jato de Água!")
              if pokeplayer == "bulbasaur":
                  vidaplayer -= 10
              elif pokeplayer == "charmander":
                  vidaplayer -= 50
              elif pokeplayer == "squirtle":
                  vidaplayer -= 20
                  
          elif ataquebot == 2:
              print("O oponente usou Mordida!")
              if pokeplayer == "bulbasaur" or pokeplayer == "charmander" or pokeplayer == "squirtle":
                  vidaplayer -= 30
                  
          elif ataquebot == 3:
              print("O oponente usou Hidro Bomba!")
              if pokeplayer == "bulbasaur":
                  vidaplayer -= 25
              elif pokeplayer == "charmander":
                  vidaplayer -= 65
              elif pokeplayer == "squirtle":
                  vidaplayer -= 25
                  
          elif ataquebot == 4:
              print("O oponente usou Água Benta!")
              resu5=random.randint(1,3)
              if resu5 == 1:
                  
                vidabot += 60
              elif resu5 == 2:
                  print("O ataque falhou!")
              else:
                  print("O ataque falhou!")
      print(os.system("cls"))
      print(f"{BLUE}================================== {RESET}")
      print(f"{BLUE}  Bem-Vindo ao jogo de Pokemon! {RESET}  ")
      print(f"{BLUE}=================================={RESET}")
      print(f"O Seu oponente escolheu {pokebot} como seu Pokemon inicial!")
      print(f"Você escolheu {pokeplayer} como seu Pokemon inicial! e seus ataques são: ")
      print(f"{BLUE}=================================={RESET}")
      if pokeplayer == "bulbasaur":
        print("1. Folha Navalha")
        print("2. Chicote de Cipó")
        print("3. Espelho de folha")
        print("4. Derrubar")
      elif pokeplayer == "charmander":
         print("1. Brasas")
         print("2. Arranhão")
         print("3. Lança Chamas")
         print("4. Pulo Ardente")
      elif pokeplayer == "squirtle":
            print("1. Jato de Água")
            print("2. Mordida")
            print("3. Hidro Bomba")
            print("4. Água Benta")
      print(f"{BLUE}================================== {RESET}")
      print(f"Sua vida: {GREEN}{vidaplayer}{RESET}")
      print(f"Vida do oponente:{RED} {vidabot}{RESET}")
      print(f"{BLUE}==================================`{RESET}")
      if vidaplayer <= 0:
            print(f"{RED}Você perdeu! O oponente venceu a batalha!{RESET}")
            break
      elif vidabot <= 0:
            print(f"{GREEN}Parabéns! Você venceu a batalha!{RESET}")
            break
      

if __name__ == "__main__":
    main()    
