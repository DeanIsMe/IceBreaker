# definitions.py
IbConfig = {
    'telepotChatId': '572145851',
    'googleServiceKeyFile' : 'GoogleCloudServiceKey.json',
    'telepotToken' : '679545486:AAEbCBdedlJ1lxFXpN1a-J-6LfgFQ4cAp04',
    'startMessage' : 'Hallo, ich bin unsere dolmetschende Eule. Stelle mich bitte auf deine Handflaeche und ich sage dir, was dein tauber Gegenueber schreibt. Wenn du etwas sagst, teile ich das deinem Gegenueber mit',
    'listenLanguage' : 'de_DE', # de_DE, en_US, en_UK, en_AU, etc. See https://cloud.google.com/speech-to-text/docs/languages
    'speakLanguage' : 'de', # de, en_US, en_UK, en_AU. See gtts-cli --all
    'micDeviceIndex' : 0,
}

