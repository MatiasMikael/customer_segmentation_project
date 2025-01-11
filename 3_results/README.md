# Asiakassegmentit ja klusteriselitykset

Tämä projekti käyttää K-means-klusterointia asiakassegmenttien muodostamiseen. Scatter plot näyttää asiakassegmentit klustereina vuositulojen (Annual Income) ja kulutustottumusten (Spending Score) perusteella.

## Klustereiden selitykset

- **Cluster 0:** Keskimääräiset tulot ja keskimääräinen kulutus (vuotuiset tulot: 40–70 k$)  
  Asiakkaat, joilla on kohtuulliset tulot ja keskimääräiset kulutustottumukset.

- **Cluster 1:** Korkeat tulot ja korkea kulutus (vuotuiset tulot: 70–140 k$)  
  Asiakkaat, jotka ansaitsevat paljon ja käyttävät aktiivisesti rahaa.

- **Cluster 2:** Matalat tulot ja korkea kulutus (vuotuiset tulot: 15–40 k$)  
  Asiakkaat, jotka kuluttavat suhteessa paljon tuloihinsa nähden.

- **Cluster 3:** Korkeat tulot ja matala kulutus (vuotuiset tulot: 70–140 k$)  
  Asiakkaat, joilla on korkea ostovoima mutta säästeliäs kulutuskäyttäytyminen.

- **Cluster 4:** Matalat tulot ja matala kulutus (vuotuiset tulot: 15–40 k$)  
  Asiakkaat, joilla on rajallinen ostovoima ja vähäinen kulutus.

## Kuva

Visualisointi on tallennettu tiedostoon `3_results/cluster_visualization_simple.png`. Se havainnollistaa segmentit ja niiden suhteet vuosituloihin ja kulutustottumuksiin.