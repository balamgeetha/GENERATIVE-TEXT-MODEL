 from transformers import pipeline
generator = pipeline('text-generation', model='gpt2')
#Try gpt2-medium or gpt2-large if you have enough memory
def generate_text(prompt, max_length=100):
result = generator(prompt, num_return_sequences=1, return_full_text=True, pad_token_id=50256)
if result and isinstance(result, list) and 'generated_text' in result[0]:
generated_text = result[0]['generated_text']
else:
generated_text = ""
return generated_text
prompt = input("Enter a prompt: ")
print(f"Prompt: {prompt}")
result = generate_text(prompt)#, max_length=100)
# result = generate_text("Make a cup of tea", max_length=50)
print(f"Generated text: {result}")

#prompt should be clear to get good results
# Tell me a short, emotional story about the time I went to a house party with my dad and his friends. I told him not to go, but he insisted. What happened next changed our relationship forever.
# Unclear prompt : "Make a cup of tea"
