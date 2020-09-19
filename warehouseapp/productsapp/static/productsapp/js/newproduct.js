//
//newproduct.js
//@ Author: Brian
//
//

var txtproductid = document.getElementById("productID");
var txtpcategoryid = document.getElementById("pcategoryID");
var txtcategoryid = document.getElementById("categoryID");
var txtpicture = document.getElementById("picture");
var txtckproductid = document.getElementById("ckproductID");
var lblckproductid = document.getElementById("lblckproductID");
var btnckproductid = document.getElementById("bntckproductID");
var ckpdbprogres = document.getElementById("ckpdbprogres");
var dvresults = document.getElementById("dvresults");

function init(){
  var dx = new Date();
  var s1 = serialN();
  var s11 = new Number(s1);
  var s2 = 'd'+s11;
  var s3 = ' ';
  var s3c;
  txtproductid.value = s1;
  txtcategoryid.oninput = function(){
    txtpcategoryid.value = categoryid.value;
    txtpicture.value = txtcategoryid.value+".jpg";
  }
  txtckproductid.oninput = function(){
    lblckproductid.innerHTML = txtckproductid.value;
  }
  for(var i = s2.length-1; i > 0; i--){
    s3c = s2.charCodeAt(i);
    console.log(i, s2[i], s3c);
    s3 += s3c;
  }
  var s4 = s3.trim();
  var s5 = parseInt(s4);
  txtcategoryid.value = s4;
  txtpcategoryid.value = txtcategoryid.value;
  txtpicture.value = txtcategoryid.value+".jpg";
  var info = navigator.appName;
  var infov = navigator.appVersion;
  console.log("s1 : "+s1, ", s2: "+s2, ", s4: "+s4, "s4 len: "+s4.length, ", s5: "+s5);
  var dy = new Date();
  var dt = dy - dx;
  console.log("dt: @",dt, info, infov, parseInt(s1), parseInt(s4));
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

function checkProduct(){
  var dy = new Date();
  var ckp = txtckproductid.value;
  ckp = ckp.trim();
  var ckpl = ckp.length;
  console.log(dy+" checkProduct: "+ckp, ckpl);
  ckpdbprogres.value = 15;
  if(ckpl > 0){
    var url1p = window.location.href;
    var url3p = url1p.split("/products");
    var url2cp = "/productsapp/checkproducts?pid="+ckp;
    var url4p = url3p[0]+url2cp;
    console.log("url4p: "+url4p);
    dvresults.innerHTML = ''
    var db = fetch(url4p).then((response) => {
      console.log("db: "+db, response);
      ckpdbprogres.value += 5;
      return response.text();
    }).then((dblist) => {
      var d1 = JSON.stringify(dblist);
      var db2 = JSON.parse(dblist);
      console.log("db: ", db2);
      ckpdbprogres.value += 59;
      var rslt = "productID: "+db2[0]["productID"]+"<br>";
      rslt += "supplierID: "+db2[0]["supplierID"]+"<br>";
      rslt += "categoryID: "+db2[0]["categories"]["categoryID"]+"<br>";
      rslt += "categoryName: "+db2[0]["categories"]["categoryName"]+"<br>"
      rslt += "description: "+db2[0]["categories"]["description"]+"<br>";
      dvresults.innerHTML = rslt;
      return db2;
    }).catch((error) => {
      console.log("db: @", error);
      ckpdbprogres.value = 3;
    }).finally(() => {
      var d2 = new Date();
      var d3 = d2 - dy;
      console.log(d2+"# db: ", db,", @"+d3);
      ckpdbprogres.value = 70;
    });
  }
  else {
    ckpdbprogres.value = 5;
    lblckproductid.innerHTML = "#"+ckpl+": "+dy;
    txtckproductid.placeholder = "Enter productid: "
  }
  console.log("#checkProduct: "+ckp+" "+ckpl+": "+dy)
}

window.onload = function () {
  init();
}
