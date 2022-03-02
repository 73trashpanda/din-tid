import prototype

def main():
    utgift_navn = input('Beskriv utgiften du vil sjekke: ').upper()
    utgift_belop = int(input('Beløp på utgiften: '))
    brutto_arslonn = float(input('Brutto årslønn: '))
    skatte_prosent = float(input('Skattetrekkprosent: '))

    nettolonn = prototype.beregne_nettolonn(brutto_arslonn, skatte_prosent)

    fraksjon_utgift_av_nettolonn = prototype.fraksjon_utgift_av_nettolonn(utgift_belop, nettolonn)

    arsverk_timer = 1695 #37.5 timer/uke + 5 ukersferie
    antall_timer_jobb = prototype.antall_timer_jobb(arsverk_timer, fraksjon_utgift_av_nettolonn)
    antall_timer_jobb = round(antall_timer_jobb, 1)

    print(f"For utgiften {utgift_navn} som koster {utgift_belop} KR må du jobbe {antall_timer_jobb} TIMER for å dekke utgiften.")

if __name__=="__main__":
    main()


