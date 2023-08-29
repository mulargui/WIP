
URL=https://v93c3ahq1d.execute-api.us-east-1.amazonaws.com/prod/providers

date +"%T.%3N"
curl -L -H 'Content-Type: application/json' $URL?zipcode=98052 ; echo
date +"%T.%3N"
curl -L -H 'Content-Type: application/json' $URL?zipcode=98052&lastname1=anderson ; echo
date +"%T.%3N"
curl -L -H 'Content-Type: application/json' $URL?zipcode=98052&lastname1=anderson&lastname2=johnson ; echo
date +"%T.%3N"
curl -L -H 'Content-Type: application/json' $URL?zipcode=98052&lastname1=anderson&lastname2=johnson&lastname3=smith  ; echo
date +"%T.%3N"
curl -L -H 'Content-Type: application/json' $URL?zipcode=98052&lastname1=anderson&gender=f ; echo
date +"%T.%3N"
curl -L -H 'Content-Type: application/json' $URL?zipcode=98052&lastname1=anderson&gender=f&distance=10 ; echo
date +"%T.%3N"
curl -L -H 'Content-Type: application/json' $URL?zipcode=98052&lastname1=anderson&gender=f&distance=10&specialty=general ; echo
date +"%T.%3N"

