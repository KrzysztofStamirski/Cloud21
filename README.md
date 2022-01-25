# chmura LoL stats
## uruchamianie
- uzyskaj dostęp do wszystkich maszyn wirtualnych
- uruchom scheduler (domyślnie U2): `dask-scheduler`
- uruchom workery (podając IP schedulera): `dask-worker tcp://172.16.0.5:8786`
- uruchom skrypt na jednej z maszyn (domyuśłnie U1): `python3 compute_corrs_lf.py tcp://172.16.0.5:8786`
- wyniki w pliku  t1_win_correlation.csv (ze względu na dużą ilość wierszy najważniejsze wyniki wyświetlam: `tail t1_win_correlation.csv`)
