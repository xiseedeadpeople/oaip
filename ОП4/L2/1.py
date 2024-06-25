import json

def main():
    # Data for the JSON file
    data = {
        "data1": {
            "age": 17,
            "phone": "+7(914)355-01-97",
            "name": "Mary",
            "city": "Vladivostok"
        },
        "data2": {
            "age": 25,
            "phone": "+7(914)653-59-48",
            "name": "Aleksander",
            "city": "Yekaterinburg"
        },
        "data3": {
            "age": 14,
            "phone": "+7(914)302-00-66",
            "name": "Maria",
            "city": "Moscow"
        },
        "data4": {
            "age": 33,
            "phone": "+7(914)000-68-31",
            "name": "Olga",
            "city": "Belgorod"
        },
        "data5": {
            "age": 55,
            "phone": "+7(914)581-58-66",
            "name": "Egor",
            "city": "Moscow"
        }
    }


    name = 'people_data.json'
    with open(name, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    #

    with open(name, 'r') as json_file:
        data = json.load(json_file)

        msk_ppl = [[person["name"], person["age"]] for person in data.values() if person["city"] == "Moscow"]

        if msk_ppl:
            avg = []
            for i in msk_ppl:
                for lst in i:
                    avg.append(lst) if str(lst).isdigit() else 0
            avg_age = sum(avg) / len(msk_ppl)
        else:
            avg_age = 0

    print(msk_ppl, avg_age)

    
if __name__ == "__main__":
    main()
