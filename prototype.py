# 1. input: beskrivelse og beløp
# 2. input: brutto lønn og skatteprosent
# 3.


# resultat: prosent av bruttolønn og antall timer som små jobbes for å

def beregne_nettolonn(bruttolonn, skatteprosent):
    skattefraksjon = ((skatteprosent) / 100)
    skatt = bruttolonn * skattefraksjon
    nettolonn = bruttolonn - skatt

    return nettolonn

def fraksjon_utgift_av_nettolonn(utgift_belop, nettolonn):
    fraksjon_utgift_av_nettolonn = utgift_belop / nettolonn

    return fraksjon_utgift_av_nettolonn

def antall_timer_jobb(arsverk_timer, fraksjon_utgift_av_nettolonn):
    antall_timer_jobb = arsverk_timer * fraksjon_utgift_av_nettolonn

    return antall_timer_jobb

if __name__=="__main__":
    fraksjon = fraksjon_utgift_av_nettolonn(30000, 300000)

    antall_timer = antall_timer_jobb(1695, fraksjon)
    print(antall_timer)
