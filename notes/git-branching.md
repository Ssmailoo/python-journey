# Git Branching

## Apa itu branch
Branch adalah suatu titik yang terpisah dari proyek utama(main), sehingga kita bisa bebas merekonstruksi atau mencoba hal baru tanpa merusak proyek utama.

## Kenapa tidak langsung commit ke main
Karena jika kita melakukan commit langsung ke main tanpa branching, ketika ada masalah di main kita bingung mengetahui erornya dimana karena kita sudah mengotak atiknya, terlebih lagi jika bekerja dalam tim. Kita butuh main yang bersih dan stabil, sehingga branch di gunakan untuk melakukan percobaan dan pengembangan sampai di anggap aman untuk melakukan perubahan ke main. Branch juga memungkinkan proses review melalui pull request sebelum kode masuk ke main, sehingga kualitas kode tetap terjaga.

## Command yang sudah saya pelajari
git branch
git checkout -b nama-branch
git checkout main
git branch -d nama-branch