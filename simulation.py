import random
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

def program():
    fig, ax = plt.subplots(num='Menscheitsende Simulation')

    hiddenValues = []
    hiddenRuns = []

    displayValues = []
    displayRuns = []

    simulationen = 10000

    def average(lst):
        return sum(lst) / len(lst)

    for run in range(simulationen):
        run += 1

        randomness = random.uniform(0.8, 1.1)

        hunger = random.randint(1,10)
        disaster = random.randint(1,10)
        war = random.randint(1,10)
        money = random.randint(1,10)

        remainingYears = hunger * disaster * war * money * randomness
        extingtion = 2023+remainingYears

        classifier = f"{run}\n\n{hunger}\n{disaster}\n{war}\n{money}"

        if run <= 10:
            displayValues.append(round(extingtion))
            displayRuns.append(classifier)

        hiddenValues.append(extingtion)
        hiddenRuns.append(classifier)

    ax.bar(displayRuns, displayValues)
    ax.set_ylabel('Jahr der Vernichtung')
    ax.set_xlabel('Durchlauf Nummer')
    ax.set_title('Jahr der Vernichtung der Menschheit')

    average = average(hiddenValues)
    averageText = f"Durchschnitt bei {simulationen} Simulationen ist: {str(round(average))}"
    print(averageText)

    with open("Python/WhenIsTheEnd/average.txt", "a") as f:
        f.write(f"{averageText}\n")
        f.close()

    plt.subplots_adjust(bottom=0.27)
    plt.show()

def update_version_file(version):
        with open("Python/WhenIsTheEnd/version.txt", "w") as file:
            file.write(str(version))
            file.close()

def updateCheck():
    # sourcery skip: merge-else-if-into-elif, swap-if-else-branches
    url_of_version_file = "https://raw.githubusercontent.com/CSL-Koga/updatecheckertest/main/version.txt"
    url_of_code = "https://raw.githubusercontent.com/CSL-Koga/updatecheckertest/main/simulation.py"

    with open("Python/WhenIsTheEnd/version.txt", "r+") as file:
        lines = file.readline()
        file.close()
    
    online_version = requests.get(url_of_version_file)

    if lines != "":
        if lines == str(online_version.content):
            program()
        else:
            print("Es ist eine neuere Version verfuegbar, jetzt upgraden? J/N")
            decision = str(input())
            if decision == "J":
                response = requests.get(url_of_code)
                soup = BeautifulSoup(response.text, 'html.parser')
                text = soup.get_text()

                response_version = requests.get(url_of_version_file)
                update_version_file(response_version.content)

                with open("Python/WhenIsTheEnd/average.txt", "w") as file:
                    file.write(text)
                    file.close()
            else:
                program()
    else:
        response = requests.get(url_of_version_file)
        update_version_file(response.content)
        print("Versionsdaten aktualisiert.")

updateCheck()
