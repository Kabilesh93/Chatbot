from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.knowledge
collection = db.tamil_chat

collection.insert_many((

    {
        "entity": "Address",
        "keywords": ["முகவரி", "விலாசம்"],
        "pattern": ""
    },
    {
        "entity": "Relocate",
        "keywords": ["இடமாற்று", "இடம்", "இடத்திற்கு"]
    },
    {
        "entity": "Agent",
        "keywords": ["முகவர்", "பிரதிநிதி", "இயக்குபவர்", "உதவியாளர்", "சிறப்பு"]
    },
    {
        "entity": "Customer Service",
        "keywords": ["வாடிக்கையாளர் சேவை"]
    },
    {
        "entity": "Xiaomi",
        "keywords": ["xiaomi", "xiao mi", "mi", "mi"]
    },
    {
        "entity": "Android",
        "keywords": ["android", "android", "google os", "andriod"]
    },
    {
        "entity": "Vivo",
        "keywords": ["vivo", "v9"]
    },
    {
        "entity": "Huawei",
        "keywords": ["address", "add", "address"]
    },
    {
        "entity": "Energizer",
        "keywords": ["energizer", "mobile energy", "energizer"]
    },
    {
        "entity": "Samsung",
        "keywords": ["samsung", "samsung", "galaxy", "s9", "note 8", "note"]
    },
    {
        "entity": "Infinity",
        "keywords": ["infinity", "sense", "blaze"]
    },
    {
        "entity": "Balance",
        "keywords": ["மீதி", "இருப்பு"]
    },
    {
        "entity": "What happened",
        "keywords": ["என்ன நடந்தது", "எங்கே"]
    },
    {
        "entity": "Only showing",
        "keywords": ["மட்டுமே காட்டுகிறது", "எங்கே"]
    },
    {
        "entity": "Missing",
        "keywords": ["காணவில்லை", "காட்டவில்லை", "தெரியவில்லை"]
    },
    {
        "entity": "Indonesia",
        "keywords": ["இந்தோனேஷியா", "ஜகார்த்தா", "மேதன்", "சுரபாய"]
    },
    {
        "entity": "Bangladesh",
        "keywords": ["வங்காளம்", "டாக்கா", "சிட்டகாங்"]
    },
    {
        "entity": "India",
        "keywords": ["இந்தியா", "தில்லி", "மும்பை", "ஹைதெராபாத்", "அகமதாபாத்"]
    },
    {
        "entity": "Saudi Arabia",
        "keywords": ["சவூதி அரேபியா", "மெக்கா", "மதினா", "சவூதி"]
    },
    {
        "entity": "Thailand",
        "keywords": ["தாய்லாந்து", "தாய்", "பாங்காக்"]
    },
    {
        "entity": "United Arab Emirates",
        "keywords": ["ஐக்கிய அரபு நாடுகள்", "துபாய்", "அபுதாபி", "uae", "ஷார்ஜா"]
    },
    {
        "entity": "Malaysia",
        "keywords": ["மலேஷியா", "கோலா லம்பூர்", "பெனாங் தீவு", "ஜொகூர்", "கோட்டா", "கிணபாழு", "குசிங்"]
    },
    {
        "entity": "Nepal",
        "keywords": ["நேபால்", "காத்மாண்டு", "போகற"]
    },
    {
        "entity": "Singapore",
        "keywords": ["சிங்கப்பூர்"]
    },
    {
        "entity": "Cambodia",
        "keywords": ["கம்போடியா", "ஃபினோம் பேனா"]
    },
    {
        "entity": "Blocked",
        "keywords": ["தடுக்கப்பட்டது", "தடை", "தடைசெய்யப்பட்டது", "முடக்கப்பட்டது", "முடக்கம்", "முடங்கியது",
                     "பூட்டப்பட்டது"]
    },
    {
        "entity": "Unblocked",
        "keywords": ["விடுவித்தல்", "விடுவிக்கப்பட்டது", "விடுவி"]
    },
    {
        "entity": "Broadband",
        "keywords": ["பிராட்பேண்ட்"]
    },
    {
        "entity": "Mobile",
        "keywords": ["மொபைல்", "செல்லுலார்", "தொலைபேசி", "கைபேசி", "கையடக்க தொலைபேசி", "எனி நெட்ஒர்க்",
                     "லைட் ப்ளாஸ்டர்", "ஸ்மார்ட் ப்ளாஸ்டர்", "அல்ட்ரா 99"]
    },
    {
        "entity": "Mobile Broadband",
        "keywords": ["மொபைல் பிராட்பேண்ட்", "கைபேசியின் அதிவேக இணையதளம்", "நேரம் சார்ந்த பெக்கேஜஸ்", "எம்பிபி"]
    },
    {
        "entity": "Home Broadband",
        "keywords": ["வீட்டு பிராட்பேண்ட்", "எச்பிபி", "மினி பெக்கேஜ்", "அல்ட்ரா பெக்கேஜ்", "ஸ்டாட்டர் பெக்கேஜ்",
                     "லைட்", "ஆபீஸ்", "பூஸ்டர்"]
    },
    {
        "entity": "Router",
        "keywords": ["ரௌட்டர்", "ரவுட்டர்", "திசைவி"]
    },
    {
        "entity": "DTV",
        "keywords": ["டிடிவி", "டிஜிட்டல் தொலைக்காட்சி", "டயலொக் தொலைக்காட்சி", "தொலைக்காட்சி", "டிவி",
                     "பவர் பிலே", "ஆரம்பம்", "பேர்ல்", "பவர் ப்ளஸ்", "தீ", "டைமென்ட்", "எமரால்டு", "கோல்ட்",
                     "டயலொக் டிவி"]
    },
    {
        "entity": "Data",
        "keywords": ["டேட்டா", "தகவல்", "தகவல்கள்", "தரவு"]
    },
    {
        "entity": "Payment & Billing",
        "keywords": ["கட்டணம்", "செலுத்துதல்", "பட்டியலிடல்", "ரசிது", "மசோதா"]
    },
    {
        "entity": "Blling",
        "keywords": ["கட்டணம்", "செலுத்துதல்", "பட்டியலிடல்", "ரசிது", "மசோதா"]
    },
    {
        "entity": "Network & Coverage",
        "keywords": ["கட்டணம்", "செலுத்துதல்", "பட்டியலிடல்", "ரசிது", "மசோதா", "கவரேஜ்"]
    },
    {
        "entity": "Buy",
        "keywords": ["வாங்கு", "கொள்முதல்", "வாங்க", "வாங்கினேன்"]
    },
    {
        "entity": "Calculating",
        "keywords": ["கணித்தல்", "கணிக்கின்றேன்", "கணிக்கின்றது"]
    },
    {
        "entity": "Calculate",
        "keywords": ["கணக்கிடு", "கணக்கிட", "கணக்கிடப்படுகிறது", "கணக்கிடப்பட்டது", "மொத்தம்", "முடிவுசெய்",
                     "நிச்சயி", "உறுதி செய்"]
    },
    {
        "entity": "Calculation",
        "keywords": ["கணக்கீடு", "கணிப்பு", "மதிப்பீடு", "கணிப்பு"]
    },
    {
        "entity": "Calls",
        "keywords": ["அழைப்புகள்", "அழை", "கூப்பிடு", "நிமிடங்கள்", "விநாடிகள்", "அழைப்பு நேரம்"]
    },
    {
        "entity": "CDMA",
        "keywords": ["CDMA", "cdma", "நிலையான அலகு", "நிலையான இணைப்பு", "நிலையான"]
    },
    {
        "entity": "Chatbot",
        "keywords": ["கணினி", "இயந்திரம்", "எந்திரம்", "செயற்கை", "ரோபோ", "AI"]
    },
    {
        "entity": "Program",
        "keywords": ["கணினி நிரல்"]
    },
    {
        "entity": "Club Vision",
        "keywords": ["கிளப் விஷன்", "Club Vision", "club vision", "vision club", "முன்னுரிமை", "சலுகை",
                     "முதன்மை", "உறுப்பினர்", "விசுவாசம்", "அடுக்கு"]
    },
    {
        "entity": "Complaint",
        "keywords": ["புகார்", "குற்றச்சாட்டு", "பிராது", "முறையீடு", "பிரச்சினை", "தொந்தரவு",
                     "குழப்பம்", "சிக்கல்", "குறை தெரிவி"]
    },
    {
        "entity": "Not working",
        "keywords": ["வேலைசெய்யவில்லை", "ெய்யவில்லை", "தோல்வி", "முடியாது", "தவறு", "உடைந்த", "உடைந்தது",
                     "உடைந்துள்ளது"]
    },
    {
        "entity": "Disconnected",
        "keywords": ["துண்டிக்கப்பட்டுள்ளது", "துண்டிக்கப்பட்டது"]
    },
    {
        "entity": "Can't activate",
        "keywords": ["முடியாது"]
    },
    {
        "entity": "Can't",
        "keywords": ["முடியாது"]
    },
    {
        "entity": "too low",
        "keywords": ["குறைந்த, தாழ்ந்த", "குறைந்தது"]
    },
    {
        "entity": "Connection",
        "keywords": ["இணைப்பு", "தொடர்பு"]
    },
    {
        "entity": "Email",
        "keywords": ["மின்னஞ்சல்"]
    },
    {
        "entity": "Call centre",
        "keywords": ["மையம்", "வாடிக்கையாளர்", "ஹாட்லைன்"]
    },
    {
        "entity": "Details",
        "keywords": ["விவரங்கள்", "தகவல்கள்", "தகவல்", "விவரம்", "பெயர்"]
    },
    {
        "entity": "Rate",
        "keywords": ["வீதம்"]
    }

))
