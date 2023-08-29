
URL=https://x73rkqly3c.execute-api.us-east-1.amazonaws.com/prod/providers

date +"%T.%3N" ; echo "zipcode=98052"
curl -v -L -H 'Content-Type: application/json' $URL?zipcode=98052 ; echo
date +"%T.%3N" ; echo "zipcode=98052&distance=10" 
curl -i -L -H 'Content-Type: application/json' $URL?zipcode=98052&distance=10 ; echo
date +"%T.%3N" ; echo "lastname1=anderson" 
curl -L -H 'Content-Type: application/json' $URL?lastname1=anderson ; echo
date +"%T.%3N" ; echo "lastname1=anderson&lastname2=brock" 
curl -L -H 'Content-Type: application/json' $URL?lastname1=anderson&lastname2=brock ; echo
date +"%T.%3N" ; echo "lastname1=anderson&lastname2=brock&lastname3=tang-xue" 
curl -L -H 'Content-Type: application/json' $URL?lastname1=anderson&lastname2=brock&lastname3=tang-xue  ; echo
date +"%T.%3N" ; echo "gender=f" 
curl -L -H 'Content-Type: application/json' $URL?gender=f  ; echo
date +"%T.%3N" ; echo "specialty=General%20Practice"
curl -L -H 'Content-Type: application/json' $URL?specialty=General%20Practice ; echo

date +"%T.%3N" ; echo "zipcode=98052&lastname1=anderson" 
curl -L -H 'Content-Type: application/json' $URL?zipcode=98052&lastname1=anderson ; echo
date +"%T.%3N" ; echo "zipcode=98052&lastname1=anderson&gender=f"
curl -L -H 'Content-Type: application/json' $URL?zipcode=98052&lastname1=anderson&gender=f ; echo 
date +"%T.%3N" ; echo "zipcode=98052&lastname1=anderson&gender=f&specialty=General%20Practice"
curl -L -H 'Content-Type: application/json' $URL?zipcode=98052&lastname1=anderson&gender=f&specialty=General%20Practice ; echo  

date +"%T.%3N" ; echo "zipcode=98052&distance=10&lastname1=anderson&lastname2=brock&lastname3=tang-xue&gender=f&specialty=General%20Practice"
curl -L -H 'Content-Type: application/json' $URL?zipcode=98052&distance=10&lastname1=anderson&lastname2=brock&lastname3=tang-xue&gender=f&specialty=General%20Practice ; echo
date +"%T.%3N" ; echo "end"
