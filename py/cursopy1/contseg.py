segundosTot = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = segundosTot // 86400 
segsrestantes = segundosTot % 86400  
horas = segsrestantes // 3600  
segsrestantess = segsrestantes % 3600  
minrestantes = segsrestantess // 60  
segs = segsrestantess % 60  



print(dias,"dias,", horas,"horas,", minrestantes, "minutos", "e", segs,"segundos.")