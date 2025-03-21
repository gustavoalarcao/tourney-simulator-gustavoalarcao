"""score"""
"""weighted matchs"""
"""two matches per phase"""

import random 
import time  
import sys
import msvcrt as ms
import emoji

teams = ['Grêmio', 'Palmeiras', 'Flamengo', 'Cruzeiro', 'Botafogo', 'Corinthians', 'Santos', 'Atlético Mineiro',
          'São Paulo', 'Fluminense', 'Vasco', 'Juventude', 'Bahia', 'Mirassol', 'Paranaense', 'Internacional']
teams_2 = ['Grêmio', 'Palmeiras', 'Flamengo', 'Cruzeiro', 'Botafogo', 'Corinthians', 'Santos', 'Atlético Mineiro',
          'São Paulo', 'Fluminense', 'Vasco', 'Juventude', 'Bahia', 'Mirassol', 'Paranaense', 'Internacional']

lac = ''
quarter_finalists = []
semi_finalists = []
bronze_dispute = []
finalists = []
champs = []
champs2 = []
vices = []
vices2 = []
years = []
years2 = []
year = 2025
year2 = 2025

ztl = '\u250f'
ztr = '\u2513'
zbl = '\u2517'
zbr = '\u251b' 
zh = '\u2501'
zv = '\u2503'
line = '\u2504'
vs = f'{zv}  x{lac:>17}{zv}'

trophy = emoji.emojize(':trophy:')
gold = emoji.emojize(':1st_place_medal:')
silver = emoji.emojize(':2nd_place_medal:')
bronze = emoji.emojize(':3rd_place_medal:')
w = emoji.emojize(':check_mark_button:')

reset = '\033[0m'
color = '\033[35m'

def r16():
    global t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, p1, p2, p3, p4, p5, p6, p7, p8
    random.shuffle(teams)
    t1 = teams.pop()
    t2 = teams.pop()
    t3 = teams.pop()
    t4 = teams.pop()
    t5 = teams.pop()
    t6 = teams.pop()
    t7 = teams.pop()
    t8 = teams.pop()
    t9 = teams.pop()
    t10 = teams.pop()
    t11 = teams.pop()
    t12 = teams.pop()
    t13 = teams.pop()
    t14 = teams.pop()
    t15 = teams.pop()
    t16 = teams.pop()
    m1 = [t1, t2]
    m2 = [t3, t4]
    m3 = [t5, t6]
    m4 = [t7, t8]
    m5 = [t9, t10]
    m6 = [t11, t12]
    m7 = [t13, t14]
    m8 = [t15, t16]
    p1 = random.choice(m1)
    p2 = random.choice(m2)
    p3 = random.choice(m3)
    p4 = random.choice(m4)
    p5 = random.choice(m5)
    p6 = random.choice(m6)
    p7 = random.choice(m7)
    p8 = random.choice(m8)
    quarter_finalists_2 = [p1, p2, p3, p4, p5, p6, p7, p8]
    quarter_finalists.extend(quarter_finalists_2)

def quarters():
    global tt1, tt2, tt3, tt4, tt5, tt6, tt7, tt8, pp1, pp2, pp3, pp4
    tt1 = quarter_finalists[0]
    tt2 = quarter_finalists[1]
    tt3 = quarter_finalists[2]
    tt4 = quarter_finalists[3]
    tt5 = quarter_finalists[4]
    tt6 = quarter_finalists[5]
    tt7 = quarter_finalists[6]
    tt8 = quarter_finalists[7]
    m9 = [tt1, tt2]
    m10 = [tt3, tt4]
    m11 = [tt5, tt6]
    m12 = [tt7, tt8]
    pp1 = random.choice(m9)
    pp2 = random.choice(m10)
    pp3 = random.choice(m11)
    pp4 = random.choice(m12)
    semi_finalists_2 = [pp1, pp2, pp3, pp4]
    semi_finalists.extend(semi_finalists_2)

def semis():
    global ttt1, ttt2, ttt3, ttt4, ppp1, ppp2
    ttt1 = semi_finalists[0]
    ttt2 = semi_finalists[1]
    ttt3 = semi_finalists[2]
    ttt4 = semi_finalists[3]
    m13 = [ttt1, ttt2]
    m14 = [ttt3, ttt4]
    ppp1 = random.choice(m13)
    ppp2 = random.choice(m14)
    finalists.append(ppp1)
    finalists.append(ppp2)
    if ppp1 == ttt1:
        bronze_dispute.append(ttt2)
    else:
        bronze_dispute.append(ttt1)
    if ppp2 == ttt3:
        bronze_dispute.append(ttt4)
    else:
        bronze_dispute.append(ttt3)

def third_place():
    global tttt1, tttt2, pppp1
    tttt1 = bronze_dispute[0]
    tttt2 = bronze_dispute[1]
    m15 = [tttt1, tttt2]
    pppp1 = random.choice(m15)

def final():
    global ttttt1, ttttt2, ppppp1, ppppp2, year2
    ttttt1 = finalists[0]
    ttttt2 = finalists[1]
    m16 = [ttttt1, ttttt2]
    ppppp1 = random.choice(m16)
    champs.append(ppppp1)
    champs2.append(ppppp1)
    m16.remove(ppppp1)
    ppppp2 = m16[0]
    vices.append(ppppp2)
    vices2.append(ppppp2)
    m16.clear()
    years.append(year2)
    years2.append(year2)
    year2 += 1

"""                                         inputs                       ----------------------------"""

def r16_output():
    time.sleep(1)
    print()
    time.sleep(0.25)
    r16() 
    print(f'{color}round of 16{lac:>48}round of 16){reset}')
    print(f'{ztl}{lac:{zh}>20}{ztr}{lac:>40}{ztl}{lac:{zh}>20}{ztr}')  #oitavas
    print(f'{zv} {t1:<19}{zv}{lac:>40}{zv} {t3:<19}{zv}\n{vs}{lac:>13}COPA DO BRASIL{lac:3}{vs:>32}\n{zv} {t2:<19}{zv}{lac:>17}({year}){lac:>17}{zv} {t4:<19}{zv}')
    print(f'{zbl}{lac:{zh}>20}{zbr}{lac:>40}{zbl}{lac:{zh}>20}{zbr}')
    time.sleep(1)
    print(f'{w} {p1:<21}{lac:>38}{w} {p2}')
    loading()
    print(f'{color}round of 16(3){lac:>48}round of 16(4){reset}')  
    print(f'{ztl}{lac:{zh}>20}{ztr}{lac:>40}{ztl}{lac:{zh}>20}{ztr}')  #oitavas
    print(f'{zv} {t5:<19}{zv}{lac:>40}{zv} {t7:<19}{zv}\n{vs}{lac:>13}COPA DO BRASIL{lac:3}{vs:>32}\n{zv} {t6:<19}{zv}{lac:>17}({year}){lac:>17}{zv} {t8:<19}{zv}')
    print(f'{zbl}{lac:{zh}>20}{zbr}{lac:>40}{zbl}{lac:{zh}>20}{zbr}')
    time.sleep(1)
    print(f'{w} {p3:<21}{lac:>38}{w} {p4}')
    loading()
    print(f'{color}round of 16(5){lac:>48}round of 16(6){reset}')
    print(f'{ztl}{lac:{zh}>20}{ztr}{lac:>40}{ztl}{lac:{zh}>20}{ztr}')  #oitavas
    print(f'{zv} {t9:<19}{zv}{lac:>40}{zv} {t11:<19}{zv}\n{vs}{lac:>13}COPA DO BRASIL{lac:3}{vs:>32}\n{zv} {t10:<19}{zv}{lac:>17}({year}){lac:>17}{zv} {t12:<19}{zv}')
    print(f'{zbl}{lac:{zh}>20}{zbr}{lac:>40}{zbl}{lac:{zh}>20}{zbr}')
    time.sleep(1)
    print(f'{w} {p5:<21}{lac:>38}{w} {p6}')
    loading()
    print(f'{color}round of 16(7){lac:>48}round of 16(8){reset}')
    print(f'{ztl}{lac:{zh}>20}{ztr}{lac:>40}{ztl}{lac:{zh}>20}{ztr}')  #oitavas
    print(f'{zv} {t13:<19}{zv}{lac:>40}{zv} {t15:<19}{zv}\n{vs}{lac:>13}COPA DO BRASIL{lac:3}{vs:>32}\n{zv} {t14:<19}{zv}{lac:>17}({year}){lac:>17}{zv} {t16:<19}{zv}')
    print(f'{zbl}{lac:{zh}>20}{zbr}{lac:>40}{zbl}{lac:{zh}>20}{zbr}')
    time.sleep(1)
    print(f'{w} {p7:<21}{lac:>38}{w} {p8}')
    loading()

def quarters_output(): 
    time.sleep(1)
    print()
    time.sleep(0.25)
    quarters()
    print(F'{color}quarters(1){lac:>51}quarters(2){reset}')  #quartas
    print(f'{ztl}{lac:{zh}>20}{ztr}{lac:>40}{ztl}{lac:{zh}>20}{ztr}')    
    print(f'{zv} {tt1:<19}{zv}{lac:>40}{zv} {tt3:<19}{zv}\n{vs}{lac:>13}COPA DO BRASIL{lac:3}{vs:>32}\n{zv} {tt2:<19}{zv}{lac:>17}({year}){lac:>17}{zv} {tt4:<19}{zv}')
    print(f'{zbl}{lac:{zh}>20}{zbr}{lac:>40}{zbl}{lac:{zh}>20}{zbr}')
    time.sleep(1)
    print(f'{w} {pp1:<21}{lac:>38}{w} {pp2}')
    loading()
    print(F'{color}quarters(3){lac:>51}quarters(4){reset}')  #quartas
    print(f'{ztl}{lac:{zh}>20}{ztr}{lac:>40}{ztl}{lac:{zh}>20}{ztr}')    
    print(f'{zv} {tt5:<19}{zv}{lac:>40}{zv} {tt7:<19}{zv}\n{vs}{lac:>13}COPA DO BRASIL{lac:3}{vs:>32}\n{zv} {tt6:<19}{zv}{lac:>17}({year}){lac:>17}{zv} {tt8:<19}{zv}')
    print(f'{zbl}{lac:{zh}>20}{zbr}{lac:>40}{zbl}{lac:{zh}>20}{zbr}')
    time.sleep(1)
    print(f'{w} {pp3:<21}{lac:>38}{w} {pp4}')
    loading()

def semis_output():
    time.sleep(1)
    print()
    time.sleep(0.25)
    print(f'{color}semis(1){lac:>54}semis(2){reset}') #semi
    semis()
    print(f'{ztl}{lac:{zh}>20}{ztr}{lac:>40}{ztl}{lac:{zh}>20}{ztr}')    
    print(f'{zv} {ttt1:<19}{zv}{lac:>40}{zv} {ttt3:<19}{zv}\n{vs}{lac:>13}COPA DO BRASIL{lac:3}{vs:>32}\n{zv} {ttt2:<19}{zv}{lac:>17}({year}){lac:>17}{zv} {ttt4:<19}{zv}')
    print(f'{zbl}{lac:{zh}>20}{zbr}{lac:>40}{zbl}{lac:{zh}>20}{zbr}')
    time.sleep(1)
    print(f'{w} {ppp1:<21}{lac:>38}{w} {ppp2}')
    loading()

def third_place_output():
    time.sleep(1)
    print()
    time.sleep(0.25)
    third_place()
    print(f'{color}3rd place{reset}') #terceiro lugar
    print(f'{ztl}{lac:{zh}>20}{ztr}')
    print(f'{zv} {tttt1:<19}{zv}\n{vs}{lac:>13}COPA DO BRASIL\n{zv} {tttt2:<19}{zv}{lac:>17}({year})')
    print(f'{zbl}{lac:{zh}>20}{zbr}')
    time.sleep(1)
    print(f'{bronze} {pppp1}')
    loading()

def final_output():
    time.sleep(1)
    print()
    time.sleep(0.25)
    final()
    print(f'{color}final{reset}')   #final
    print(f'{ztl}{lac:{zh}>20}{ztr}')
    print(f'{zv} {ttttt1:<19}{zv}\n{vs}{lac:>13}COPA DO BRASIL\n{zv} {ttttt2:<19}{zv}{lac:>17}({year})')
    print(f'{zbl}{lac:{zh}>20}{zbr}')
    time.sleep(1)
    print(f'{gold} {ppppp1}')
    print()
    time.sleep(1)
    print(f'{silver} {ppppp2}')
    loading()

"""                                         play                       ----------------------------"""

def stop():
    print()
    time.sleep(1)
    print('    shutting down...   ')
    time.sleep(1)
    print()
    time.sleep(1)
    sys.exit()
        
def tourney_reset():
    random.shuffle(teams_2)
    teams.extend(teams_2)
    quarter_finalists.clear()
    semi_finalists.clear()
    bronze_dispute.clear()
    finalists.clear()
    champs.extend(champs2)
    vices.extend(vices2)
    years.extend(years2)

def champs_per_year():
    for i in champs:
        for j in years:
            while len(champs) > 0:
                print(f'{years.pop(0)} - {trophy} {champs.pop(0)}')
                time.sleep(0.01)

def loading():
    time.sleep(1.5)
    print(' ')
    time.sleep(0.25)
    print(' ')
    time.sleep(0.25)
    print(' ')
    time.sleep(0.25)
    print(' ')
    time.sleep(0.25)

def play():
    global key_1, key_2, key_3, key_4, key_5, year
    print()
    r16_output()
    print()
    print('Press space or letters to continue,\n'
           'Other stuff to leave')
    key_1 = ms.getch()
    if key_1.isalpha() or key_1 == b' ':
        print()
        time.sleep(0.5)  
        print(f'{lac:{line}>140}')
        time.sleep(0.5)
        print()
        time.sleep(0.25)
        quarters_output()  
        print()
        print('Press space or letters to continue,\n'
               'Other stuff to leave')

    if not key_1.isalpha() and key_1 != b' ':
        stop() 
    key_2 = ms.getch()
    if key_2.isalpha() or key_2 == b' ':
        print()
        time.sleep(0.5)
        print(f'{lac:{line}>140}')
        time.sleep(0.5)         
        print()
        time.sleep(0.25)
        semis_output()  
        print()
        print('Press space or letters to continue,\n'
               'Other stuff to leave')
    if not key_2.isalpha() and key_2 != b' ':
        stop()
    key_3 = ms.getch()
    if key_3.isalpha() or key_3 == b' ':
        print()
        time.sleep(0.5)
        print(f'{lac:{line}>140}')
        time.sleep(0.5)  
        print()
        time.sleep(0.25)
        third_place_output()
        print()
        print('Press space or letters to continue,\n'
               'Other stuff to leave')
    if not key_3.isalpha() and key_3 != b' ':
        stop()
    key_4 = ms.getch()
    if key_4.isalpha() or key_4 == b' ':
        print()
        time.sleep(0.5)
        print(f'{lac:{line}>140}')
        time.sleep(0.5)  
        print()
        time.sleep(0.25)
        final_output()
        year += 1
        champs_per_year()
        loading()
        print('For another simulation press space or letter\n'
               'Other stuff to leave')
        print()
    if not key_4.isalpha() and key_4 != b' ':
        stop()
    key_5 = ms.getch()
    while key_5.isalpha() or key_5 == b' ':
        time.sleep(0.5)
        print(f'{lac:{line}>140}')
        time.sleep(0.5)
        print()
        time.sleep(0.25)
        tourney_reset()
        play()
    if not key_5.isalpha() and key_5 != b' ':
        stop()


play()







