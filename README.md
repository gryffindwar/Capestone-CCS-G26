# Capestone-CCS-G26

Threat Intelligence Dashboard
Overview
This project is a Threat Intelligence Dashboard built using Flask (Python framework), Plotly (for charts), and HTML/CSS for the frontend. The dashboard fetches threat data related to different domains (like example.com, paypal.com, etc.) and displays it in a user-friendly manner with a pie chart, bar graph, and a domain threat data overview table.

The purpose of this project is to provide insights into the threat landscape by visualizing domain threat levels, severity, and additional data such as VirusTotal reports. The dashboard can display multiple domains and provides easy-to-read charts for analyzing threat data.

Features
Interactive Dashboard: Displays threat data in a clean, visually appealing layout.
Charts: Includes a pie chart and bar graph representing threat levels across different domains.
Data Table: A table showing detailed domain threat data including:
Domain Name
Threat Level
Count of Threats
Severity
VirusTotal Report (or placeholder if no data is available)
Technologies Used
Flask: For backend API and serving HTML templates.
Plotly: For creating interactive charts.
Pandas: For handling data manipulation.
Matplotlib: For chart creation.
HTML/CSS: For building the frontend.
Bootstrap (optional): For styling (if needed).
Requirements
Python 3.x
Flask
Plotly
Pandas
Matplotlib
Requests
Installation
Follow these steps to install and run the project locally:

Clone the Repository:

bash

git clone https://github.com/your-username/threat_intelligence_dashboard.git
cd threat_intelligence_dashboard
Create a Virtual Environment (Optional but recommended):

On Windows:

bash

python -m venv venv
On macOS/Linux:

bash

python3 -m venv venv
Activate the Virtual Environment:

On Windows:

bash

venv\Scripts\activate
On macOS/Linux:

bash
Copy code
source venv/bin/activate
Install Dependencies:

bash

pip install -r requirements.txt
If requirements.txt is not available, manually install the necessary packages:

bash

pip install Flask Plotly pandas matplotlib requests
Running the Application
Run the Flask App:

In the project folder, run the following command to start the Flask development server:

bash

python app.py


Project Structure
Here’s a breakdown of the project structure:

bash

threat_intelligence_dashboard/
│
├── app.py               # Backend logic to fetch data and generate charts
├── index.html           # HTML template for the dashboard
├── style.css            # CSS for styling the dashboard
├── requirements.txt     # Python dependencies
└── README.md            # Project description and setup instructions
File Descriptions:
app.py: The main backend file where Flask routes are defined, data is fetched, and charts are created.
index.html: The frontend HTML file where the dashboard layout is defined.
style.css: The CSS file that styles the page (colors, layout, etc.).
Customizing the Dashboard
You can customize the following:

Add More Domains:
Modify the domains list in app.py to include additional domains.
Change Charts:
You can modify the create_pie_chart and create_bar_graph functions to display different data or charts.
Change Table Data:
Modify the data inside the fetch_threat_data() function in app.py to reflect your custom threat data sources.
Troubleshooting
Issue: App Doesn't Run
Solution: Make sure that Flask and other dependencies are properly installed. Use pip install -r requirements.txt to install all dependencies.

Issue: Chart Doesn't Appear
Solution: Check if Plotly and Matplotlib are installed. Ensure that the functions for generating charts are correctly defined in app.py.
