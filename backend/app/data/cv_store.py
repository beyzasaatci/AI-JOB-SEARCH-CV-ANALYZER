cv_store = {}


def save_cv(file_id, text):

    cv_store[file_id] = text



def get_cv(file_id):

    return cv_store.get(file_id)