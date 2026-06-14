

BANK_DATA = {
    "starting_capital": 5000000,      
    "loan_interest_rate": 0.18,       
    "investment_interest_rate": 0.09   
}




INVESTORS = [
    {"id": 501, "name": "Volkan Şen", "deposit_amount": 750000, "duration_months": 12, "type": "investor", "status": "active", "credit_score": 840, "start_date": "2026-03-01", "branch": "Antalya"},
    {"id": 502, "name": "Buse Yilmaz", "deposit_amount": 320000, "duration_months": 24, "type": "investor", "status": "active", "credit_score": 760, "start_date": "2026-04-10", "branch": "Adana"},
    {"id": 503, "name": "Cengiz Aksu", "deposit_amount": 120000, "duration_months": 6, "type": "investor", "status": "closed", "credit_score": 670, "start_date": "2026-01-15", "branch": "Eskişehir"},
    {"id": 504, "name": "Dilek Çetin", "deposit_amount": 980000, "duration_months": 36, "type": "investor", "status": "active", "credit_score": 875, "start_date": "2026-02-25", "branch": "Antalya"},
    {"id": 505, "name": "Emre Öztürk", "deposit_amount": 250000, "duration_months": 12, "type": "investor", "status": "active", "credit_score": 730, "start_date": "2026-05-20", "branch": "Eskişehir"},
    {"id": 506, "name": "Fulya Demir", "deposit_amount": 450000, "duration_months": 18, "type": "investor", "status": "active", "credit_score": 795, "start_date": "2026-03-12", "branch": "Adana"},
    {"id": 507, "name": "Görkem Kaya", "deposit_amount": 620000, "duration_months": 12, "type": "investor", "status": "closed", "credit_score": 810, "start_date": "2026-02-01", "branch": "Antalya"},
    {"id": 508, "name": "Hale Arslan", "deposit_amount": 110000, "duration_months": 12, "type": "investor", "status": "active", "credit_score": 650, "start_date": "2026-06-10", "branch": "Antalya"},
    {"id": 509, "name": "İsmail Doğan", "deposit_amount": 1650000, "duration_months": 48, "type": "investor", "status": "active", "credit_score": 885, "start_date": "2026-01-08", "branch": "Eskişehir"},
    {"id": 510, "name": "Kader Şahin", "deposit_amount": 800000, "duration_months": 24, "type": "investor", "status": "active", "credit_score": 780, "start_date": "2026-07-15", "branch": "Adana"},
    {"id": 511, "name": "Levent Polat", "deposit_amount": 65000, "duration_months": 3, "type": "investor", "status": "closed", "credit_score": 615, "start_date": "2026-08-20", "branch": "Eskişehir"},
    {"id": 512, "name": "Mine Uzun", "deposit_amount": 290000, "duration_months": 12, "type": "investor", "status": "active", "credit_score": 745, "start_date": "2026-04-02", "branch": "Antalya"},
    {"id": 513, "name": "Nuri Kiliç", "deposit_amount": 1100000, "duration_months": 36, "type": "investor", "status": "active", "credit_score": 850, "start_date": "2026-01-30", "branch": "Adana"},
    {"id": 514, "name": "Özlem Bulut", "deposit_amount": 340000, "duration_months": 18, "type": "investor", "status": "active", "credit_score": 770, "start_date": "2026-09-05", "branch": "Eskişehir"},
    {"id": 515, "name": "Polat Tekin", "deposit_amount": 520000, "duration_months": 24, "type": "investor", "status": "active", "credit_score": 765, "start_date": "2026-05-14", "branch": "Antalya"},
    {"id": 516, "name": "Rüya Kurt", "deposit_amount": 90000, "duration_months": 6, "type": "investor", "status": "closed", "credit_score": 630, "start_date": "2026-10-12", "branch": "Adana"},
    {"id": 517, "name": "Sami Yavuz", "deposit_amount": 720000, "duration_months": 12, "type": "investor", "status": "active", "credit_score": 825, "start_date": "2026-06-01", "branch": "Eskişehir"},
    {"id": 518, "name": "Tülin Erdem", "deposit_amount": 560000, "duration_months": 24, "type": "investor", "status": "active", "credit_score": 755, "start_date": "2026-06-22", "branch": "Antalya"},
    {"id": 519, "name": "Utku Aksoy", "deposit_amount": 210000, "duration_months": 12, "type": "investor", "status": "active", "credit_score": 715, "start_date": "2026-11-15", "branch": "Adana"},
    {"id": 520, "name": "Veli Aydin", "deposit_amount": 840000, "duration_months": 36, "type": "investor", "status": "active", "credit_score": 840, "start_date": "2026-02-18", "branch": "Antalya"},
    {"id": 521, "name": "Yonca Koç", "deposit_amount": 125000, "duration_months": 12, "type": "investor", "status": "closed", "credit_score": 680, "start_date": "2026-12-01", "branch": "Eskişehir"},
    {"id": 522, "name": "Zafer Şimşek", "deposit_amount": 1500000, "duration_months": 60, "type": "investor", "status": "active", "credit_score": 899, "start_date": "2026-01-05", "branch": "Antalya"},
    {"id": 523, "name": "Zehra Altin", "deposit_amount": 380000, "duration_months": 18, "type": "investor", "status": "active", "credit_score": 740, "start_date": "2026-12-20", "branch": "Adana"},
    {"id": 524, "name": "Bilal Sönmez", "deposit_amount": 420000, "duration_months": 24, "type": "investor", "status": "active", "credit_score": 790, "start_date": "2026-04-28", "branch": "Eskişehir"},
    {"id": 525, "name": "Kadir Akin", "deposit_amount": 990000, "duration_months": 12, "type": "investor", "status": "active", "credit_score": 860, "start_date": "2026-03-22", "branch": "Antalya"}
]




DEBTORS = [
    {"id": 601, "name": "Anil Korkmaz", "loan_amount": 85000, "duration_months": 12, "type": "debtor", "status": "active", "credit_score": 830, "start_date": "2026-01-25", "branch": "Antalya"},
    {"id": 602, "name": "Beren Çelik", "loan_amount": 165000, "duration_months": 24, "type": "debtor", "status": "active", "credit_score": 740, "start_date": "2026-02-18", "branch": "Adana"},
    {"id": 603, "name": "Caner Güler", "loan_amount": 60000, "duration_months": 6, "type": "debtor", "status": "closed", "credit_score": 675, "start_date": "2025-12-15", "branch": "Eskişehir"},
    {"id": 604, "name": "Deniz Şen", "loan_amount": 105000, "duration_months": 18, "type": "debtor", "status": "active", "credit_score": 770, "start_date": "2026-04-12", "branch": "Antalya"},
    {"id": 605, "name": "Engin Özdemir", "loan_amount": 410000, "duration_months": 48, "type": "debtor", "status": "defaulted", "credit_score": 395, "start_date": "2026-01-22", "branch": "Eskişehir"},
    {"id": 606, "name": "Esen Temel", "loan_amount": 35000, "duration_months": 12, "type": "debtor", "status": "active", "credit_score": 710, "start_date": "2026-04-26", "branch": "Adana"},
    {"id": 607, "name": "Ferhat Tutar", "loan_amount": 90000, "duration_months": 24, "type": "debtor", "status": "active", "credit_score": 735, "start_date": "2026-05-28", "branch": "Antalya"},
    {"id": 608, "name": "Gamze Gün", "loan_amount": 135000, "duration_months": 36, "type": "debtor", "status": "active", "credit_score": 805, "start_date": "2026-03-08", "branch": "Eskişehir"},
    {"id": 609, "name": "Hakan Aksoy", "loan_amount": 65000, "duration_months": 12, "type": "debtor", "status": "closed", "credit_score": 750, "start_date": "2025-11-28", "branch": "Adana"},
    {"id": 610, "name": "İlayda Hilal", "loan_amount": 350000, "duration_months": 60, "type": "debtor", "status": "active", "credit_score": 855, "start_date": "2026-01-18", "branch": "Antalya"},
    {"id": 611, "name": "Kubilay Taş", "loan_amount": 25000, "duration_months": 6, "type": "debtor", "status": "active", "credit_score": 625, "start_date": "2026-07-08", "branch": "Eskişehir"},
    {"id": 612, "name": "Melis Yalçin", "loan_amount": 95000, "duration_months": 18, "type": "debtor", "status": "active", "credit_score": 720, "start_date": "2026-03-05", "branch": "Adana"},
    {"id": 613, "name": "Nihat Saka", "loan_amount": 55000, "duration_months": 12, "type": "debtor", "status": "active", "credit_score": 760, "start_date": "2026-07-20", "branch": "Antalya"},
    {"id": 614, "name": "Oya Karaca", "loan_amount": 150000, "duration_months": 24, "type": "debtor", "status": "active", "credit_score": 695, "start_date": "2026-03-28", "branch": "Eskişehir"},
    {"id": 615, "name": "Ömer Yaman", "loan_amount": 80000, "duration_months": 12, "type": "debtor", "status": "active", "credit_score": 685, "start_date": "2026-05-15", "branch": "Adana"},
    {"id": 616, "name": "Pelin Soylu", "loan_amount": 260000, "duration_months": 36, "type": "debtor", "status": "defaulted", "credit_score": 415, "start_date": "2026-01-29", "branch": "Antalya"},
    {"id": 617, "name": "Sabri Tunç", "loan_amount": 45000, "duration_months": 10, "type": "debtor", "status": "active", "credit_score": 740, "start_date": "2026-08-18", "branch": "Eskişehir"},
    {"id": 618, "name": "Sena Seçkin", "loan_amount": 125000, "duration_months": 24, "type": "debtor", "status": "active", "credit_score": 790, "start_date": "2026-06-05", "branch": "Adana"},
    {"id": 619, "name": "Tolga İleri", "loan_amount": 85000, "duration_months": 15, "type": "debtor", "status": "active", "credit_score": 710, "start_date": "2026-09-25", "branch": "Antalya"},
    {"id": 620, "name": "Uğur Bulut", "loan_amount": 185000, "duration_months": 36, "type": "debtor", "status": "active", "credit_score": 830, "start_date": "2026-02-28", "branch": "Eskişehir"},
    {"id": 621, "name": "Vildan Yener", "loan_amount": 42000, "duration_months": 8, "type": "debtor", "status": "closed", "credit_score": 660, "start_date": "2025-10-31", "branch": "Adana"},
]