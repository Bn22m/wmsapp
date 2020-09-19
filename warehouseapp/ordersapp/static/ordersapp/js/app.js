//
//app.js
//@ Author: Brian
//

var txtorderid = document.getElementById("orderID");
var txtckordersid = document.getElementById("cksorders");
var lblckproductid = document.getElementById("lblckorders");
var ckodbprogres = document.getElementById("ckodbprogres");
var dvresults = document.getElementById("dvresults");
var txtproductid = document.getElementById("productID");
var txtunitprice = document.getElementById("unitPrice");
var txtquantity = document.getElementById("quantity");

function init(){
  var sern = serialN();
  txtorderid.value = sern;
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

function checkOrders(){
  var dy = new Date();
  var ckp = txtckordersid.value;
  ckp = ckp.trim();
  var ckpl = ckp.length;
  console.log(dy+" checkOrders: "+ckp, ckpl);
  ckodbprogres.value = 15;
  if(ckpl > 0){
    var url1p = window.location.href;
    var url3p = url1p.split("/orders");
    var url2cp = "/productsapp/checkproducts?pid="+ckp;
    var url4p = url3p[0]+url2cp;
    console.log("url4p: "+url4p);
    dvresults.innerHTML = ''
    var db = fetch(url4p).then((response) => {
      console.log("db: "+db, response);
      ckodbprogres.value += 5;
      return response.text();
    }).then((dblist) => {
      var d1 = JSON.stringify(dblist);
      var db2 = JSON.parse(dblist);
      console.log("db: ", db2);
      ckodbprogres.value += 5;
      return db2;
    }).then((db2) => {
      console.log("db: "+db2);
      ckodbprogres.value += 59;
      var rslt = "productID: "+db2[0]["productID"]+"<br>";
      rslt += "productName: "+db2[0]["productName"]+"<br>"
      rslt += "supplierID: "+db2[0]["supplierID"]+"<br>";
      rslt += "categoryID: "+db2[0]["categories"]["categoryID"]+"<br>";
      rslt += "quantityPerUnit: "+db2[0]["quantityPerUnit"]+"<br>"
      rslt += "unitPrice: "+db2[0]["unitPrice"]+"<br>";
      rslt += "unitsInStock: "+db2[0]["unitsInStock"]+"<br>";
      rslt += "unitsOnOrder: "+db2[0]["unitsOnOrder"]+"<br>";
      rslt += "reorderLevel: "+db2[0]["reorderLevel"]+"<br>"
      rslt += "discontinued: "+db2[0]["discontinued"]+"<br>";
      dvresults.innerHTML = rslt;
      products(db2);
    }).catch((error) => {
      console.log("db: @", error);
      ckodbprogres.value = 3;
    }).finally(() => {
      var d2 = new Date();
      var d3 = d2 - dy;
      console.log(d2+"# db: ", db,", @"+d3);
      ckodbprogres.value = 70;
    });
  }
  else {
    ckodbprogres.value = 5;
    lblckordersid.innerHTML = "#"+ckpl+": "+dy;
    txtckordersid.placeholder = "Enter productid: "
  }
  console.log("#checkOrders: "+ckp+" "+ckpl+": "+dy)
}

function products(db2){
  console.log(db2);
  txtproductid.value = db2[0]["productID"];
  txtunitprice.value = db2[0]["unitPrice"];
}

window.onload = function () {
  init();
}
