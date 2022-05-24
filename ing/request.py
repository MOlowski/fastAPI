import requests
import json



def result_parse(result,Name,payload,matched):
    urls_num = 0
    is_url = False
    for source_num in range((len(result['sources']))):
        source = 'source{}'.format(source_num+1)
        if len(result['sources'][source]['urls']) > 0:
            urls_num += result['sources'][source]['quantity']
            is_url = True
    if is_url:
        alcohol = {
            "alcohol_id": payload['required'][0]['keyword'],
            "payload" : payload,
            "urls_num": urls_num
        }
        matched += 1
        with open("results.json","r+") as f:
            f_data = json.load(f)
            f_data["alcohol"].append(alcohol)
            f.seek(0)
            json.dump(f_data, f, indent = 4)

    return matched


def request(Brand, Name, category, URL, headers, optional_threshhold):
    matched_result = 0
    with open("results.json","w") as f:
        initalize = {
            "alcohol": []
        }
        json.dump(initalize,f)


    for i in range(len(Brand)):
        if len(Name[i]) < 5:
            mode = "m"
        else:
            mode = "c"
        if i%10 == 0:
            print(i, Brand[i], category[i], Name[i], sep= ' ')
        payload = {
            "required": [
                {
                    "keyword": Brand[i],
                    "mode":"c"
                },     
            ],
            "optional": [
                {
                    "keyword": category[i],
                    "mode":"c"
                },
                {
                    "keyword": Name[i],
                    "mode":mode
                },
                {
                    "keyword": 'vodka',
                    "mode":"c"
                },
                {
                    "keyword": "beer",
                    "mode":"c"
                },
                {
                    "keyword": "wine",
                    "mode":"c"
                },
                {
                    "keyword": "cider",
                    "mode":"c"
                },
                {
                    "keyword": "mead",
                    "mode":"c"
                },
                {
                    "keyword": "sake",
                    "mode":"c"
                },
                {
                    "keyword": "brandy",
                    "mode":"c"
                },
                {
                    "keyword": "gin",
                    "mode":"c"
                },
                {
                    "keyword": "whiskey",
                    "mode":"c"
                },
                {
                    "keyword": "rum",
                    "mode":"c"
                },
                {
                    "keyword": "tequila",
                    "mode":"c"
                },
                {
                    "keyword": "absinthe",
                    "mode":"c"
                },
                {
                    "keyword": "liquor",
                    "mode":"c"
                },                                                                                                                     
            ],                                                                                                                  
            "optionalThreshold": optional_threshhold
        }

        response = requests.post(
            URL,
            data = json.dumps(payload),
            headers = headers,
        )

        matched_result = result_parse(response.json(), Name, payload, matched_result)

    return f"number of matched alcohols: {matched_result}"
    