import shelve

save_path = ''
username = ''


def setSavePath(path='files'):

    global save_path
    save_path = path


def setUserName(name='Anonymous'):

    global username
    username = name


def savePreferences():

    config = shelve.open('preferences')
    config['username'] = username
    config['save_path'] = save_path
