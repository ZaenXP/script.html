<html><meta charset='UTF-8'/><meta content='width=device-width, initial-scale=1, user-scalable=1, minimum-scale=1, maximum-scale=5' name='viewport'/><meta content='IE=edge' http-equiv='X-UA-Compatible'/>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Josefin+Sans:wght@400;700&display=swap" rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=Ubuntu&display=swap" rel="stylesheet"><script src="https://cdn.jsdelivr.net/npm/sweetalert2@11.0.19/dist/sweetalert2.all.min.js"></script><script src="https://kit.fontawesome.com/4f3ce16e3e.js" crossorigin="anonymous"></script><link href="https://drive.google.com/uc?export=view&id=1VfmTZv0p4DDLybPc7oiGxXeG8bfDKYNz" rel="stylesheet" type="text/css" /><script src="https://Kudapatkan.feeldream.repl.co/script.js"></script>
<head>
<title>Script HTML</title>
<!-- 
  Script html video 
-->
</head>
<!-- Edit Wallpaper 
di background-image URL --><style>
:root {
--warna-bg: rgb(44, 54, 57,.85);
--warna-teks: #fff;
--warna-bingkai: #fff;
--bingkai: 14px;
--bingkai-kiri: 2px solid var(--warna-bingkai);
--bingkai-kanan: 2px solid var(--warna-bingkai);
--gaya-font: 'Josefin Sans', sans-serif;
--gaya-font2: 'Ubuntu', sans-serif;
}
</style>
<body>
	
   <!-- Ganti Audio di sini --><audio id="linkmp3">https://feeldreams.github.io/sepatu.mp3</audio>
   
   <div id="bodyblur">
     <!-- Wallpaper --><img src="https://feeldreams.github.io/wpemandangan.jpg" id="wallpaper"/>
   </div>

   <div id='Content'>

   <!-- Stiker untuk Pesan Awal --><div id="pesanstiker">
		<img id="stiker1" src="https://feeldreams.github.io/peach1.gif"/>
		<img id="stiker2" src="https://feeldreams.github.io/peach3.gif"/>
		<img id="stiker3" src="https://feeldreams.github.io/peach2.gif"/>
		<img id="stiker4" src="https://feeldreams.github.io/peachkiss.gif"/>
        <img id="stiker5" src="https://feeldreams.github.io/peach11.gif"/>
	</div>

   <!-- Pesan Awal -->
   <script id="pesanAwal">
   	async function pesanutama(){
         audio.play();
   	  await swalst.fire({
            title: 'Pergi Membeli Sepatu,',
            imageUrl: '' + stiker1.src,
            timer: 1200,
         });   	
            await swalst.fire({
            title: 'Pulangnya Membeli Paku 😆',
            imageUrl: '' + stiker2.src,
            timer: 1600,
         });
            await swalst.fire({
            title: 'Yang Ku Mau Itu Cuman Satu,',
            imageUrl: '' + stiker3.src,
            timer: 1500,
         });
            await swalst.fire({
            title: 'Yaitu, Ku Dapatkan Kamu..',
            imageUrl: '' + stiker4.src,
            timer: 1500,
         });
            titleAkhir = "Sebagai Milik Aku 🤣❤️";
            await swalst.fire({
            title: '' + titleAkhir,
            imageUrl: '' + stiker5.src,
            timer: 1000,
         });
         mulaikonten();
       }
     </script>
   
     <div><blockquote id='bq'>
       <div>
         <!-- Stiker untuk Konten -->
         <img src="https://feeldreams.github.io/peachktw.gif" id="fotoakhir"/>
         <img src="https://sinkronin.github.io/peach10.gif" id="fotoakhir2"/>
       </div>

       <!-- Konten Penerapan -->
       <p id="kalimat"></p>
       <p id="kalimatb">Anjay🤣</p><p id="kalimatbb">Radagelo :v</p>
       <p id="kalimatc">Hahahaha🤪</p>

       <!-- Konten Pertanyaan -->
       <p id="kalimat2">Kamu Mau Kan Jadi Milikku? 🤭❤️</p>
       <p id="kalimatb2"></p>
       <p id="kalimatc2"></p>

       <!-- Konten Jawaban -->
       <p id="kalimat3">Yeaayy!!!🥳</p>
       <p id="kalimatb3">Balas pesan ke WhatsApp aku yaa😆❤️</p>
       <p id="kalimatc3"></p>
     </blockquote></div>

      <!-- Pesan Ditolak -->
     <div id="pesanditolak">
       <img id="stikerditolak" src="https://feeldreams.github.io/ywdh.gif"/>
       <p id="kataditolak">Yaahh🥺 yaudah deh:(</p>
     </div>
   
     <!-- Tombol Multifungsi -->
     <div id="Tombol">
       <a id="By" onClick="multifungsi()">
         <b id="tmbl">Lanjut</b>
         <b id="tmbl2">Mau</b>
       </a>
       
       <a id="Bn" onClick="ditolak()">Gamau</a>
     </div>
     
   </div>

<!-- Jangan Edit Bagian Ini --><script>
  audio = new Audio('' + linkmp3.innerHTML);
  var aa=0,katangetik1;katangetik1=kalimatb.innerHTML;kalimatb.innerHTML="";
  var ab=0,katangetik2;katangetik2=kalimatbb.innerHTML;kalimatb.innerHTML="";
  var ac=0,katangetik3;katangetik3=kalimatc.innerHTML;kalimatc.innerHTML="";
  ftom=0;jikakuis=0;ftganti=0;flag=1;flagg=1;fungsi=0;
  
  async function memulai(){await swals.fire('Selamat datang!', 'Sekarang lihat ini ya :)');setTimeout(pesanutama,300)}
  
  function mulaikonten() {pesanwhatsapp = "Iyadeh aku mau ><";ftmuncul();setTimeout(ngetik1,50);setTimeout(pergantian,1000);kalimat.innerHTML=titleAkhir;Content.style = "opacity:1;margin-top:2vh;";bodyblur.style="opacity:.3;animation:none";wallpaper.style="transform: scale(2);opacity:1;";bq.style = "position:relative;opacity:1;visibility:visible;border-radius:var(--bingkai);margin-top:0;";fungsi=1;}
  
  function ftmuncul(){if(ftganti==0){fotoakhir.style="display:inline-flex;transition:all 0s ease;opacity:1;transform:scale(1)";}else{fotoakhir.src = fotoakhir2.src;fotoakhir.style="display:inline-flex;opacity:1;transition:all .7s ease;transform:scale(1);padding:10px;";setTimeout(jjfoto,490);}}
  function fthilang(){fotoakhir.style="display:inline-flex;opacity:1;transition:all .7s ease;transform:scale(.1)";}
  function jjfoto(){fotoakhir.style.animation="rto .8s infinite alternate";}
  
  function tombol(){Tombol.style="opacity:1;transform: scale(1);";
                    if(jikakuis==0){Bn.style.display="none";ftom=1;} 
                    if(jikakuis==1){tmbl.innerHTML=tmbl2.innerHTML;Bn.style="margin:12px 0 12px 12px";ftom=2;}}
  
  function multifungsi(){if(ftom==1){dilanjut();} if(ftom==2){diterima();} if(ftom==5){menuju();}}
  
  async function menuju(){await swals.fire('OK!', 'Kirim pesan ke WhatsApp aku, ya!', 'success');window.location = "https://api.whatsapp.com/send?phone=&text=" + pesanwhatsapp;Tombol.style="margin-top:15px;opacity:1;transform: scale(1);";}

  const swalst = Swal.mixin({timer: 2777, allowOutsideClick: false, showConfirmButton: false, timerProgressBar: true, imageHeight: 100,}); const swals = Swal.mixin({allowOutsideClick: false, cancelButtonColor: '#FF0040', imageWidth: 100, imageHeight: 100,}); const style = document.createElement('style'); var today = new Date();var dd = String(today.getDate()).padStart(2, '0');var mm = String(today.getMonth() + 1).padStart(2, '0');var yyyy = today.getFullYear();const monthNames = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"];today = dd + ' ' + monthNames[today.getMonth()] + ' ' + yyyy;

  function pergantian(){kalimatb.innerHTML="";setTimeout(ngetik2,50);setTimeout(ngetik3,1000);}
  function ngetik1() {if(aa<katangetik1.length){kalimatb.innerHTML += katangetik1.charAt(aa);aa++;setTimeout(ngetik1,40);}}
  function ngetik2() {if(ab<katangetik2.length){kalimatb.innerHTML += katangetik2.charAt(ab);ab++;setTimeout(ngetik2,60);}}
  function ngetik3() {if(ac<katangetik3.length){kalimatc.innerHTML += katangetik3.charAt(ac);ac++;setTimeout(ngetik3,60);}
                      if(ac==katangetik3.length){setTimeout(tombol,500);}}
  
  function dilanjut(){otomatis2();Tombol.style="opacity:0;transform: scale(.1);";jikakuis=1;setTimeout(tombol,1000);}
  
  function otomatis() {befanimkata();setTimeout(animkata,400);} 
  function befanimkata(){kalimat.style="transform:scale(.3);";kalimatb.style="transform:scale(.3);";kalimatc.style="transform:scale(.3);";} 
  function animkata() {kalimat.style="transform:scale(1);";kalimatb.style="transform:scale(1);";kalimatc.style="transform:scale(1);";}
  
  function otomatis2() {befanimkata2();setTimeout(animkata2,700);} 
  function befanimkata2(){kalimat.style.opacity="0";kalimatb.style.opacity="0";kalimatc.style.opacity="0";} 
  function animkata2() {kalimat.innerHTML = kalimat2.innerHTML;kalimatb.innerHTML = kalimatb2.innerHTML;kalimatc.innerHTML = kalimatc2.innerHTML;kalimat.style.opacity="1";kalimatb.style.opacity="1";kalimatc.style.opacity="1";}

  function otomatis3() {befanimkata3();setTimeout(animkata3,700);} 
  function befanimkata3(){kalimat.style.opacity="0";kalimatb.style.opacity="0";kalimatc.style.opacity="0";} 
  function animkata3() {kalimat.innerHTML = kalimat3.innerHTML;kalimatb.innerHTML = kalimatb3.innerHTML;kalimatc.innerHTML = kalimatc3.innerHTML;kalimat.style.opacity="1";kalimatb.style.opacity="1";kalimatc.style.opacity="1";}
  
  function sbakhir(){Bn.style.display="none";setTimeout(stakhir,500);} function stakhir(){tmbl.innerHTML="💌 Kirim";Tombol.style="opacity:1;transform: scale(1)";ftom=5;fungsi=0;}
  
  async function diterima(){
      setInterval(createHeart,200);
      fthilang();ftganti=1;
      setTimeout(ftmuncul,400);
      wallpaper.style="transform: scale(1)";
      bq.style = "position:relative;opacity:1;visibility:visible;transform: scale(1);transition:all 1s ease;border-radius:var(--bingkai);margin-top:0;";
      Tombol.style="opacity:0;transform: scale(.1);";
      Content.style = "transition:all 1s ease;opacity:1;margin-top:7vh;";
      setTimeout(sbakhir,1000);otomatis3();
   }
  
  async function ditolak(){
  	if(fungsi==1){
  	Tombol.style="transition:all .3s ease;opacity:0";await swalst.fire({title: '' + kataditolak.innerHTML, timer: 2000, imageUrl: '' + stikerditolak.src,});tombol();
  	}
   }
   memulai();
   const body = document.querySelector("body");function createHeart() {const heart = document.createElement("div"); heart.className = "fas fa-heart"; heart.style.left = (Math.random() * 90)+"vw"; heart.style.animationDuration = (Math.random()*3)+2+"s"; body.appendChild(heart);} setInterval(function name(params) {var heartArr = document.querySelectorAll(".fa-heart"); if (heartArr.length > 100) {heartArr[0].remove()}},100);
</script>
<!-- Sampai Sini -->
</body>
</html>
