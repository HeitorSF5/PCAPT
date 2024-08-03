input("This script will REVERT every MapXXX.json file that was altered by the PC Party Talk mod while ONLY reverting the Party Talk changes (hopefully...) \n\nPress ENTER to continue...")

import json

files_found = False

# "{:03d}".format(29) === 029

# This flag will let me skip one iteration of the parameters
for map_number in range(200):
    file = "Map" + "{:03d}".format(map_number) + ".json"
    try:
        with open (file, "r+", encoding="utf-8") as json_file:
            data = json.load(json_file)
            files_found = True
            alter_this = False
            for event in data["events"]:
                if event == None:
                    pass
                elif event["name"] == "party_talk":
                    for pages in event["pages"]:
                        for page_list in pages["list"]:
                            # page_list: { 'code': number, indent: number, parameters: [numbers...] }
                            # print("this page_list: ", page_list)
                            if len(page_list["parameters"]) == 3 and page_list["parameters"][0] == 4:
                              if alter_this:
                                parameter = page_list["parameters"]
                                match parameter[1]:
                                    # Marina
                                    case 3: 
                                        parameter[1] = 242
                                    
                                    # Daan
                                    case 4:
                                        parameter[1] = 243
                                    
                                    # Abella
                                    case 5:
                                        parameter[1] = 244

                                    # Levi
                                    case 1:
                                        parameter[1] = 246

                                    # Osaa
                                    case 6:
                                        parameter[1] = 2401

                                    # Olivia
                                    case 15:
                                        parameter[1] = 2402

                                    # Marcoh
                                    case 13:
                                        parameter[1] = 2403

                                    # Karin
                                    case 14:
                                        parameter[1] = 2404

                                    # Tanaka
                                    case 35:
                                        parameter[1] = 2405

                                    # Samarie ? Her case code could be wrong
                                    case 36:
                                        parameter[1] = 2406
                                    
                                    # August
                                    case 31:
                                        parameter[1] = 2407

                                    # Caligura
                                    case 32:
                                        parameter[1] = 2408

                                    # Henryk
                                    case 33:
                                        parameter[1] = 2409

                                    # Pav
                                    case 34:
                                        parameter[1] = 2410

                                    # OC Mods:

                                    # Maddalena
                                    case 9:
                                        parameter[1] = 375

                                    # Unaccounted for code
                                    case _:
                                        continue
                                        # I'm taking into account that there might be other events in here that do have 0 as the first value but that do not pertain to any character being THE player character. So I'm skipping the whole parameter.

                                parameter[0] = 0
                                # = 0 is the default -> Check if character is the PC
                                # = 4 is the new one -> Check if character is in the Party

                                parameter[2] = 1
                                # = 0 is the default -> Means "False"
                                # = 1 is the new one -> Means "True"
                                
                                alter_this = False
                              elif alter_this == False:
                                  alter_this = True
                            else:
                                alter_this = False
                                # so that it resets in case no dupe is found but went on to the next page_list. Only works if dupes are right next to each other (which they should be for now, at least)
                                
                    print("Map"+"{:03d}".format(map_number)+" updated")
                    break
                    # break here is important because there is no other "party_talk" in the map json so this will prevent from it running through every other event in the file.
            json_file.seek(0)
            json.dump(data, json_file)
            json_file.truncate()
            # https://stackoverflow.com/questions/13949637/how-to-update-json-file-with-python
    except Exception as e:
        print('could not find or read Map'+"{:03d}".format(map_number))
        # print(e)
        continue

if files_found is True:
    input("All maps have been modded. Press ENTER to close this.")
else:
    input("NO MAP FILES WERE FOUND! Make sure this is in the correct folder. Check the GUIDE again if you're unsure!")

# Note: If at some point the game checks for conditions for a Party Talk dialogue that is anything other than a character being present - for example: Item in inventory, event witnessed, a character has died, x amount of soul stones, etc - then this script will NOT change anything pertaining to it, HOPEFULLY, and should still work regardless.
