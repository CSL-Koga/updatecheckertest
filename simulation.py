import random
import matplotlib.pyplot as plt

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

def updateCheck():
    with open("Python/WhenIsTheEnd/version.txt", "r+") as file:
        lines = file.readline()
        print(lines)


updateCheck()
program()
