
#!/bin/bash
cd NeighborlyFrontEnd
pip install -r requirements.txt
gunicorn --bind=0.0.0.0 app:app
