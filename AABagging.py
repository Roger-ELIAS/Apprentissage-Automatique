#On va récupérer les prédicts depuis les 3 sources différentes : chi2, réseau
#de neurones, et Naive Bayes. 

#Les 3 arrays sont de même taille.

def personnalBagging(chi2Array, NWArray, NBArray) : 
	finalArray = [];
	for i in range(0, len(chi2Array)):
		count = 0;
		if chi2Array[i] == 1 :
			++count;
		if NWArray[i] == 1	:
			++count; 
		if NBArray[i] == 1 : 
			++count; 
		if count >= 2 : 
			finalArray.append(1)
		else
			finalArray.append(-1)

	return finalArray		
