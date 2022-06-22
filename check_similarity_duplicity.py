from difflib import SequenceMatcher


def check_similarity(data):
    similarity_threshold = 0.8
    result = []
    for i in data.index:
        h = data.loc[i, 'hash']
        if h != 'failed hashing':
            similars = []
            for j in data.index:
                if i != j:
                    try:
                        r = SequenceMatcher(None, data.loc[i, 'hash'], data.loc[j, 'hash']).ratio()
                    except:
                        pass
                    if r > similarity_threshold:
                        similars.append('-'.join([str(r), data.loc[j, 'file']]))

            if len(similars) > 0:
                data.loc[i, 'similar_images'] = ','.join(similars)
    return data
