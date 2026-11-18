FRESHERS INVITATION GENERATOR

EVENT DETAILS INCLUDED
College: College of Horticulture and FSR, Nalbari
Date: 23 November 2026
Venue: Seminar Hall

WHAT IT DOES
1. Student opens the website.
2. Student enters their name and roll number.
3. The personalized invitation page opens with those details printed on the invitation.
4. They can print it or save it as PDF.

RUN ON YOUR COMPUTER
1. Install Python 3.
2. Open a terminal inside this project folder.
3. Run:  pip install -r requirements.txt
4. Run:  python app.py
5. Open this address in your browser: http://127.0.0.1:5000

INVITATION DESIGN
The customized invitation design is included at static/invitation.jpg.
The student's name and roll number are inserted dynamically by Flask.
The event time is still shown as “Coming Soon” because no time was provided.

MAKE A PUBLIC WEBSITE LINK
This ZIP is the website source code; it is not yet hosted on the internet.
To get a public link, deploy this project to a Python hosting service such as
Render. Create a new Web Service from the project repository, use:
Build command: pip install -r requirements.txt
Start command: gunicorn --workers 2 --threads 4 --timeout 30 app:app
Choose Singapore as the Render region for users primarily in Assam/India, if available.

After deployment, the hosting service gives you a public URL. A QR code can
then be generated from that public URL. The app does not save student submissions; it only renders each invitation. The two-worker Gunicorn command is a starting configuration, not a guarantee of 100 requests per minute. Run a load test against the live service and scale the instance/workers if needed.
