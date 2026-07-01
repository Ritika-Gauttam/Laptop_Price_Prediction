from flask import Flask , url_for ,request , render_template
import joblib
import pandas as pd
model = joblib.load(r"C:\Users\user\OneDrive\Desktop\DATA_SCIENCE_UPFLAIR\Laptop_Price_Prediction\model\model.lb")
app = Flask(__name__)
df = pd.read_csv('laptop_data_cleaned.csv') 
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


    # Jis sequence mein model train kiya hai, usi order mein unique list banayein
    # unique_gpus_raw = df['GPU'].dropna().unique().tolist()
    
    # Python dictionary mapping (taaki index hamesha original hi rahe)
    # gpu_mapping = {gpu: index for index, gpu in enumerate(unique_gpus_raw)}
    
    # HTML par alphabetically dikhane ke liye sort karein
    # sorted_gpus = sorted(unique_gpus_raw)
    
    # HTML file ko render karte waqt sorted_gpus aur gpu_mapping dono bhej dein
    # return render_template('index.html', sorted_gpus=sorted_gpus, gpu_mapping=gpu_mapping)


if __name__ == "__main__":
    app.run(debug=True)