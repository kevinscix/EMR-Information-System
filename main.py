def main(fileName):
    patients = readPatientsFromFile(fileName)
    print("Welcome to the Health Information System\n\n")
    print("1. Display all patient data")
    print("2. Display patient data by ID")
    print("3. Add patient data")
    print("4. Display patient statistics")
    print("5. Find visits by year, month, or both")
    print("6. Find patients who need follow-up")
    print("7. Delete all visits of a particular patient")
    print("8. Quit\n")
    choice = input("Enter your choice (1-8):")
    if int(choice) == 1:
        displayPatientData(patients, 0)
    if int(choice) == 2:
        patientChoice = int(input("Enter patient ID:"))
        displayPatientData(patients, patientChoice)
    if int(choice) == 3:
        patientId = int(input("Enter patient ID:"))
        date = input("Enter date (YYYY-MM-DD):")
        temp = float(input("Enter temperature (Celcius):"))
        hr = float(input("Enter heart rate (bpm):"))
        rr = float(input("Enter respiratory rate (breaths per minute):"))
        sbp = float(input("Enter systolic blood pressure (mmHg):"))
        dbp = float(input("Enter diastolic blood pressure (mmHg):"))
        spo2 = float(input("Enter oxygen saturation (%):"))

        dateList = date.split("-")
        if len(dateList[0]) != 4 or len(dateList[1]) != 2 or  len(dateList[2]) != 2:
            print("Invalid date format. Please enter date in the format ‘yyyy-mm-dd’.")
            main(fileName)
        if  (int(dateList[1]) > 12 or 0 > int(dateList[1])) or (int(dateList[2]) > 31 or 0 > int(dateList[2])):
            print("Invalid date. Please enter a valid date.")
            main(fileName)
        if temp > 42 or temp < 35:
            print("Invalid temperature. Please enter a temperature between 35.0 and 42.0 Celsius.\n\n")
            main(fileName)
        if hr > 180 or hr < 30:
            print("Invalid heart rate. Please enter a heart rate between 30 and 180 bpm.\n\n")
            main(fileName)
        if rr > 40 or rr < 5:
            print("Invalid respiratory rate. Please enter a respiratory rate between 5 and 40 bpm.\n\n")
            main(fileName)
        if sbp > 200 or sbp < 70:
            print("Invalid systolic blood pressure. Please enter a systolic blood pressure between 70 and 200 mmHg.\n\n")
            main(fileName)
        if dbp > 120 or dbp < 40:
            print("Invalid diastolic blood pressure. Please enter a diastolic blood pressure between 40 and 120 mmHg.\n\n")
            main(fileName)
        if spo2 > 100 or spo2 < 70:
            print("Invalid oxygen saturation. Please enter an oxygen saturation between 70 and 100%.\n\n")
            main(fileName)
        addPatientData(patients, patientId, date, temp, hr, rr, sbp, dbp, spo2, fileName)

    if int(choice) == 4:
        patientChoice = float(input("Enter patient ID (or '0' for all patients):"))
        displayStats(patients, patientChoice)

    if int(choice) == 5:
        year = int(input("Enter year (YYYY) (or 0 for all years):"))
        month = int(input("Enter month (MM) (or 0 for all months):"))
        findVisitsByDate(patients, year, month)

    if int(choice) == 6:
        followUpList = findPatientsWhoNeedFollowUp(patients)
        print("Patients who need follow-up visits:")
        for i in range(len(followUpList)):
            if i < len(followUpList) - 1:
                print(followUpList[i], end=", ")
            else:
                print(followUpList[i])
        main("patients.txt")

    if int(choice) == 7:
        patientId = int(input("Enter Patient ID:"))
        deleteAllVisitsOfPatient(patients, patientId, fileName)
        main("patients.txt")



def readPatientsFromFile(fileName):
    f = open(fileName, 'r')
    patients = {}
    for line in f.readlines():
        line = line.strip()
        if line != "":
            parts = line.split(',')
            cleanParts = [part.strip() for part in parts]
            data = cleanParts[1:]
            patientID = cleanParts[0]
            if patientID not in patients:
                patients[patientID] = []
            patients[patientID].append(data)
    return patients

def displayPatientData(patients, patientId):
    if patientId == 0:
        for patient in patients:
            print("Patient ID: " + patient)
            for visit in patients[patient]:
                print(" Visit Date:", visit[0])
                print("  Temperature:", "%.2f" % float(visit[1]), "C")
                print("  Heart Rate:", "%d" % float(visit[2]), "bpm")
                print("  Respiratory Rate:", "%d" % float(visit[3]), "bpm")
                print("  Systolic Blood Pressure:", "%d" % float(visit[4]), "mmHg")
                print("  Diastolic Blood Pressure:", "%d" % float(visit[5]), "mmHg")
                print("  Oxygen Saturation:", "%d" % float(visit[6]), "%")
    if patientId >= 1:
        for patient in patients:
            if patientId == int(patient):
                print("Patient ID: " + patient)
                for visit in patients[patient]:
                    print(" Visit Date:", visit[0])
                    print("  Temperature:", "%.2f" % float(visit[1]), "C")
                    print("  Heart Rate:", "%d" % int(visit[2]), "bpm")
                    print("  Respiratory Rate:", "%d" % int(visit[3]), "bpm")
                    print("  Systolic Blood Pressure:", "%d" % int(visit[4]), "mmHg")
                    print("  Diastolic Blood Pressure:", "%d" % int(visit[5]), "mmHg")
                    print("  Oxygen Saturation:", "%d" % int(visit[6]), "%")
    if patientId not in patients and patientId != 0:
        print("Patient with ID", "%d not found.\n\n" % int(patientId))
    main("patients.txt")

def displayStats(patients, patientId):
    if patientId == 0:
        print("Vital Signs for All Patients:")
        temp_sum = 0
        heartrate_sum = 0
        respiratoryrate_sum = 0
        systolicbloodpressure_sum = 0
        diastolicbloodpressure_sum = 0
        oxygensaturation_sum = 0
        num_visits = 0
        for patient in patients:
            for visit in patients[patient]:
                temp_sum += float(visit[1])
                heartrate_sum += float(visit[2])
                respiratoryrate_sum += float(visit[3])
                systolicbloodpressure_sum += float(visit[4])
                diastolicbloodpressure_sum += float(visit[5])
                oxygensaturation_sum += float(visit[6])
                num_visits += 1
        print(" Average temperature:", "%.2f" % float(temp_sum / num_visits), "C")
        print(" Average heart rate:", "%.2f" % float(heartrate_sum / num_visits), "bpm")
        print(" Average respiratory rate:", "%.2f" % float(respiratoryrate_sum / num_visits), "bpm")
        print(" Average systolic blood pressure:", "%.2f" % float(systolicbloodpressure_sum / num_visits), "mmHg")
        print(" Average diastolic blood pressure:", "%.2f" % float(diastolicbloodpressure_sum / num_visits), "mmHg")
        print(" Average oxygen saturation:", "%.2f" % int(oxygensaturation_sum / num_visits), "%")
    if int(patientId) >= 1:
        print("Vital Signs for Patient", "%d:" % int(patientId))
        temp_sum = 0
        heartrate_sum = 0
        respiratoryrate_sum = 0
        systolicbloodpressure_sum = 0
        diastolicbloodpressure_sum = 0
        oxygensaturation_sum = 0
        num_visits = 0
        for patient in patients:
            if patientId == int(patient):
                for visit in patients[patient]:
                        temp_sum += float(visit[1])
                        heartrate_sum += float(visit[2])
                        respiratoryrate_sum += float(visit[3])
                        systolicbloodpressure_sum += float(visit[4])
                        diastolicbloodpressure_sum += float(visit[5])
                        oxygensaturation_sum += float(visit[6])
                        num_visits += 1
                print(" Average temperature:", "%.2f" % float(temp_sum / num_visits), "C")
                print(" Average heart rate:", "%.2f" % float(heartrate_sum / num_visits), "bpm")
                print(" Average respiratory rate:", "%.2f" % float(respiratoryrate_sum / num_visits), "bpm")
                print(" Average systolic blood pressure:", "%.2f" % float(systolicbloodpressure_sum / num_visits), "mmHg")
                print(" Average diastolic blood pressure:", "%.2f" % float(diastolicbloodpressure_sum / num_visits), "mmHg")
                print(" Average oxygen saturation:", "%.2f" % float(oxygensaturation_sum / num_visits), "%")
    if patientId not in patients:
        print("No data found for patient with ID", "%d." % int(patientId))
    main("patients.txt")

def addPatientData(patients, patientId, date, temp, hr, rr, sbp, dbp, spo2, fileName):
    list = [patientId, date, temp, hr, rr, sbp, dbp, spo2]
    if patientId in patients:
        for patient in patients:
            if int(patient) == patientId:
                patients[patient].append(list)

    tempString = str(patientId) + "," + str(date) + "," + str(temp) + "," + str(hr) + "," + str(rr) + "," + str(sbp) \
                 + "," + str(dbp) + "," + str(spo2)
    file = open(fileName, 'a')
    file.write("\n" + tempString)
    print("Visit saved for Patient #", "%d" % int(patientId))
    main("patients.txt")

def findVisitsByDate(patients, year, month):
    invalid = False
    previous = True
    for patient in patients:
        for visit in patients[patient]:
            if (year == 0 and month == 0) or (year == 0 and month != 0):
                print("Patient ID: " + patient)
                print(" Visit Date:", visit[0])
                print("  Temperature:", "%.2f" % float(visit[1]), "C")
                print("  Heart Rate:", "%d" % float(visit[2]), "bpm")
                print("  Respiratory Rate:", "%d" % float(visit[3]), "bpm")
                print("  Systolic Blood Pressure:", "%d" % float(visit[4]), "mmHg")
                print("  Diastolic Blood Pressure:", "%d" % float(visit[5]), "mmHg")
                print("  Oxygen Saturation:", "%d" % float(visit[6]), "%")
            elif year != 0 and month == 0:
                if year == int(visit[0][0:4]):
                    print("Patient ID: " + patient)
                    print(" Visit Date:", visit[0])
                    print("  Temperature:", "%.2f" % float(visit[1]), "C")
                    print("  Heart Rate:", "%d" % float(visit[2]), "bpm")
                    print("  Respiratory Rate:", "%d" % float(visit[3]), "bpm")
                    print("  Systolic Blood Pressure:", "%d" % float(visit[4]), "mmHg")
                    print("  Diastolic Blood Pressure:", "%d" % float(visit[5]), "mmHg")
                    print("  Oxygen Saturation:", "%d" % float(visit[6]), "%")
                else:
                    invalid = True
            elif year != 0 and month != 0:
                if year == int(visit[0][0:4]):
                    if month == int(visit[0][5:7]):
                        print("Patient ID: " + patient)
                        print(" Visit Date:", visit[0])
                        print("  Temperature:", "%.2f" % float(visit[1]), "C")
                        print("  Heart Rate:", "%d" % float(visit[2]), "bpm")
                        print("  Respiratory Rate:", "%d" % float(visit[3]), "bpm")
                        print("  Systolic Blood Pressure:", "%d" % float(visit[4]), "mmHg")
                        print("  Diastolic Blood Pressure:", "%d" % float(visit[5]), "mmHg")
                        print("  Oxygen Saturation:", "%d" % float(visit[6]), "%")
                        previous = True
                    else:
                        if not previous:
                            invalid = True
                else:
                    if not previous:
                        invalid = True
    if invalid:
        print("No visits found for the specified year/month.")
    main("patients.txt")

def findPatientsWhoNeedFollowUp(patients):
    followUpList = []
    for patient in patients:
        for visit in patients[patient]:
            if float(visit[2]) > 100 or float(visit[2]) < 60:
                if patient not in followUpList:
                    followUpList.append(patient)
            if float(visit[4]) > 140:
                if patient not in followUpList:
                    followUpList.append(patient)
            if float(visit[5]) > 90:
                if patient not in followUpList:
                    followUpList.append(patient)
            if float(visit[6]) < 90:
                if patient not in followUpList:
                    followUpList.append(patient)
    return followUpList

def deleteAllVisitsOfPatient(patients, patientId, fileName):
    file = open(fileName, 'w')
    for patient in patients:
        if int(patient) != patientId:
            for visit in patients[patient]:
                keep = str(patient) + "," + str(visit[0]) + "," + str(visit[1]) + "," + str(visit[2]) + "," + str(visit[3]) + "," + str(visit[4]) + "," + str(visit[5]) + "," + str(visit[6]) + "\n"
                file.writelines(keep)
                print("Data for patient", "%d" % int(patientId), "has been deleted.\n\n")
        if patientId not in patients[patient]:
            print("No data found for patient with ID", "%d" % int(patientId))

    file.close()




main("patients.txt")
