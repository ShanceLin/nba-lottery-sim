import sys
import string
import random
from numpy.random import choice
import numpy

def main():
    input_file = sys.argv[1]

    with open(input_file, 'r') as l:
        teams = [line.strip() for line in l]
        teams.reverse()

    lottery_teams = []

    #cuts the teams to only the lottery teams
    for i in range(14):
        lottery_teams.append(teams[i])

    #set rates for first four picks
    results = []
    weights_first_ties = [.14, .14, .14, .125, .105, .09, .075, .06, .045, .03, .02, .015, .01, .005]
    weights_first = [.14, .14, .14, .125, .105, .09, .06, .06, .06, .03, .02, .01, .01, .01]
    weights_second_ties = [.13417, .13417, .13417, .12229, .10540, .09200, .07801, .06344, .04833, .03271, .02202, .01659, .01111, .00558]
    weights_third_ties = [.12749, .12749, .12749, .11891, .10555, .09409, .08138, .06745, .05231, .03600, .02450, .01856, .01249, .00631]
    weights_fourth_ties = [.11972, .11972, .11972, .11462, .10528, .09618, .08517, .07217, .05715, .04011, .02763, .02105, .01425, .00724]
    weights_second = [.134, .134, .134, .122, .105, .092, .063, .063, .063, .033, .022, .011, .011, .011]
    weights_third = [.127, .127, .127, .119, .105, .094, .067, .067, .067, .036, .024, .012, .012, .012]
    weights_fourth = [.119, .119, .119, .114, .105, .096, .072, .072, .072, .040, .028, .014, .014, .014]

    draw = random.choices(lottery_teams, weights_first, k=1)
    results.append(draw)
    for i in range(14):
        if results[0] == ([lottery_teams[i]]):
            location_first = i
    lottery_teams.pop(location_first)
    weights_second.pop(location_first)
    weights_third.pop(location_first)
    weights_fourth.pop(location_first)
    draw_second = random.choices(lottery_teams, weights_second, k=1)
    results.append(draw_second)
    for i in range(13):
        if results[1] == ([lottery_teams[i]]):
            location_second = i
    lottery_teams.pop(location_second)
    weights_second.pop(location_second)
    weights_third.pop(location_second)
    weights_fourth.pop(location_second)
    draw_third = random.choices(lottery_teams, weights_third, k=1)
    results.append(draw_third)
    for i in range(12):
        if results[2] == ([lottery_teams[i]]):
            location_third = i
    lottery_teams.pop(location_third)
    weights_third.pop(location_third)
    weights_fourth.pop(location_third)
    draw_fourth = random.choices(lottery_teams, weights_fourth, k=1)
    results.append(draw_fourth)
    for i in range(11):
        if results[3] == ([lottery_teams[i]]):
            location_fourth = i
    lottery_teams.pop(location_fourth)
    for i in range(len(lottery_teams)):
        results.append([lottery_teams[i]])

    #All the traded draft picks below
    if results[8] == ['Grizzlies']:
        results[8] = ['Celtics(via Grizzlies)']
    if results[9] == ['Grizzlies']:
        results[9] = ['Celtics(via Grizzlies)']
    if results[10] == ['Grizzlies']:
        results[10] = ['Celtics(via Grizzlies)']
    if results[11] == ['Grizzlies']:
        results[11] = ['Celtics(via Grizzlies)']
    if results[8] == ['Mavericks']:
        results[8] = ['Hawks(via Mavericks)']
    if results[9] == ['Mavericks']:
        results[9] = ['Hawks(via Mavericks)']
    if results[10] == ['Mavericks']:
        results[10] = ['Hawks(via Mavericks)']
    if results[11] == ['Mavericks']:
        results[11] = ['Hawks(via Mavericks)']
    if results[12] == ['Mavericks']:
        results[12] = ['Hawks(via Mavericks)']
    if results[0] == ['Kings']:
        results[0] = ['76ers(via Kings)']
    if results[1] == ['Kings']:
        results[1] = ['Celtics(via Kings)']
    if results[2] == ['Kings']:
        results[2] = ['Celtics(via Kings)']
    if results[3] == ['Kings']:
        results[3] = ['Celtics(via Kings)']
    if results[13] == ['Kings']:
        results[13] = ['Celtics(via Kings)']

    results = [i[0] for i in results]
    print("First Pick: ", results[0], "\n" "Second Pick: ", results[1], "\n" "Third Pick: ", results[2], "\n" "Fourth Pick: ", results[3], "\n" "Fifth Pick: ", results[4], "\n" "Sixth Pick: ", results[5], "\n" "Seventh Pick: ", results[6], "\n" "Eighth Pick: ", results[7], "\n" "Ninth Pick: ", results[8], "\n" "Tenth Pick: ", results[9], "\n" "Eleventh Pick: ", results[10], "\n" "Twelveth Pick: ", results[11], "\n" "Thirteenth Pick: ", results[12], "\n" "Fourteenth Pick: ", results[13],)
main()
