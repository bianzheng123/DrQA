import jsonlines


def run(username: str, dataset: str):
    raw_data_path = f'/home/{username}/Dataset/vector-set-similarity-search/RawData/{dataset}/document/collection.tsv'
    json_l = []
    with open(raw_data_path, 'r') as f:
        for line in f:
            if line == '':
                continue
            txt_l = line.split('\t')
            doc_id = txt_l[0]
            doc_text = txt_l[1]
            json_l.append({"id": doc_id, "text": doc_text})

    doc_json_name = f'/home/{username}/DrQA/data/raw_data/{dataset}.jsonl'

    with jsonlines.open(doc_json_name, 'w') as writer:
        writer.write_all(json_l)
    print(f"complete the json write file")


if __name__ == '__main__':
    config_m = {
        'db': {
            'username': 'zhengbian',
            'dataset': 'wikipedia-500',
        },
        'local': {
            'username': 'bianzheng',
            'dataset': 'wikipedia-500',
        },
    }
    config_name = 'local'
    config = config_m[config_name]

    username = config['username']
    dataset = config['dataset']
    run(username, dataset)
