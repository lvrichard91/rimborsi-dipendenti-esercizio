"""Parametri normativi per il calcolo dei rimborsi spese.

I massimali e il plafond mensile dipendono dalla data di sostenimento della
spesa (regime transitorio, Circolare MEF n. 18/2026, Sezione 7):

- spese fino al 31/12/2025: Circolare MEF n. 41/2024;
- spese dal 01/01/2026: Circolare MEF n. 18/2026.
"""

DECORRENZA_2026 = "2026-01-01"

PARAMETRI = {
    "2024": {  # Circolare 41/2024 — fino al 31/12/2025
        "trasferta_italia": 46.48,
        "trasferta_estero": 77.47,
        "pasto": 8.00,
        "km": 0.42,
        "notte": 150.00,
        "plafond": 1200.00,
        "riferimento": "Circolare MEF n. 41/2024",
    },
    "2026": {  # Circolare 18/2026 — dal 01/01/2026
        "trasferta_italia": 50.00,
        "trasferta_estero": 85.00,
        "pasto": 10.00,
        "km": 0.45,
        "notte": 170.00,
        "plafond": 1400.00,
        "riferimento": "Circolare MEF n. 18/2026",
    },
}

CATEGORIE = {
    "trasferta_italia": "Trasferta in Italia",
    "trasferta_estero": "Trasferta all'estero",
    "pasto": "Rimborso pasto",
    "chilometrico": "Rimborso chilometrico",
    "alloggio": "Rimborso alloggio",
}

CATEGORIE_A_GIORNATE = ("trasferta_italia", "trasferta_estero", "pasto")


def parametri(data_iso):
    """Parametri vigenti alla data di sostenimento (stringa ISO AAAA-MM-GG).

    Il confronto tra stringhe ISO è lessicografico e coincide con l'ordine
    cronologico: la data di decorrenza 2026-01-01 rientra nel regime 2026.
    """
    return PARAMETRI["2026"] if data_iso >= DECORRENZA_2026 else PARAMETRI["2024"]


def plafond_per_mese(mese):
    """Plafond mensile vigente per un mese nel formato AAAA-MM."""
    return parametri(mese + "-01")["plafond"]
