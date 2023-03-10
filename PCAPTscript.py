input("This script will alter every MapXXX.json file it finds. BACKUP YOUR FILES IF YOU'RE NOT ON STEAM! \n\nPress ENTER to continue...")

import json

files_found = False

# "{:03d}".format(29) === 029

for map_number in range(200):
    file = "Map" + "{:03d}".format(map_number) + ".json"
    try:
        with open (file, "r+") as json_file:
            data = json.load(json_file)
            files_found = True
            for event in data["events"]:
                if event == None:
                    pass
                elif event["name"] == "party_talk":
                    # so far every Event has a "name" key and value
                    for pages in event["pages"]:
                        for page_list in pages["list"]:
                            if len(page_list["parameters"]) == 3 and page_list["parameters"][0] == 0:
                                # these are the checks for the conditions in which a certain Party Talk dialogue per character will play or not. The ones I'm changing all have 3 values in their parameter list so it's the way to narrow them down. And also the ones I want to change always have the "0" as the first value.
                                parameter = page_list["parameters"]

                                match parameter[1]:
                                    # Marina
                                    case 242: 
                                        parameter[1] = 3
                                    
                                    # Daan
                                    case 243:
                                        parameter[1] = 4
                                    
                                    # Abella
                                    case 244:
                                        parameter[1] = 5

                                    # Levi
                                    case 246:
                                        parameter[1] = 1

                                    # Osaa
                                    case 2401:
                                        parameter[1] = 6

                                    # Olivia
                                    case 2402:
                                        parameter[1] = 15

                                    # Marcoh
                                    case 2403:
                                        parameter[1] = 13

                                    # Karin
                                    case 2404:
                                        parameter[1] = 14

                                    # Tanaka
                                    case 2405:
                                        parameter[1] = 35

                                    # Samarie ? Her case code could be wrong
                                    case 2406:
                                        parameter[1] = 36
                                    
                                    # August
                                    case 2407:
                                        parameter[1] = 31

                                    # Caligura
                                    case 2408:
                                        parameter[1] = 32

                                    # Henryk
                                    case 2409:
                                        parameter[1] = 33

                                    # Pav
                                    case 2410:
                                        parameter[1] = 34

                                    # Unaccounted for code
                                    case _:
                                        continue
                                        # I'm taking into account that there might be other events in here that do have 0 as the first value but that do not pertain to any character being THE player character. So I'm skipping the whole parameter.

                                parameter[0] = 4
                                # Always to 4 because in Termina's RPGMaker MV to check for a character's presence in the party makes this first item in parameter always a 4. The default 0 is to check whether they are THE player character.

                                parameter[2] = 0
                                # Always to 0 because it needs to be TRUE that this character is in your party. ALSO 0 is True and 1 is False in RPGMaker MV. ye idk
                                
                                # print(parameter)
                    print("Map"+"{:03d}".format(map_number)+" updated")
                    break
                    # break here is important because there is no other "party_talk" in the map json so this will prevent from it running through every other event in the file.
            json_file.seek(0)
            json.dump(data, json_file)
            json_file.truncate()
            # https://stackoverflow.com/questions/13949637/how-to-update-json-file-with-python
    except:
        print('error in trying to read file Map'+"{:03d}".format(map_number))
        continue

if files_found is True:
    input("All maps have been modded. Press ENTER to close this.")
else:
    input("NO MAP FILES WERE FOUND! Make sure this is in the correct folder. Check the GUIDE again if you're unsure!")

# Note: If at some point the game checks for conditions for a Party Talk dialogue that is anything other than a character being present - for example: Item in inventory, event witnessed, a character has died, x amount of soul stones, etc - then this script will NOT change anything pertaining to it, HOPEFULLY, and should still work regardless.