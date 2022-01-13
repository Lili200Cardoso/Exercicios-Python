brasileirao = ("Atletico MG","Palmeiras","Flamengo","Fortaleza","Bragantino",
               "Corinthias","Fluminense","Cuiabá",
               "Internacional","Atletico GO","Athletico PR","Ceará SC","Santos","Juventude","Bahia",
               "São Paulo","América MG","Gremio","Sport Recife","Chapecoense")
print("-=" * 40)
print(f"Lista de Times do Brasileirão{brasileirao}")
print("-=" * 40)
print(f"Os 5 primeiros são {brasileirao[0:5]}")
print("-=" * 40)
print(f"Os últimos 4 são {brasileirao[-4:]}")
print("-=" * 40)
print(f"Times em ordem alfabetica {sorted(brasileirao)}")
print("-=" * 40)
print(f"O Chapecoense está na {brasileirao.index('Chapecoense')+1}ª posição")
print("-=" * 40)
