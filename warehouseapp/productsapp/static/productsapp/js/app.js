//
//app.js
//@ Author: Brian
//

var dvpproducts = document.getElementById("dvpproducts");
var dvnewproduct = document.getElementById("dvnew");
var dvsearch = document.getElementById("dvsearch");
var searchp = document.getElementById("searchp");
var filter = document.getElementById("filter");
var dvfilter = document.getElementById("dvfilter");
var searchrows = document.getElementById("searchrows");
var lblshow = document.getElementById("lblshow");
var txtmore = document.getElementById("txtmore");
var dvmore = document.getElementById("dvmore");
var dvresults = document.getElementById("dvresults");
var dbprogres = document.getElementById("dbprogres");
var txtdbproduct = document.getElementById("txtdbproduct");
var tblproducts = document.getElementById("tblproducts");
var dvsuppliers = document.getElementById("dvsuppliers");
var txtProductListSize = document.getElementById("txtProductListSize").value;
var tblsize;
var products = [];
var pproducts = [];
var categories = [];
var suppliers = [];
var filterrows = 50;
var pplist = 0;
var plist = 0;
var filtersearch = "all";
var done = 0;
var url1;
var url2 = "/productsapp/wproducts";
var dbdb = 0;
var dbppic = 0;
var supplierID = "supplierID"
var dbList1 = 0;

function sortCategories(dx) {
  return new Promise((resolve, reject) => {
    categories = mergeSortCat(categories, "categories", "categoryID");
    var dy = new Date();
    var d3 = dy - dx;
    console.log("categories: @"+d3, categories.length);
    dbprogres.value += 5;
    resolve(d3);
  });
}

function sortSuppliers(dx) {
  return new Promise((resolve, reject) => {
    suppliers = mergeSortSup(suppliers, supplierID);
    var dy = new Date();
    var d3 = dy - dx;
    console.log("suppliers: @"+d3, suppliers.length);
    dbprogres.value += 5;
    resolve(d3);
  });
}

async function csort() {
  var d1 = new Date();
  var p1 = sortCategories(d1);
  var pc = await p1;
  var dy = new Date();
  var d3 = dy - d1;
  console.log("csort: @"+d3, "pc: "+pc);
};

async function ssort() {
  var d1 = new Date();
  var p2 = sortSuppliers(d1);
  var ps = await p2;
  var dy = new Date();
  var d3 = dy - d1;
  console.log("ssort: @"+d3, ", ps: "+ps);
};

function init() {
  url1 = window.location.href;
  dbprogres.value = 5;
  var tr = tblproducts.getElementsByTagName("tr");
  tblsize = tr.length;
  console.log("@"+tblsize+"# url1: ", url1);
  searchp.oninput = function() {
  	var pfilter = searchp.value;
  	if(pfilter == "category"){
  		dvpproducts.style.display = "block";
      dvfilter.style.display = "block";
      filter.placeholder = "Enter categoryid: ";
      lblshow.innerHTML = "Categories: ";
      filtersearch = pfilter;
      dbproducts(categories, "Categories");
      dbprogres.value = 50;
      dvsuppliers.style.display = "none";
  	}
    if(pfilter == "supplier"){
  		dvpproducts.style.display = "block";
      dvfilter.style.display = "block";
      filter.placeholder = "Enter supplierid: ";
      lblshow.innerHTML = "Suppliers: ";
      filtersearch = pfilter;
      dbproducts(suppliers, "Suppliers");
      dbprogres.value = 70;
      dvsuppliers.style.display = "block"
  	}
  	if(pfilter == "newproduct"){
  		dvnewproduct.style.display = "block";
      dvpproducts.style.display = "none";
      dvfilter.style.display = "none";
      dbprogres.value = 80;
      dvsuppliers.style.display = "none";
  	}
  	else{
  		dvnewproduct.style.display = "none";
  	}
    if(pfilter == "allproducts"){
      dbprogres.value = 0;
  		dvnewproduct.style.display = "none";
      dvpproducts.style.display = "none";
      dvsuppliers.style.display = "none";
      dvmore.style.display = "none";
      dbprogres.style.display = "block";
      filter.placeholder = "Enter categoryid or supplierid";
      dvfilter.style.display = "none";
      dvsearch.style.display = "none";
      filtersearch = pfilter;
      var url3 = url1.split("/products");
      console.log("url3: "+url3[0], url3[1]);
      var url4 = url3[0]+url2;
      dbprogres.value += 5;
      //So, what are we fetching this time?
      var dbt1 = new Date();
      dbdb++;
      console.log(dbt1+" @dbdb: ", dbdb, url4);
      var db = fetch(url4).then((response) => {
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
        var dbl = db2json.length;
        dbprogres.value += 5;
        console.log("dblist: ", dbl);
        return(db2json)
      }).then((db2json) => {
        var d1 = new Date();
        products = [];
        categories = [];
        suppliers = [];
        var filter1 = db2json.filter(filterList);
        var d2 = new Date();
        var d3 = d2 - d1;
        dbprogres.value += 5;
        console.log("dbfilter: @"+d3, filter1.length);
        return filter1;
      }).then((filter1) => {
        var d1 = new Date();
        csort();
        ssort();
        dbprogres.value += 5;
        var d2 = new Date();
        var d3 = d2 - d1;
        dbList1 = filter1.length;
        txtProductListSize.value = dbList1;
        console.log("c, s sort: @"+d3+", dbList1: ", dbList1);
        return d1;
      }).then((d1) => {
        dbproducts(products, "All");
        dvfilter.style.display = "block";
        dvsearch.style.display = "block";
        dbprogres.value += 5;
        console.log("#done: @"+d1);
      }).catch((error) => {
        console.log("db: @", error);
        dvfilter.style.display = "block";
        dvsearch.style.display = "block";
        dvpproducts.style.display = "block";
        dbprogres.value = 53;
      }).finally(() => {
        var d2 = new Date();
        var d3 = d2 - dbt1;
        console.log(d2+", #d3 @"+d3+", dbdb: "+dbdb);
        dbprogres.value = 70;
      });
      var db2 = fetchSuppliers();
      console.log("@db1: ", db+", @db2: "+db2+", "+dbprogres.value);
  	}
  };

  searchrows.oninput = function () {
    filterrows = searchrows.valueAsNumber;
    var lbl = lblshow.innerHTML;
    var lbl2 = lbl.split(":");
    lblshow.innerHTML = lbl2[0]+": "+filterrows+" rows."
    txtmore.value = filterrows;
    dbprogres.value = filterrows;
  };

  console.log("#00 List size: ", plist);
  var productsTemp = JSON.parse(txtdbproduct.value);
  plist = productsTemp.length;
  txtProductListSize.value = plist;
  console.log("#01 List size: ", plist);
  var d1 = new Date();
  var filter1 = productsTemp.filter(filterList);
  var d1 = new Date();
  csort();
  ssort();
  fetchSuppliers();
  var d2 = new Date();
  var d3 = d2 - d1;
  console.log("#02 c, s sort: @"+d3, filter1.length);
  dbprogres.value += 5;
  console.log("# 03 ", d2);
}

function pproductlist () {
  var producttable;
  var tr;
  var td;
  var tdvalue;
  var loc;
  var strv;
  var obj;
  producttable = document.getElementById("tblproducts");
  tr = producttable.getElementsByTagName("tr");
  for(var i = 0; i < tr.length; i++){
    loc = tr[i].getElementsByTagName("td").length;
    td = tr[i].getElementsByTagName("td");
    if(td[0]){
      strv = '{"productid":"'+td[0].innerHTML+'", ';
      strv += '"productname":"'+td[1].innerHTML+'", ';
      strv += '"supplierid":"'+td[2].innerHTML+'", ';
      strv += '"categoryid":"'+td[3].innerHTML+'", ';
      strv += '"quantityperunit":"'+td[4].innerHTML+'", ';
      strv += '"unitprice":"'+td[5].innerHTML+'", ';
      strv += '"unitsinstock":"'+td[6].innerHTML+'", ';
      strv += '"unitsonorder":"'+td[7].innerHTML+'", ';
      strv += '"reorderlevel":"'+td[8].innerHTML+'", ';
      strv += '"discontinued":"'+td[9].innerHTML+'"}';
      obj = JSON.parse(strv);
      //console.log(obj.categoryid);
      pproducts.push(obj);
      //console.log(products[plist].supplierid);
      pplist++;
    }
  }
  console.log("##001 pList size: ", pplist);
}

function dbproducts (dbl, info) {
  var db2 = JSON.stringify(dbl);
  txtdbproduct.value = db2;
  displayResults(dbl, info);
  console.log(db2);
  //var db3 = JSON.parse(db2);
  //console.log(db3);
}

function categorylist (categoryid) {
  console.log(filtersearch, categoryid);
  var d1 = new Date();
  var producttable;
  var tr;
  var td;
  var tdvalue;
  var loc = 3;
  var found = 0;
  producttable = document.getElementById("tblproducts");
  tr = producttable.getElementsByTagName("tr");
  var trlength = tr.length;
  if (trlength > 50){
    tblsize = trlength;
    console.log("tblsize: ", tblsize);
    return trlength;
  }
  for(var i = 0; i < trlength; i++){
    td = tr[i].getElementsByTagName("td")[loc];
    if(td){
      tdvalue = td.innerHTML;
      if (tdvalue == categoryid) {
        tr[i].style.display = "";
        found++;
      }
      else {
        tr[i].style.display = "none";
      }
    }
  }
  console.log("category list: "+found+"/", trlength);
  var d2 = new Date();
  var d3 = d2 - d1;
  console.log(filtersearch, categoryid+": "+d3+"@");
}

function supplierlist (supplierid) {
  console.log(filtersearch, supplierid);
  var d1 = new Date();
  var producttable;
  var tr;
  var td;
  var tdvalue;
  var loc = 2;
  var found = 0;
  producttable = document.getElementById("tblproducts");
  tr = producttable.getElementsByTagName("tr");
  var trlength = tr.length;
  if (trlength > 50){
    tblsize = trlength;
    console.log("tblsize: ", tblsize);
    return trlength;
  }
  for(var i = 0; i < trlength; i++){
    td = tr[i].getElementsByTagName("td")[loc];
    if(td){
      tdvalue = td.innerHTML;
      if (tdvalue == supplierid) {
        tr[i].style.display = "";
        found++;
      }
      else {
        tr[i].style.display = "none";
      }
    }
  }
  console.log("supplier list: "+found+"/", trlength);
  var d2 = new Date();
  var d3 = d2 - d1;
  console.log(filtersearch, supplierid+": "+d3+"@");
}

function productFilterT(x, y){
  filter.value = x;
  filtersearch = y;
  productfilter();
}

function productfilter(){
  var pfilter = filter.value;
  var filter1
  var filter2
  console.log(pfilter);
  done = 1;
  if (filtersearch == "category") {
    filterCategories(pfilter);
    if (tblsize <= 50){
      categorylist (pfilter);
    }
  }
  else if (filtersearch == "supplier") {
    filterSuppliers(pfilter);
    if (tblsize <= 50){
      supplierlist(pfilter);
    }
  }
  filter.value = "";
}

function showall () {
  var producttable;
  var tr;
  var td;
  var tdvalue;
  var loc = 2;
  var found = 0;
  producttable = document.getElementById("tblproducts");
  tr = producttable.getElementsByTagName("tr");
  var trlength = tr.length;
  for(var i = 0; i < trlength; i++){
    tr[i].style.display = "";
    found++;
  }
  console.log("all list: "+found+"/", trlength);
}

function filterList(cslist){
  console.log("filterList: ", cslist);
  products.push(cslist);
  suppliers.push(cslist);
  categories.push(cslist);
  return cslist;
}

function filterCategories(xy){
  var bs = binarySearchCat(xy, categories, "categories", "categoryID");
  console.log("filterCategories, bs: "+xy, bs);
  dvresults.innerHTML = bs;
  if (bs > -1) {
    wmsFilterCat(categories, bs, "categories", "categoryID", xy, txtdbproduct);
  }
}

function filterSuppliers(xy){
  var xyy = document.getElementById("txtProductListSize").value;
  var yx = document.getElementById("txtSuppliersListSize").value;
  var bs2 = 0;
  if ( yx < xyy) {
    var bs2 = binarySearchSup(xy, suppliers, supplierID);
    var bs1 = 0;
    if (bs2 > -1) {
      bs1 = binarySearchSup(xy, suppliers, supplierID);
      dvresults.innerHTML = bs1;
      wmsFilterSup(suppliers, bs1, supplierID, xy, txtdbproduct);
    }
    console.log("filterSuppliers bs: "+xy, bs2, bs1);
  }
  else {
    filterSuppliers2(xy)
  }
}

function filterSuppliers2(xy){
  var bs1 = binarySearchSup(xy, suppliers, supplierID);
  var bs2 = 0
  if (bs1 > -1) {
    dvresults.innerHTML = bs1;
    wmsFilterSup(suppliers, bs1, supplierID, xy, txtdbproduct);
    bs2 = displaySuppliers(xy)
  }
  console.log("filterSuppliers bs: "+xy, bs2, bs1);
}

function productInfo(pinfo){
  console.log("@# pinfo: "+pinfo);
}

window.onload = function () {
  init();
}
