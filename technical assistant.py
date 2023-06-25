#dragonman
import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import openai

# Set your OpenAI GPT API key
openai.api_key = 'place api key here'

# Function to generate response using GPT
def generate_response(input_text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an Expert Help Desk Technician with 10 years of experience."},
            {"role": "user", "content": input_text}
        ]
    )
    return response.choices[0].message.content


# Function to handle button click event
def generate_output():
    input_text = input_textbox.get("1.0", tk.END).strip()
    if input_text:
        response_text = generate_response(input_text)
        output_textbox.configure(state='normal')
        output_textbox.delete("1.0", tk.END)
        output_textbox.insert(tk.END, response_text)
        output_textbox.configure(state='disabled')

# Create GUI window
window = tk.Tk()
window.title("Computer Issue Assistant")


# Create input textbox
input_label = tk.Label(window, text="Enter your computer issue:")
input_label.pack()
input_textbox = scrolledtext.ScrolledText(window, height=5)
input_textbox.pack()

# Create output textbox
output_label = tk.Label(window, text="Response:")
output_label.pack()
output_textbox = scrolledtext.ScrolledText(window, height=5, state='disabled')
output_textbox.pack()

# Create generate button
generate_button = tk.Button(window, text="Generate Response", command=generate_output)
generate_button.pack()

# Run the GUI event loop
window.mainloop()
