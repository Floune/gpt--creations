# Affiche la température à toulouse avec des nuances de couleur 
# en fonction de la température de toulouse

printf "\n"
printf "\n"
echo "\033[41m=================\033[0m"
echo "\033[41m|   TOULOUSE    |\033[0m"
echo "\033[41m=================\033[0m"
RAW_JSON=$(curl -s "http://api.weatherapi.com/v1/current.json?key=aa4aa13bdb844f0aae2113721230601&q=Toulouse&aqi=no")
TEMP=$(echo "$RAW_JSON" | jq -r ".current.temp_c")
WIND=$(echo "$RAW_JSON" | jq -r ".current.wind_kph")
DIR=$(echo "$RAW_JSON" | jq -r ".current.wind_dir")
HUM=$(echo "$RAW_JSON" | jq -r ".current.humidity")
if [ "$TEMP" -gt 30 ]
then
    echo "\033[32;47m      $TEMP°C       \033[0m"
elif [ "$TEMP" -gt 10 ]
then
    echo "\033[31;47m      $TEMP°C       \033[0m"
else
    echo "\033[33;47m      $TEMP°C       \033[0m"
fi

echo "\033[30;47mVent $DIR $WIND km/h\033[0m"
echo "\033[30;47m$HUM% d'humidité   \033[0m"
printf "\n"
printf "\n"


