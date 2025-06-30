input = "Parts of the UK could see one of the hottest June days ever as a heatwave, now in its fourth day, peaks on Monday. Temperatures of 34C are possible around the Greater London and Bedfordshire areas with a small chance of reaching 35C. If the temperature does go above 34C as expected, it would be in the top three hottest June days on record. It is not expected to challenge the hottest day though of 35.6C set in 1976."

prompt = f"User: Summarise the following text:\n\n{input}\nBot:"

request_body = {
    "inputText": prompt,
    "textGenerationConfig": {
        "temperature": 0.5,  
        "topP": 0.5,
        "maxTokenCount": 512,
        "stopSequences": []
    }
}


