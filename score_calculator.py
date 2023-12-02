"""
Auteur : Bertrand Awenze
"""
import json

with open("static/print.json", "r", encoding='utf-8') as file:
    infos = json.load(file)
    file.close()

SCORES = infos["NUM_VAL_SCORE"]

def take_user_input(num_of_course : int = 1) -> float:
    """
    Prends et valide la note entrée par l'utilisateur
    """
    user_input = input(infos["MSG_SCORE"].format(num_of_course)).capitalize()

    if user_input in SCORES:
        return SCORES[user_input]
    
    return take_user_input(num_of_course)

def compile_scores(exec_n: int)->None:
    """
    Interagit avec l'utilisateur.
    """
    print(infos["MSG_WELCOME"] + infos["NOTICE"].format(infos["AUTHOR"]) + 
          infos["URL_MASK"].format(infos['URL_REF'])) if exec_n == 0 else print

    number_of_courses = 0

    while number_of_courses < 1 : 
        try : 
            number_of_courses = int(input(infos["MSG_NB_C"]))
        except ValueError : 
            number_of_courses = 0

    score_obtained = []
    print()

    for i in range(number_of_courses):
        score_obtained.append(3 * take_user_input(i+1)) #3 est le nombre de crédits par défaut (cours magistraux)

    cumulative_average = (sum(score_obtained)/(3*number_of_courses))

    print(f"{infos['MSG_RES']} \033[1;34m {round(cumulative_average, 2)} / 4.33 \033[0m")

def run() ->  int:
    """
    Execution du programme
    Returns:
        int: exit code
    """
    exec_n = 0
    while True:
        compile_scores(exec_n)
        exec_n += 1
        print()
        if input(infos["MSG_CLOSE"]).capitalize() == "Y":
            return 0

if __name__ == '__main__':
    run()