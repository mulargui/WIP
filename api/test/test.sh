
URL=https://v93c3ahq1d.execute-api.us-east-1.amazonaws.com/prod/providers

date +"%T.%3N" ; echo "zipcode=98052"
curl -L -H 'Content-Type: application/json' $URL?zipcode=98052
date +"%T.%3N" ; echo "zipcode=98052&distance=10" 
curl -L -H 'Content-Type: application/json' $URL?zipcode=98052&distance=10
date +"%T.%3N" ; echo "lastname1=anderson" 
curl -L -H 'Content-Type: application/json' $URL?lastname1=anderson
date +"%T.%3N" ; echo "lastname1=anderson&lastname2=brock" 
curl -L -H 'Content-Type: application/json' $URL?lastname1=anderson&lastname2=brock
date +"%T.%3N" ; echo "lastname1=anderson&lastname2=brock&lastname3=tang-xue" 
curl -L -H 'Content-Type: application/json' $URL?lastname1=anderson&lastname2=brock&lastname3=tang-xue 
date +"%T.%3N" ; echo "gender=f" 
curl -L -H 'Content-Type: application/json' $URL?gender=f 
date +"%T.%3N" ; echo "specialty=General%20Practice"
curl -L -H 'Content-Type: application/json' $URL?specialty=General%20Practice 

date +"%T.%3N" ; echo "zipcode=98052&lastname1=anderson" 
curl -L -H 'Content-Type: application/json' $URL?zipcode=98052&lastname1=anderson 
date +"%T.%3N" ; echo "zipcode=98052&lastname1=anderson&gender=f"
curl -L -H 'Content-Type: application/json' $URL?zipcode=98052&lastname1=anderson&gender=f 
date +"%T.%3N" ; echo "zipcode=98052&lastname1=anderson&gender=f&specialty=General%20Practice"
curl -L -H 'Content-Type: application/json' $URL?zipcode=98052&lastname1=anderson&gender=f&specialty=General%20Practice  
date +"%T.%3N" ; echo "zipcode=98052&distance=10&lastname1=anderson&lastname2=brock&lastname3=tang-xue&gender=f&specialty=General%20Practice"

curl -L -H 'Content-Type: application/json' $URL?zipcode=98052&distance=10&lastname1=anderson&lastname2=brock&lastname3=tang-xue&gender=f&specialty=General%20Practice
date +"%T.%3N"
