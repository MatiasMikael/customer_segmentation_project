## Asiakassegmentointi: Customer Segmentation Project

### **Yleiskatsaus**
Tämä projekti käyttää K-means-klusterointia ryhmitelläkseen asiakkaat eri segmentteihin heidän vuositulojensa ja kulutustottumustensa perusteella. Kaikki projektin koodi noudattaa Pythonin virallisia PEP 8 -tyyliohjeita selkeyden, luettavuuden ja ylläpidettävyyden takaamiseksi. Projekti tarjoaa interaktiivisen raportin Streamlitin avulla, jossa käyttäjä voi tarkastella klustereita ja niiden ominaisuuksia selaimessa.

---

### **Työkalut ja kirjastot**

  - **Python**
  - **Pandas:** Datan käsittelyyn ja analysointiin.
  - **Matplotlib:** Klusterien visualisointiin scatter plotin avulla.
  - **Scikit-learn:** K-means-klusterointialgoritmin toteuttamiseen.
  - **Streamlit:** Interaktiivisen raportin luomiseen.
  - **OS ja Logging:** Tiedostojen hallintaan ja lokien tallentamiseen.
  - **ChatGPT:** Projektin suunnitteluun ja toteutukseen.
---

### **Skriptien kuvaus**
Projektin koodit on jaettu useisiin skripteihin eri vaiheita varten:

1. **`download_dataset.py`:**
   - Lataa datasetin Kagglesta.
   - Tallentaa datan `2_data`-kansioon.

2. **`data_segmentation.py`:**
   - Lataa datasetin.
   - Suorittaa K-means-klusteroinnin käyttäen `Annual Income (k$)` ja `Spending Score (1-100)` -ominaisuuksia.
   - Lisää datan joukkoon klusteritunnisteen ja tallentaa tulokset `segmented_Mall_Customers.csv` -tiedostoon `2_data`-kansioon.

3. **`data_visualization.py`:**
   - Visualisoi klusterit scatter plotin avulla.
   - Tallentaa scatter plotin kuvatiedostona `3_results`-kansioon.

4. **`streamlit_report.py`:**
   - Luo interaktiivisen Streamlit-raportin, jossa:
     - Näytetään scatter plot klustereista.
     - Tarjotaan klustereiden selitykset.
     - Käyttäjä voi suodattaa klustereita ja tarkastella niitä dynaamisesti.
   - Raportin voi avata selaimessa komennolla:
     ```bash
     streamlit run 1_scripts/streamlit_report.py
     ```

---

### **Lopputulos**
- **Scatter Plot:** Asiakassegmentit visualisoituna vuositulojen ja kulutustottumusten perusteella.
- **Interaktiivinen raportti:** Käyttäjät voivat tarkastella segmenttejä ja saada tietoa niiden ominaisuuksista suoraan selaimessa.
- **Analyysitulokset:** Datasetti, johon on lisätty klusteritunnisteet, on tallennettu `2_data`-kansioon ja valmis jatkoanalyyseihin.

---

### **Data ja lisenssi**
- **Data:** Projektin data on peräisin Kagglesta:  
  [Customer Segmentation Dataset](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python)
- **Lisenssi:** Tämä projekti on julkaistu MIT-lisenssillä.
