import json

quiz_data = [{
        "quiz_id": 1,
        "quiz_name": "Patung Liberty merupakan hadiah dari negara ____ ke AS?",
        "correct_answer" : "Prancis",
        "quiz_answers": ["Polandia", "Prancis", "Belanda"]
    },
    {
        "quiz_id": 2,
        "quiz_name": "Apa nama perusahaan teknologi terbesar di Korea Selatan?",
        "correct_answer" : "LG Electronics",
        "quiz_answers": ["SK Hynix", "Samsung Electronics", "LG Electronics"]
    },
    {
        "quiz_id": 3,
        "quiz_name": "Logam apa yang ditemukan oleh Hans Christian Oersted pada tahun 1825?",
        "correct_answer" : "Aluminium",
        "quiz_answers": ["Aluminium", "Emas", "Tembaga"]
    },
    {
        "quiz_id": 4,
        "quiz_name": "Apa nama kapal yang membawa Charles Darwin dalam perjalanannya yang terkenal di Galapagos?",
        "correct_answer" : "HMS Beagle",
        "quiz_answers": ["HMS Bounty", "HMS Beagle", "HMS Endeavour"]
    },
    {
        "quiz_id": 5,
        "quiz_name": "Di mana letak Great Barrier Reef, sebuah kawasan karang terbesar di dunia?",
        "correct_answer" : "Australia",
        "quiz_answers": ["Australia", "Brasil", "Meksiko"]
    },
    {
        "quiz_id": 6,
        "quiz_name": "Siapa pendiri dan pemimpin pertama Republik Rakyat Tiongkok?",
        "correct_answer" : "Mao Zedong",
        "quiz_answers": ["Mao Zedong", "Deng Xiaoping", "Sun Yat-sen"]
    },   
    {
        "quiz_id": 7,
        "quiz_name": "Apa nama teknologi yang memungkinkan kita untuk membuat percakapan antara manusia dan mesin terdengar lebih alami?",
        "correct_answer" : "Natural Language Processing",
        "quiz_answers": ["Natural Language Processing", "Speech Synthesis", "Voice Assistant"]
    },      
    {
        "quiz_id": 8,
        "quiz_name": "Apa ibu kota Laos?",
        "correct_answer" : "Vientiane",
        "quiz_answers": ["Luang Prabang", "Savannakhet", "Vientiane"]
    },   
    {
        "quiz_id": 9,
        "quiz_name": "Apa ibu kota Mongolia?",
        "correct_answer" : "Mao Zedong",
        "quiz_answers": ["Ulaanbaatar", "Darkhan", "Erdenet"]
    },      
    {
        "quiz_id": 10,
        "quiz_name": "Apa ibu kota Kazakhstan?",
        "correct_answer" : "Astana",
        "quiz_answers": ["Nur-Sultan", "Almaty", "Astana"]
    },   
    ]

with open('quiz_data.json', 'w') as f:
    json.dump(quiz_data, f)
