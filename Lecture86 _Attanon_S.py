import csv

with open('Lecture86_Attanon_S.csv', 'w', newline='') as file:
    writer = csv.writer(file)
     
    writer.writerow(["Name", "Movie", "Pet"])
    writer.writerow(["Jame", "Docter Strange", "Dog"])
    writer.writerow(["Lily", "Infinity War", "Cat"])
    writer.writerow(["Mike", "John Wick", "Bird"])
    writer.writerow(["Luna", "The Hulk", "Rabbit"])
    writer.writerow(["Max", "My little Mermaid", "Squirrel"])