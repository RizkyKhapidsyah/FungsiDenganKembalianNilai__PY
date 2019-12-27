# FungsiDenganKembalianNilai__PY

Bahan Ajar Pemrograman Python - Membuat dan Menggunakan Fungsi Yang Mengembalikan Nilai (Dengan 1 Argument dan Banyak Argument).<br><br>
<img src="https://github.com/RizkyKhapidsyah/FungsiDenganKembalianNilai__PY/blob/master/results/001.PNG"><br>
<img src="https://github.com/RizkyKhapidsyah/FungsiDenganKembalianNilai__PY/blob/master/results/002.PNG"><br><br>

# - Lihat <a href="https://github.com/RizkyKhapidsyah/FungsiDenganKembalianNilai__PY/blob/master/FungsiDenganKembalianNilai__PY.py">Source Code.</a><br>

Fungsi adalah grup/blok program untuk melakukan tugas tertentu yang berulang. Fungsi membuat kode program menjadi reusable, artinya hanya di definisikan sekali saja, dan kemudian bisa digunakan berulang kali dari tempat lain di dalam program. Fungsi memecah keseluruhan program menjadi bagian – bagian yang lebih kecil . Dengan semakin besarnya program, maka fungsi akan membuatnya menjadi lebih mudah diorganisir dan dimanage. Sejauh ini, kita sudah menggunakan beberapa fungsi, misalnya fungsi print(), type(), dan sebagainya. Fungsi tersebut adalah fungsi bawaan dari Python. Kita bisa membuat fungsi kita sendiri sesuai kebutuhan.

# Mendefinisikan Fungsi

Berikut adalah sintaks yang digunakan untuk membuat fungsi:

      def function_name(parameters):
          """function_docstring"""
          statement(s)
          return [expression]

Penjelasannya dari sintaks fungsi di atas:

Kata kunci def diikuti oleh function_name (nama fungsi), tanda kurung dan tanda titik dua (:) menandai header (kepala) fungsi.
Parameter / argumen adalah input dari luar yang akan diproses di dalam tubuh fungsi. "function_docstring" bersifat opsional, yaitu sebagai string yang digunakan untuk dokumentasi atau penjelasan fungsi. “function_doctring” diletakkan paling atas setelah baris def. Setelah itu diletakkan baris – baris pernyataan (statements). Jangan lupa indentasi untuk menandai blok fungsi. return bersifat opsional. Gunanya adalah untuk mengembalikan suatu nilai expression dari fungsi. Berikut adalah contoh fungsi untuk menyapa seseorang.

      def sapa(nama): 
          """Fungsi ini untuk menyapa seseorang sesuai nama yang dimasukkan sebagai parameter""" 
          print("Hi, " + nama + ". Apa kabar?") 

      # pemanggilan fungsi 
      # output: Hi, Umar. Apa kabar? 
      sapa('Umar') 
 
# Memanggil Fungsi

Bila fungsi sudah didefinisikan, maka ia sudah bisa dipanggil dari tempat lain di dalam program. Untuk memanggil fungsi caranya adalah dengan mengetikkan nama fungsi berikut paramaternya. Untuk fungsi di atas, kita bisa melakukannya seperti contoh berikut:

>>> sapa('Galih')<br>
Hi, Galih. Apa kabar?

>>> sapa('Ratna')<br>
Hi, Ratna. Apa kabar?

# Docstring

Docstring adalah singkatan dari documentation string. Ini berfungsi sebagai dokumentasi atau keterangan singkat tentang fungsi yang kita buat. Meskipun bersifat opsional, menuliskan docstring adalah kebiasaan yang baik. Untuk contoh di atas kita menuliskan docstring. Cara mengaksesnya adalah dengan menggunakan format namafungsi.__doc__

>>> print(sapa.__doc__)<br>
"""Fungsi ini untuk menyapa seseorang sesuai nama yang dimasukkan sebagai parameter"""

# Pernyataan return

Pernyataan return digunakan untuk keluar dari fungsi  dan kembali ke baris selanjutnya dimana fungsi dipanggil. Adapun sintaks dari return adalah:

      return [expression_list]
      
return bisa berisi satu atau beberapa ekspresi atau nilai yang dievaluasi dan nilai tersebut akan dikembalikan. Bila tidak ada pernyataan return yang dibuat atau ekspresi dikosongkan, maka fungsi akan mengembalikan objek None.

Perhatikan bila hasil keluaran dari fungsi sapa kita simpan dalam variabel.

>>> keluaran = sapa('Gani')<br>
>>> print(keluaran)<br>
>>> None

# Argumen Fungsi

Kita bisa memanggil fungsi dengan menggunakan salah satu dari empat jenis argumen berikut:

- Argumen wajib (required argument)
- Argumen kata kunci (keyword argument)
- Argumen default
- Argumen dengan panjang sembarang
- Argumen Wajib

Argumen wajib adalah argumen yang dilewatkan ke dalam fungsi dengan urutan posisi yang benar. Di sini, jumlah argumen pada saat pemanggilan fungsi harus sama persis dengan jumlah argumen pada pendefinisian fungsi

Pada contoh fungsi sapa() di atas, kita perlu melewatkan satu argumen ke dalam fungsi sapa(). Bila tidak, maka akan muncul error.

>>> sapa('Umar')<br>
Hi Umar. Apa kabar?<br><br>

>>> "# akan muncul error<br>
>>> sapa()<br>

      Traceback (most recent call last):
       File "<pyshell#5>", line 1, in <module>
       sapa()
      TypeError: sapa() missing 1 required positional argument: 'nama'

# Argumen Kata Kunci

Argumen dengan kata kunci berkaitan dengan cara pemanggilan fungsi. Ketika menggunakan argumen dengan kata kunci, fungsi pemanggil menentukan argumen dari nama parameternya. Hal ini membuat kita bisa mengabaikan argumen atau menempatkannya dengan sembarang urutan. Python dapat menggunakan kata kunci yang disediakan untuk mencocokkan nilai sesuai dengan parameternya. Jelasnya ada pada contoh berikut:

      # definisi fungsi print_string 
      def print_string( str ): 
          """Menampilkan argumen string str ke layar""" 
          print (str) 

      # Kita memanggil fungsi dengan kata kunci 
      print_string( str = "Hello Python") 

Urutan parameter tidak menjadi masalah. Perhatikan contoh berikut:

      # Definisi fungsi 
      def print_info( nama, usia ): 
          """Fungsi ini menampilkan info yang dimasukkan"""
          print ("Nama: ", nama) 
          print ("Usia: ", usia) 

      # Memanggil fungsi 
      # output 
      # Name: Budi 
      # Usia: 25 
      print_info( usia = 25, nama = "Budi" )
 
# Argumen Default

Fungsi dengan argumen default menggunakan nilai default untuk argumen yang tidak diberikan nilainya pada saat pemanggilan fungsi. Pada contoh berikut, fungsi akan menampilkan usia default bila argumen usia tidak diberikan:

      # Definisi fungsi 
      def print_info( nama, usia= 17 ): 
          """Fungsi ini menampilkan info yang dimasukkan""" 
          print ("Nama: ", nama) 
          print ("Usia ", usia) 

      # Memanggil fungsi print_info 
      print_info( usia = 29, nama = "Galih" ) 

      # Pemanggilan fungsi tidak menyediakan argumen usia 
      print_info( nama = "Galih" ) 

Pada contoh di atas, pemanggilan fungsi kedua tidak menyediakan nilai untuk parameter usia, sehingga yang digunakan adalah nilai default yaitu 17. Bila program di atas dijalankan, hasilnya adalah seperti berikut:

>>> Nama: Galih<br>
>>> Usia: 29<br>
>>> Nama: Galih<br>
>>> Usia: 17<br>

# Argumen Dengan Panjang Sembarang

Terkadang kita butuh untuk memproses fungsi yang memiliki banyak argumen. Nama – nama argumennya tidak disebutkan saat pendefinisian fungsi, beda halnya dengan fungsi dengan argumen wajib dan argumen default.

Sintaksnya fungsi dengan argumen panjang sembarang adalah seperti berikut:

      def function_name([formal_args,] *var_args_tuple): 
          """function_docstring""" 
          statement(s) 
          return [expression]

Tanda asterisk (*) ditempatkan sebelum nama variabel yang menyimpan nilai dari semua argumen yang tidak didefinisikan. Tuple ini akan kosong bila tidak ada argumen tambahan pada saat pemanggilan fungsi. Berikut adalah contohnya:

      # Definisi fungsi 
      def print_info( arg1, *vartuple ): 
          """Fungsi untuk menampilkan nilai argumen sembarang yang dilewatkan""" 
          print ("Outputnya adalah: ") 
          print (arg1) 
          for var in vartuple: 
              print (var) 

      # Pemanggilan fungsi 
      # Satu argumen 
      print_info( 10 ) 

      # Empat argumen 
      print_info( 10, 30, 50, 70 ) 

Pada saat program di atas dijalankan maka hasilnya adalah seperti berikut:

>>> Outputnya adalah:<br>
>>> 10<br>
>>> Outputnya adalah:<br>
>>> 10<br>
>>> 30<br>
>>> 50<br>
>>> 70<br>

# Ruang Lingkup (Scope) Variabel

Di Python, tidak semua variabel bisa diakses dari semua tempat. Ini tergantung dari tempat dimana kita mendefinisikan variabel. Ruang lingkup variabel ada dua, yaitu:

- Global
- Local

Variabel yang didefinisikan di dalam fungsi memiliki scope lokal, sedangkan variabel yang didefinisikan di luar fungsi memiliki scope global. Ini berarti, variabel lokal hanya bisa diakses dari dalam fungsi di mana ia di definisikan, sedangkan variabel global bisa diakses dari seluruh tempat dimanapun di dalam program. Berikut adalah contohnya:

      total = 0 
      # Variabel global 
      # Definisi fungsi 
      def sum( arg1, arg2 ): 
          """Menambahkan variabel dan mengembalikan hasilnya."""
          total = arg1 + arg2; 
          # total di sini adalah variabel lokal 
          print ("Di dalam fungsi nilai total : ", total) 
          return total 

      # Pemanggilan fungsi sum 
      sum( 10, 20 ) 
      print ("Di luar fungsi, nilai total : ", total ) 

Pada saat dijalankan, maka hasilnya adalah seperti berikut:

>>> Di dalam fungsi nilai total : 30 <br>
>>> Di luar fungsi, nilai total : 0 <br>

Perhatikan bagaimana variabel total di dalam dan di luar fungsi adalah dua variabel yang berbeda.<br><br>

Referensi Artikel: <a href="https://www.pythonindo.com">PythonIndo</a>. Thanks To: <a href="https://www.pythonindo.com">PythonIndo</a><br>
Referensi Source Code:<a href="https://www.youtube.com/user/faqihzamukhlish"> Kelas Terbuka </a> dan <a href="https://github.com/kelasterbuka"> Kelas Terbuka (Repository)</a>. Created by <a href="https://github.com/faqihza">Faqihza Mukhlish.</a> Thanks To: <a href="https://www.youtube.com/channel/UCRGHjysoCemh4y7tCJQs30w/about">Faqihza Mukhlish.</a><br>

-----
All Source Code is Modified.




