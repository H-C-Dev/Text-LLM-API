# Exmaple input = "Parts of the UK could see one of the hottest June days ever as a heatwave, now in its fourth day, peaks on Monday. Temperatures of 34C are possible around the Greater London and Bedfordshire areas with a small chance of reaching 35C. If the temperature does go above 34C as expected, it would be in the top three hottest June days on record. It is not expected to challenge the hottest day though of 35.6C set in 1976."

class RequestBody:
    def __init__(self, input, temp, topP, maxTokenCount, stopSequences=[]):
        self.inputText = self.__set_input_text(input)
        self.temp = temp
        self.topP = topP
        self.maxTokenCount = maxTokenCount
        self.stopSequences = stopSequences

    def __set_input_text(self, input):
        return f"User: Summarise the following text:\n\n{input}\nBot:"
    
    def get_request_body(self):
        request_body = {
            "inputText": self.inputText,
            "textGenerationConfig": {
            "temperature": self.temp,  
            "topP": self.topP,
            "maxTokenCount": self.maxTokenCount,
            "stopSequences": self.stopSequences
            }
        }
        return request_body


        
