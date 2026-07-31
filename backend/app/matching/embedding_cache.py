import pickle
import os


CACHE_FILE = "embedding_cache.pkl"



def load_cache():

    if os.path.exists(CACHE_FILE):

        with open(
            CACHE_FILE,
            "rb"
        ) as f:

            return pickle.load(f)


    return {}



embedding_cache = load_cache()



def save_cache():

    with open(
        CACHE_FILE,
        "wb"
    ) as f:

        pickle.dump(
            embedding_cache,
            f
        )