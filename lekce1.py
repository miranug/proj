# https://como-python.streamlit.app
import streamlit as st

# úkol 1 
# Vytvořte textový vstup, kde bude defaultní/výchozí hodnota "Jméno" a maximální počet znaků bude 5.
'''# Úkol 1'''
jmeno = st.text_input("Jméno", value="Jméno", max_chars=(5), key="jmeno")

# Úkol 2
# Vytvořte textový vstup, kde bude defaultní/výchozí hodnota "Příjmení" a bude mít schovaný label.
'''# Úkol 2'''
prijmeni = st.text_input("Přijmení", value="Přijmení", label_visibility="hidden", key="prijmeni")

# Úkol 3
# Vytvořte textový vstup, kde bude defaultní/výchozí hodnota "Město" a bude typ password a bude mít nápovědu "Zadejte město".
'''# Úkol 3'''
mesto = st.text_input("Město", value="Město", placeholder="Zadejte město", type=("password"), key="mesto")

# Úkol 4
# Spojte ty 3 textové vstupy dohromady proměnné spojeni_pomoci_plus a spojte je pomocí + znaménka.
'''# Úkol 4'''
spojeni_pomoci_plus = jmeno+prijmeni+mesto
st.write(spojeni_pomoci_plus)
# Úkol 5
# Spojte ty 3 textové vstupy dohromady proměnné spojeni_pomoci_fstring a spojte je pomocí f-stringu.
'''# Úkol 5'''
spojeni_pomoci_fstring = f"{jmeno} {prijmeni} {mesto}"
st.write(spojeni_pomoci_fstring)
# Úkol 6
# Nechte si od uživatele dodat jméno a příjmení. Zajistěte, že první písmeno jména a příjmení budou velké a zbytek malé a napište toto celé jméno pomocí f-stringu.
'''# Úkol 6'''
jmeno1 = st.text_input("Zadejte jméno", key="jmeno1")

prijmeni1 = st.text_input("Zadejte přijmení", key="prijmeni1")

jmeno_prijmeni = f"{jmeno1.capitalize()} {prijmeni1.capitalize()}"
st.write(jmeno_prijmeni)
