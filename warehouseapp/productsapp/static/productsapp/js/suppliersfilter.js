//
//suppliersfilter.js
//@ Author: Brian
//

var dvresults2 = document.getElementById("dvresults2");
var txtSuppliersListSize = document.getElementById("txtSuppliersListSize");
var dbsuppliers2 = [];
var dbList2 = 0;
var dbdb2 = 0;
var dbt2;

function sortSuppliers2(dx) {
  return new Promise((resolve, reject) => {
    dbsuppliers2 = mergeSortSup(dbsuppliers2, "supplierID");
    var dy = new Date();
    var d3 = dy - dx;
    console.log("dbsuppliers2: @"+d3, dbsuppliers2.length);
    dbprogres.value += 15;
    resolve(d3);
  });
}

function displaySuppliers(dy){
  var mid = binarySearchSup(dy, dbsuppliers2, "supplierID");
  dvresults2.innerHTML = "<h1>"+mid+"</h1>"
  if (mid > -1){
    var dvsuppliers2 = document.getElementById("dvsuppliers");
    var rslt = "<h1>"+mid+"</h1>";
    rslt += "#"+dbdb2+"<br>"
    rslt += "@"+dbt2+"<br>"
    rslt += "supplierID: "+dbsuppliers2[mid]["supplierID"]+"<br>";
    rslt += "companyName: "+dbsuppliers2[mid]["companyName"]+"<br>"
    rslt += "contactName: "+dbsuppliers2[mid]["contactName"]+"<br>";
    rslt += "contactTitle: "+dbsuppliers2[mid]["contactTitle"]+"<br>";
    rslt += "address: "+dbsuppliers2[mid]["address"]+"<br>"
    rslt += "city: "+dbsuppliers2[mid]["city"]+"<br>";
    rslt += "region: "+dbsuppliers2[mid]["region"]+"<br>";
    rslt += "postalCode: "+dbsuppliers2[mid]["postalCode"]+"<br>"
    rslt += "country: "+dbsuppliers2[mid]["country"]+"<br>";
    rslt += "phone: "+dbsuppliers2[mid]["phone"]+"<br>";
    rslt += "fax: "+dbsuppliers2[mid]["fax"]+"<br>"
    rslt += "homePage: "+dbsuppliers2[mid]["homePage"]+"<br>";
    dvresults2.innerHTML = rslt;
    dvsuppliers2.style.display = "block"
  }
  return mid;
}

function filterList2(cslist){
  console.log("filterList: ", cslist);
  dbsuppliers2.push(cslist);
  return cslist;
}

function fetchSuppliers(){
  var url0 = window.location.href;
  var url5 = "/suppliersapp/wsuppliers"
  var url6 = url0.split("/products");
  var url7 = url6[0]+url5;
  dbprogres.value += 5;
  //So, what are we fetching this time?
  dbt2 = new Date();
  dbdb2++;
  var db = fetch(url7).then((response) => {
      console.log("db: "+db, response);
      dbprogres.value += 5;
      return response.text();
    }).then((dblist) => {
      var d1 = JSON.stringify(dblist);
      var db2 = JSON.parse(dblist);
      console.log("db: ", db2);
      dbprogres.value += 5;
      return db2;
    }).then((db2json) => {
      var d1 = new Date();
      dbsuppliers2 = [];
      var filter2 = db2json.filter(filterList2);
      var d2 = new Date();
      var d3 = d2 - d1;
      dbprogres.value += 5;
      dbList2 = filter2.length
      txtSuppliersListSize.value = dbList2;
      console.log("dbfilter2: @"+d3+", dbList2: "+dbList2);
      return filter2;
    }).then((filter2) => {
      var d1 = new Date();
      var dd = sortSuppliers2(d1);
      dbprogres.value += 5;
      var d2 = new Date();
      var d3 = d2 - d1;
      console.log("s sort: @"+d3, filter2.length, dd);
    }).catch((error) => {
      console.log("db2: @", error);
      dbprogres.value = 30;
    }).finally(() => {
      var d2 = new Date();
      var d3 = d2 - dbt2;
      console.log(d2+"# d3 @"+d3+", #dbdb2: "+dbdb2);
      dbprogres.value = 95;
    });
    console.log("db: ", db+", "+dbprogres.value);
}
