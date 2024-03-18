studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"]
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend", "Data Analyst", "Backend"]

#Aggiungere i corsi di Grace e Henry
corsi.append("Frontend")
corsi.append("Cybersecurity")
if len(studenti) == len(corsi):
    print(corsi)