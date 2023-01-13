#!/bin/bash

# Définir les couleurs de l'arc en ciel
RAINBOW=('\e[38;5;196m' '\e[38;5;202m' '\e[38;5;208m' '\e[38;5;214m' '\e[38;5;220m' '\e[38;5;226m' '\e[38;5;190m' '\e[38;5;154m' '\e[38;5;118m' '\e[38;5;82m' '\e[38;5;46m' '\e[38;5;47m' '\e[38;5;48m' '\e[38;5;49m' '\e[38;5;50m' '\e[38;5;51m')

# Afficher l'arc en ciel
for color in "${RAINBOW[@]}"
do
    echo -e "$color¯\_(ツ)_/¯¯\_(ツ)_/¯¯\_(ツ)_/¯¯\_(ツ)_/¯¯\_(ツ)_/¯¯\_(ツ)_/¯"
done
