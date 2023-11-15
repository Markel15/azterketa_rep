#!/bin/bash
origen=/home/erabiltzailea/Segurtasuna
destino=/var/tmp/Backups

fecha=$(date +%F)

mkdir -p $destino/$fecha

rsync -a --link-dest=$destino/$(date -d yesterday +%F) $origen/ $destino/$fecha/
