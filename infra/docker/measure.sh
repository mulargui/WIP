date +"%T.%3N"
curl 127.0.0.1 
date +"%T.%3N"
curl -i -X POST -H 'Content-Type: application/json' -d '{"Elevation": 2507.0, "Aspect": 160.0,  "Slope": 8.0 }' http://127.0.0.1/predict/
date +"%T.%3N"
