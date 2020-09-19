//
//app.js
//@ Author: Brian
//

var txtsupplierid = document.getElementById("supplierID");
var txtcksupplierid = document.getElementById("cksupplierID");
var lblcksupplierid = document.getElementById("lblcksupplierID");
var btncksupplierid = document.getElementById("bntcksupplierID");
var cksdbprogres = document.getElementById("cksdbprogres");
var dvresults = document.getElementById("dvresults");

function init(){
  var sern = serialN();
  txtsupplierid.value = sern;
  var info = navigator.appName;
  console.log("info: "+info, sern);
}

function serialN(){
  var d2 = new Date();
  var y = d2.getFullYear();
  var m = d2.getMonth()+1;
  var mm = '0'+m;
  if(mm.length < 3){
    m = mm;
  }
  var d = d2.getDate();
  var dd = '0'+d;
  if(dd.length < 3){
    d = dd;
  }
  var h = d2.getHours();
  var hh = '0'+h;
  if(hh.length < 3){
    h = hh;
  }
  var n = d2.getMinutes();
  var nn = '0'+n;
  if(nn.length < 3){
    n = nn;
  }
  var s = d2.getSeconds();
  var ss = '0'+s;
  if('0'+s.length < 3){
    s = ss;
  }
  var c = d2.getMilliseconds();
  var mc = c%100;
  var ser = ' '+y+m+d+h+n+s+mc;
  var sern = ser.trim();
  var sernl = sern.length;
  var min = 20
  if (sernl < min){
    for(var i = sernl; i < min; i++){
      sern += '0';
    }
  }
  console.log("sern:", sern);
  return sern;
}

function checkSuppliers(){
  var dy = new Date();
  var cks = txtcksupplierid.value;
  cks = cks.trim();
  var cksl = cks.length;
  console.log(dy+" checkProduct: "+cks, cksl);
  cksdbprogres.value = 15;
  if(cksl > 0){
    var url1s = window.location.href;
    var url3s = url1s.split("/suppliers");
    var url2cs = "/suppliersapp/checksuppliers?pid="+cks;
    var url4s = url3s[0]+url2cs;
    console.log("url4s: "+url4s);
    dvresults.innerHTML = ''
    var db = fetch(url4s).then((response) => {
      console.log("response: "+response);
      cksdbprogres.value += 5;
      return response.text();
    }).then((dblist) => {
      var d1 = JSON.stringify(dblist);
      var db2 = JSON.parse(dblist);
      console.log("db: ", db2);
      cksdbprogres.value += 5;
      return db2;
    }).then((db2) => {
      console.log("db: ", db2);
      cksdbprogres.value += 59;
      var rslt = "supplierID: "+db2[0]["supplierID"]+"<br>";
      rslt += "companyName: "+db2[0]["companyName"]+"<br>";
      rslt += "contactName: "+db2[0]["contactName"]+"<br>";
      rslt += "homePage: "+db2[0].homePage+"<br>";
      rslt += "city: "+db2[0].city+"<br>";
      rslt += "region: "+db2[0].region+"<br>";
      rslt += "<b>...................</b><br>";
      rslt += "<b>.................</b><br>";
      dvresults.innerHTML = rslt;
    }).catch((error) => {
      console.log("db: @", error);
      cksdbprogres.value = 3;
    }).finally(() => {
      var d2 = new Date();
      var d3 = d2 - dy;
      console.log(d2+"# db: ", db,", @"+d3);
      cksdbprogres.value = 70;
    });
  }
  else {
    cksdbprogres.value = 5;
    lblcksupplierid.innerHTML = "#"+cksl+": "+dy;
    txtcksupplierid.placeholder = "Enter productid: "
  }
  console.log("#checkSuppliers: "+cks+" "+cksl+": "+dy)
}

window.onload = function () {
  init();
}
