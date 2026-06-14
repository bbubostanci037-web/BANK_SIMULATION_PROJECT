

BANK_DATA = {
    "starting_capital": 4200000,      
    "loan_interest_rate": 0.16,        
    "investment_interest_rate": 0.08    
}




INVESTORS = [
    {"id": 701, "name": "Gökhan Tekin", "deposit_amount": 580000, "duration_months": 12, "type": "investor", "status": "active", "credit_score": 815, "start_date": "2026-04-01", "branch": "Samsun"},
    {"id": 702, "name": "Bahar Yildiz", "deposit_amount": 420000, "duration_months": 24, "type": "investor", "status": "active", "credit_score": 730, "start_date": "2026-05-12", "branch": "Denizli"},
    {"id": 703, "name": "Cem Şen", "deposit_amount": 180000, "duration_months": 6, "type": "investor", "status": "closed", "credit_score": 665, "start_date": "2026-01-20", "branch": "Erzurum"},
    {"id": 704, "name": "Derya Aksu", "deposit_amount": 910000, "duration_months": 36, "type": "investor", "status": "active", "credit_score": 865, "start_date": "2026-02-15", "branch": "Samsun"},
    {"id": 705, "name": "Engin Kurt", "deposit_amount": 230000, "duration_months": 12, "type": "investor", "status": "active", "credit_score": 725, "start_date": "2026-06-05", "branch": "Erzurum"},
    {"id": 706, "name": "Funda Kaya", "deposit_amount": 390000, "duration_months": 18, "type": "investor", "status": "active", "credit_score": 775, "start_date": "2026-03-22", "branch": "Denizli"},
    {"id": 707, "name": "Hakan Bulut", "deposit_amount": 670000, "duration_months": 12, "type": "investor", "status": "closed", "credit_score": 820, "start_date": "2026-02-10", "branch": "Samsun"},
    {"id": 708, "name": "Işil Demir", "deposit_amount": 95000, "duration_months": 12, "type": "investor", "status": "active", "credit_score": 645, "start_date": "2026-07-01", "branch": "Samsun"},
    {"id": 709, "name": "Kamil Öztürk", "deposit_amount": 1550000, "duration_months": 48, "type": "investor", "status": "active", "credit_score": 890, "start_date": "2026-01-12", "branch": "Erzurum"},
    {"id": 710, "name": "Lale Arslan", "deposit_amount": 780000, "duration_months": 24, "type": "investor", "status": "active", "credit_score": 795, "start_date": "2026-08-14", "branch": "Denizli"},
    {"id": 711, "name": "Murat Polat", "deposit_amount": 70000, "duration_months": 3, "type": "investor", "status": "closed", "credit_score": 610, "start_date": "2026-09-02", "branch": "Erzurum"},
    {"id": 712, "name": "Nalan Doğan", "deposit_amount": 310000, "duration_months": 12, "type": "investor", "status": "active", "credit_score": 750, "start_date": "2026-04-18", "branch": "Samsun"},
    {"id": 713, "name": "Onur Kiliç", "deposit_amount": 1050000, "duration_months": 36, "type": "investor", "status": "active", "credit_score": 845, "start_date": "2026-01-28", "branch": "Denizli"},
    {"id": 714, "name": "Pelin Yavuz", "deposit_amount": 290000, "duration_months": 18, "type": "investor", "status": "active", "credit_score": 760, "start_date": "2026-10-05", "branch": "Erzurum"},
    {"id": 715, "name": "Ramazan Şahin", "deposit_amount": 460000, "duration_months": 24, "type": "investor", "status": "active", "credit_score": 780, "start_date": "2026-05-20", "branch": "Samsun"},
    {"id": 716, "name": "Seda Uzun", "deposit_amount": 82000, "duration_months": 6, "type": "investor", "status": "closed", "credit_score": 635, "start_date": "2026-11-12", "branch": "Denizli"},
    {"id": 717, "name": "Tolga Erdem", "deposit_amount": 690000, "duration_months": 12, "type": "investor", "status": "active", "credit_score": 830, "start_date": "2026-06-15", "branch": "Erzurum"},
    {"id": 718, "name": "Umut Çetin", "deposit_amount": 510000, "duration_months": 24, "type": "investor", "status": "active", "credit_score": 740, "start_date": "2026-07-22", "branch": "Samsun"},
    {"id": 719, "name": "Vildan Aksoy", "deposit_amount": 195000, "duration_months": 12, "type": "investor", "status": "active", "credit_score": 710, "start_date": "2026-12-01", "branch": "Denizli"},
    {"id": 720, "name": "Yalçin Aydin", "deposit_amount": 860000, "duration_months": 36, "type": "investor", "status": "active", "credit_score": 825, "start_date": "2026-02-24", "branch": "Samsun"},
    {"id": 721, "name": "Zuhal Koç", "deposit_amount": 140000, "duration_months": 12, "type": "investor", "status": "closed", "credit_score": 670, "start_date": "2026-12-10", "branch": "Erzurum"},
    {"id": 722, "name": "Ahmet Şimşek", "deposit_amount": 1450000, "duration_months": 60, "type": "investor", "status": "active", "credit_score": 895, "start_date": "2026-01-04", "branch": "Samsun"},
    {"id": 723, "name": "Canan Altin", "deposit_amount": 340000, "duration_months": 18, "type": "investor", "status": "active", "credit_score": 755, "start_date": "2026-12-18", "branch": "Denizli"},
    {"id": 724, "name": "Deniz Sönmez", "deposit_amount": 400000, "duration_months": 24, "type": "investor", "status": "active", "credit_score": 785, "start_date": "2026-05-11", "branch": "Erzurum"},
    {"id": 725, "name": "Ferit Akin", "deposit_amount": 950000, "duration_months": 12, "type": "investor", "status": "active", "credit_score": 855, "start_date": "2026-03-19", "branch": "Samsun"}
]




DEBTORS = [
    {"id": 801, "name": "Alper Korkmaz", "loan_amount": 75000, "duration_months": 12, "type": "debtor", "status": "active", "credit_score": 820, "start_date": "2026-01-22", "branch": "Samsun"},
    {"id": 802, "name": "Burcu Çelik", "loan_amount": 155000, "duration_months": 24, "type": "debtor", "status": "active", "credit_score": 725, "start_date": "2026-02-20", "branch": "Denizli"},
    {"id": 803, "name": "Cihan Güler", "loan_amount": 45000, "duration_months": 6, "type": "debtor", "status": "closed", "credit_score": 680, "start_date": "2025-12-12", "branch": "Erzurum"},
    {"id": 804, "name": "Damla Şen", "loan_amount": 110000, "duration_months": 18, "type": "debtor", "status": "active", "credit_score": 765, "start_date": "2026-04-10", "branch": "Samsun"},
    {"id": 805, "name": "Eray Özdemir", "loan_amount": 380000, "duration_months": 48, "type": "debtor", "status": "defaulted", "credit_score": 405, "start_date": "2026-01-25", "branch": "Erzurum"},
    {"id": 806, "name": "Filiz Temel", "loan_amount": 40000, "duration_months": 12, "type": "debtor", "status": "active", "credit_score": 705, "start_date": "2026-04-22", "branch": "Denizli"},
    {"id": 807, "name": "Gazi Tutar", "loan_amount": 95000, "duration_months": 24, "type": "debtor", "status": "active", "credit_score": 740, "start_date": "2026-05-20", "branch": "Samsun"},
    {"id": 808, "name": "Gizem Gün", "loan_amount": 125000, "duration_months": 36, "type": "debtor", "status": "active", "credit_score": 810, "start_date": "2026-03-10", "branch": "Erzurum"},
    {"id": 809, "name": "Halil Aksoy", "loan_amount": 60000, "duration_months": 12, "type": "debtor", "status": "closed", "credit_score": 735, "start_date": "2025-11-25", "branch": "Denizli"},
    {"id": 810, "name": "İpek Hilal", "loan_amount": 320000, "duration_months": 60, "type": "debtor", "status": "active", "credit_score": 845, "start_date": "2026-01-15", "branch": "Samsun"},
    {"id": 811, "name": "Kadir Taş", "loan_amount": 30000, "duration_months": 6, "type": "debtor", "status": "active", "credit_score": 615, "start_date": "2026-07-10", "branch": "Erzurum"},
    {"id": 812, "name": "Merve Yalçin", "loan_amount": 85000, "duration_months": 18, "type": "debtor", "status": "active", "credit_score": 730, "start_date": "2026-03-08", "branch": "Denizli"},
    {"id": 813, "name": "Nedim Saka", "loan_amount": 50000, "duration_months": 12, "type": "debtor", "status": "active", "credit_score": 755, "start_date": "2026-07-18", "branch": "Samsun"},
    {"id": 814, "name": "Oylum Karaca", "loan_amount": 140000, "duration_months": 24, "type": "debtor", "status": "active", "credit_score": 685, "start_date": "2026-03-26", "branch": "Erzurum"},
    {"id": 815, "name": "Özgür Yaman", "loan_amount": 75000, "duration_months": 12, "type": "debtor", "status": "active", "credit_score": 690, "start_date": "2026-05-12", "branch": "Denizli"},
    {"id": 816, "name": "Pinar Soylu", "loan_amount": 240000, "duration_months": 36, "type": "debtor", "status": "defaulted", "credit_score": 425, "start_date": "2026-01-28", "branch": "Samsun"},
    {"id": 817, "name": "Sait Tunç", "loan_amount": 40000, "duration_months": 10, "type": "debtor", "status": "active", "credit_score": 745, "start_date": "2026-08-15", "branch": "Erzurum"},
    {"id": 818, "name": "Sibel Seçkin", "loan_amount": 115000, "duration_months": 24, "type": "debtor", "status": "active", "credit_score": 775, "start_date": "2026-06-02", "branch": "Denizli"},
    {"id": 819, "name": "Tamer İleri", "loan_amount": 80000, "duration_months": 15, "type": "debtor", "status": "active", "credit_score": 715, "start_date": "2026-09-22", "branch": "Samsun"},
    {"id": 820, "name": "Ufuk Bulut", "loan_amount": 175000, "duration_months": 36, "type": "debtor", "status": "active", "credit_score": 825, "start_date": "2026-02-25", "branch": "Erzurum"},
    {"id": 821, "name": "Yonca Yener", "loan_amount": 35000, "duration_months": 8, "type": "debtor", "status": "closed", "credit_score": 665, "start_date": "2025-10-29", "branch": "Denizli"},
    {"id": 822, "name": "Yunus Kartal", "loan_amount": 65000, "duration_months": 12, "type": "debtor", "status": "active", "credit_score": 750, "start_date": "2026-11-12", "branch": "Samsun"},
    {"id": 823, "name": "Zahit Mert", "loan_amount": 90000, "duration_months": 18, "type": "debtor", "status": "active", "credit_score": 740, "start_date": "2026-05-06", "branch": "Erzurum"},
    {"id": 824, "name": "Zelal Topal", "loan_amount": 160000, "duration_months": 24, "type": "debtor", "status": "active", "credit_score": 780, "start_date": "2026-07-02", "branch": "Denizli"},
    {"id": 825, "name": "Hikmet Altin", "loan_amount": 52000, "duration_months": 12, "type": "debtor", "status": "active", "credit_score": 730, "start_date": "2026-11-22", "branch": "Samsun"}
]