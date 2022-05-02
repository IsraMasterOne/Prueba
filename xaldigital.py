"""Programa Creado para la Prueba Tecnica
de XalDigital por Israel Fuentes Saavedra
Fecha: 02/06/2022"""

import requests
import json
from collections import Counter
import msvcrt
import os


def menu():
	print ("Selecciona una opción")
	print ("\t1 - Numero de Respuestas contestadas y no contestadas")
	print ("\t2 - ID Respuesta con menor número de vistas")
	print ("\t3 - ID Respuesta mas vieja y mas actual")
	print ("\t4 - ID Respuesta del owner con mayor reputacion")
	print ("\t5 - Salir")


if __name__=='__main__':
	os.system("cls")	 
	print("\t\tPrograma hecho por Israel Fuentes Saavedra\n\n")
	print("\t\tPresione una tecla para continuar...")
	msvcrt.getch()

	while True:
		os.system("cls")	 
		url="https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow"

		response=requests.get(url)
		if response.status_code == 200:
			print('Exitosamente conectado')
		elif response.status_code == 404:
			print('Not Found!')
			print("Favor de verificar que el url este correcto")
			exit()

		response=response.json()	

		accepted_answerid=[dict(response['items'][i])['accepted_answer_id'] if 'accepted_answer_id' in dict(response['items'][i]).keys() else 'Not_answer' for i in range(len(response['items']))]

		menu()
		opcion = input("\n\t\t--->     ")

		if opcion=="1":
			os.system("cls")

			answered= Counter([dict(response['items'][i])['is_answered'] for i in range(len(response['items']))])
			print("Respondidas\t\t"+str(dict(answered.items())[1]))	
			print("No Respondidas\t\t"+str(dict(answered.items())[0]))	

			print("\t\tPresione una tecla para continuar...")
			msvcrt.getch()
		
		elif opcion=="2":
			os.system("cls")
			view_count = [dict(response['items'][i])['view_count'] for i in range(len(response['items']))]
			vc_id=accepted_answerid[view_count.index(min(view_count))]
			print("ID Respuesta con menor numero de visitas: "+str(vc_id))
			print("\t\tPresione una tecla para continuar...")
			msvcrt.getch()
		
		elif opcion=="3":
			os.system("cls")
			date=[dict(response['items'][i])['creation_date'] for i in range(len(response['items']))]				
			new_date=accepted_answerid[date.index(min(date))]
			old_date=accepted_answerid[date.index(max(date))]
			print("ID Respuesta mas vieja: "+str(old_date))
			print("ID Respuesta mas actual: "+str(new_date))
			print("\t\tPresione una tecla para continuar...")
			msvcrt.getch()
		
		elif opcion=='4':
			os.system("cls")
			rep=[int(dict(response['items'][i])['owner']['reputation']) if dict(response['items'][i])['owner']['user_type']!='does_not_exist' else 0 for i in range(len(response['items']))]
			idrep=accepted_answerid[rep.index(max(rep))]
			print("ID Respuesta del owner con mayor reputacion: "+str(idrep))
			print("\t\tPresione una tecla para continuar...")
			msvcrt.getch()	
		elif opcion=='5':
			os.system("cls")
			exit()



		