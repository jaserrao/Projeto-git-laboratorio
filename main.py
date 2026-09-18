def boas_vindas():
    print("==========================================")
    print("  Projeto Laboratório de Git e GitHub     ")
    print("==========================================")

if __name__ == "__main__":
    boas_vindas()

def listar_ferramentas():
    ferramentas = ["Git", "GitHub", "Python", "HTML/CSS"]
    print("\nFerramentas praticadas neste projeto:")
    for item in ferramentas:
        print(f"- {item}")

if __name__ == "__main__":
    boas_vindas()
    listar_ferramentas()

def exibir_integrantes():
    print("\nIntegrantes da equipe:")
    print("1. João Arthur Alves Serrão")
    print("2. [Fernando França De Lima]")

if __name__ == "__main__":
    boas_vindas()
    listar_ferramentas()
    exibir_integrantes()