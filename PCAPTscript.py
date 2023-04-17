import json
import multiprocessing
import os
import time

CHARACTER_PARAMETER_MAP = {
    242: 3,  # Marina
    243: 4,  # Daan
    244: 5,  # Abella
    246: 1,  # Levi
    2401: 6,  # Osaa
    2402: 15,  # Olivia
    2403: 13,  # Marcoh
    2404: 14,  # Karin
    2405: 35,  # Tanaka
    2406: 36,  # Samarie
    2407: 31,  # August
    2408: 32,  # Caligura
    2409: 33,  # Henryk
    2410: 34,  # Pav
}

def update_map(map_number):
    file = f"Map{map_number:03d}.json"
    try:
        with open(file, "r+") as json_file:
            data = json.load(json_file)
            for event in data["events"]:
                if event is None:
                    pass
                elif event["name"] == "party_talk":
                    for pages in event["pages"]:
                        for page_list in pages["list"]:
                            if (
                                len(page_list["parameters"]) == 3
                                and page_list["parameters"][0] == 0
                            ):
                                parameter = page_list["parameters"]
                                if parameter[1] in CHARACTER_PARAMETER_MAP:
                                    parameter[1] = CHARACTER_PARAMETER_MAP[
                                        parameter[1]
                                    ]
                                    parameter[0] = 4
                                    parameter[2] = 0

                    json_file.seek(0)
                    json.dump(data, json_file)
                    json_file.truncate()
                    return True
    except:
        pass

    return False


if __name__ == "__main__":
    print("This script will alter every MapXXX.json file it finds. BACKUP YOUR FILES IF YOU'RE NOT ON STEAM!")
    input("Press ENTER to continue...")

    start_time = time.perf_counter()

    pool = multiprocessing.Pool(processes=os.cpu_count())

    map_numbers = range(200)
    results = pool.map(update_map, map_numbers)
    completed = any(results)

    if completed:
        input("All maps have been modded. Press ENTER to close this.")
    else:
        input("NO MAP FILES WERE FOUND! Make sure this is in the correct folder. Check the GUIDE again if you're unsure!")

    pool.close()
    pool.join()

    end_time = time.perf_counter()
    print(f"Total time taken: {end_time - start_time:.6f} seconds")
