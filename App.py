from flask import Flask, render_template
import requests

app = Flask(__name__)

# Function to fetch data for multiple domains
def get_virustotal_data(domains):
    api_key = 'your_api_key_here'  # Replace with your actual VirusTotal API key
    headers = {
        'x-apikey': api_key
    }
    domain_data = {}
    
    for domain in domains:
        url = f'https://www.virustotal.com/api/v3/domains/{domain}'
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                domain_data[domain] = response.json()
            else:
                domain_data[domain] = f"Error: {response.status_code}"
        except requests.exceptions.RequestException as e:
            domain_data[domain] = f"Error: {str(e)}"
    
    return domain_data

@app.route('/')
def index():
    # Domains to analyze
    domains = ['paypal.com', 'google.com', 'microsoft.com', 'amazon.com', 'facebook.com']
    
    # Fetch data for the listed domains
    domain_data = get_virustotal_data(domains)

    # Threat Data Overview
    data = [
        ("Phishing", 20, "High"),
        ("Malware", 15, "Medium"),
        ("Ransomware", 10, "Critical"),
        ("Spyware", 5, "Low"),
    ]

    # Pie chart data
    pie_data = {
        "labels": ["Phishing", "Malware", "Ransomware", "Spyware"],
        "datasets": [{
            "data": [20, 15, 10, 5],
            "backgroundColor": ['#FF5733', '#33FF57', '#3357FF', '#FF33A6'],
        }]
    }

    return render_template('index.html', data=data, pie_data=pie_data, domain_data=domain_data)

if __name__ == '__main__':
    app.run(debug=True)
