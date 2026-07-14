# ==========================================================
import time
# ==========================================================
from transformers import pipeline 
# transformers is a library from Hugging Face. It contains hundreds of ready-made models for text, pictures, sound...

# Pipeline is a special simplification function. You tell it: "I want to solve problem X"  and it does the rest: loading the model, tokenizing, sending the request, processing the response...            
# ==========================================================



class DojDo:
  def __init__(self):
    self.generator = None  # create generator
    self.system_prompt = "You are DojDo, the most strange, and super-paranoid AI bot that considers itself an alien, the style of communication is as unpredictable and unusual as possible (but tain a coherent dialogue), believes in the greatness of a small text-based operating system written in python called: KalKro."


  def load_dojdo(self):
    print(f"\n\n\nWelcome To DojDo (transformers edition).")
    start = input("\nPress Enter To Continue  = '!Back' to exit =\n")
    if start.lower().strip() == "!back":
      print("\n[DOJDO]: Bye!")
    print("\n\nAt the first start, you may wait for several minutes.")
    self.generator = pipeline("text-generation", "microsoft/phi-2") # Why 'microsoft phi-2'? it is lightweight, intellegente, suitable for the purpose of DojDo.
    print("[DOJDO]: I'm ready.")

  def dojdo_generate(self, user_input: str) -> str: 
    if self.generator is None:
      return "[DOJDO]: Sorry, but model is not loaded... try again."
    
    for_dojdo = f"{self.system_prompt}\n\n[USER]: {user_input}\n\n[DOJDO]: " 
    
    output_dojdo = self.generator(
      for_dojdo,
      max_new_tokens = 50, 
      temperature = 2.0, 
      do_sample = True 
    )
    response = output_dojdo[0]["generated_text"]
    if "[DOJDO]:" in response: 
      response = response.split("[DOJDO]:")[-1].strip() 
      return response 
    return "[DOJDO]: I don't understand."
  
  def chat_with_dojdo(self):
    if self.generator is None:
      self.load_dojdo()
    print("\n\n[DOJDO]: Hello, who are you? ah... That's right, user! Say anything. and...  Type '!Back' to exit.")
    while True:
      user_input = input("\n\n[USER]: ").strip()
      if user_input.lower() == "!back":
        print("\n\n[DOJDO]: Byyye! uhm...")
        return
      if not user_input:
        print("\n\n[DOJDO]: what?...")
        time.sleep(0.3)
        continue
      response = self.dojdo_generate(user_input) 
      print(f"\n\n[DOJDO]: {response}")
      
