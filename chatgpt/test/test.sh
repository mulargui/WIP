
URL=https://127.0.0.1:3333

date +"%T.%3N"
curl -L -H 'Content-Type: application/json' $URL?zipcode=98052 ; echo
date +"%T.%3N"
curl -L -H 'Content-Type: application/json' $URL?zipcode=98052&distance=10 ; echo
date +"%T.%3N"
curl -L -H 'Content-Type: application/json' $URL?lastname1=anderson ; echo
date +"%T.%3N"
curl -L -H 'Content-Type: application/json' $URL?lastname1=anderson&lastname2=johnson ; echo
date +"%T.%3N"
curl -L -H 'Content-Type: application/json' $URL?lastname1=anderson&lastname2=johnson&lastname3=smith  ; echo
date +"%T.%3N"
curl -L -H 'Content-Type: application/json' $URL?gender=f ; echo
date +"%T.%3N"
curl -L -H 'Content-Type: application/json' $URL?specialty=Nurse ; echo
date +"%T.%3N"

curl -L -H 'Content-Type: application/json' $URL?zipcode=98052&lastname1=anderson ; echo
date +"%T.%3N"
curl -L -H 'Content-Type: application/json' $URL?zipcode=98052&lastname1=anderson&gender=f ; echo
date +"%T.%3N"
curl -L -H 'Content-Type: application/json' $URL?zipcode=98052&lastname1=anderson&gender=f&specialty=Nurse ; echo
date +"%T.%3N"
curl -L -H 'Content-Type: application/json' $URL?zipcode=98052&distance=10&lastname1=anderson&lastname2=johnson&lastname3=smith&gender=f&specialty=Nurse ; echo
date +"%T.%3N"
