"use strict";
const apiUrl = "http://localhost:5000/api/";
let year = 2020;
let month = 3;
const month_name = ["All", "January","February","March","April","May","June","July",
    "August","September","October","November","December"];
const years = [2020]



// navigation and page loading functions

function changePage(newPage) {
    const pages = document.querySelectorAll("main > div");
    pages.forEach(function (page) {
        page.classList.add("hidden");
    });
    document.getElementById(newPage).classList.remove("hidden");
}

function changeMonth(y, m) {
    changePage("page_month");
    document.querySelector("#page_month h1").textContent = m.toString() + " - " + y.toString();
    year = y;
    month = m;
    loadMonth();
}



// content loading
// load navigation
function loadAvailableYears() {
    // TODO load all the years in the navigation menu
}

function loadMonthNames() {
    // TODO load all the names of the month in the navigation menu
}

// load pages

function loadMonth() {
    // load income
    loadIncomeMonth();
    loadTransactionForm('#m-income-cat', 'm-income-from')
    // load expense
    loadExpenseMonth();
    loadTransactionForm('#m-expense-cat', 'm-expense-to')
}

// load page elements

function loadIncomeMonth() {
    fetch(apiUrl + 'income/' + year + "/" + month + "/", {
        headers: {contentType: 'application/json'},
    })
        .then(response => response.json())
        .then(data => fill_income_month_table(data))
        .catch((error) => console.error('Error:', error));
}

function loadExpenseMonth() {
    fetch(apiUrl + 'expense/' + year + "/" + month + "/", {
        headers: {contentType: 'application/json'},
    })
        .then(response => response.json())
        .then(data => fill_expense_month_table(data))
        .catch((error) => console.error('Error:', error));
}


// load tables

function load_transaction_table(data, selector) {
    console.log(data)
    document.querySelector(selector).innerHTML = ""
    data.forEach(function (transactions) {
        document.querySelector(selector).innerHTML += '<tr><td>' + transactions.day + '</td>'
            + '<td>' + transactions.contact + '</td><td>' + transactions.description + '</td><td>' + transactions.value + '</td><td>'
            + transactions.category.name + '</td></tr>';
    })
}

function fill_income_month_table(data) {
    load_transaction_table(data, '#table-month-income tbody')
    // TODO test, if test ok remove code
    // document.querySelector('#table-month-income tbody').innerHTML = ""
    // data.forEach(function (transactions) {
    //     document.querySelector('#table-month-income tbody').innerHTML += '<tr><td>' + transactions.day + '</td>'
    //         + '<td>' + transactions.contact + '</td><td>' + transactions.description + '</td><td>' + transactions.value + '</td><td>'
    //         + transactions.category.name + '</td></tr>';
    // })
}

function fill_expense_month_table(data) {
    console.log("ready to fill transaction table")
    load_transaction_table(data, '#table-month-expense tbody')
    // TODO test, if test ok remove code
    // document.querySelector('#table-month-expense tbody').innerHTML = ""
    // data.forEach(function (transaction) {
    //     document.querySelector('#table-month-expense tbody').innerHTML += '<tr><td>' + transaction.day + '</td>'
    //         + '<td>' + transaction.contact + '</td><td>' + transaction.description + '</td><td>' + transaction.value + '</td><td>'
    //         + transaction.category.name + '</td></tr>';
    // })
}


// load forms

function loadTransactionForm(category_selector, contact_selector) {
    // fetch categories
    fetch(apiUrl + 'category/all/', {
        headers: {contentType: 'application/json'}
    })
        .then((response) => response.json())
        .then(data => {
            document.querySelector(category_selector).innerHTML = ""
            data.forEach(function (category) {
                document.querySelector(category_selector).innerHTML += "<option>" + category.name + "</option>"
            })
        })
        .catch((error) => console.error('Error:', error));

    // fetch contacts
    fetch(apiUrl + 'contact/all/', {
        headers: {contentType: 'application/json'}
    })
        .then((response) => response.json())
        .then(data => { autocomplete(document.getElementById(contact_selector), data); })
        .catch((error) => console.error('Error:', error));
}



// Submit Forms

function submit_add_category(event) {
    event.preventDefault()
    fetch(apiUrl + 'category/', {
        headers: {contentType: "application/json"},
        method: 'POST',
        body: JSON.stringify({name: document.querySelector('#form-add-category #name').value})
    })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}

function submit_add_m_income(event) {
    event.preventDefault()
    fetch(apiUrl + 'income/' + year + '/' + month + '/', {
        headers: {contentType: "application/json"},
        method: 'POST',
        body: JSON.stringify({
            day: document.querySelector('#m-income-day').value,
            category: document.querySelector('#m-income-cat').value,
            contact: document.querySelector('#m-income-from').value,
            description: document.querySelector('#m-income-desc').value,
            value: document.querySelector('#m-income-val').value,
        })
    })
        .then(response => response.json())
        .then(data => {
            fill_income_month_table(data);
        })
        .catch((error) => console.error('Error:', error));
}

function submit_add_m_expense(event) {
    event.preventDefault()
    fetch(apiUrl + 'expense/' + year + "/" + month + "/", {
        headers: {contentType: 'application/json'},
        method: 'POST',
        body: JSON.stringify({
            day: document.querySelector('#m-expense-day').value,
            category: document.querySelector('#m-expense-cat').value,
            contact: document.querySelector('#m-expense-to').value,
            description: document.querySelector('#m-expense-desc').value,
            value: document.querySelector('#m-expense-val').value,
        })
    })
        .then(response => response.json())
        .then(data => {
            fill_expense_month_table(data);
        })
        .catch((error) => console.error('Error:', error));
}

// onload event listeners

window.onload = function () {
    // forms submit buttons
    document.querySelector('#form-add-category button[type="submit"]')
        .addEventListener("click", submit_add_category, false);
    document.querySelector('#form-add-m-income button[type="submit"]')
        .addEventListener("click", submit_add_m_income, false);
    document.querySelector('#form-add-m-expense button[type="submit"]')
        .addEventListener("click", submit_add_m_expense, false);
};


// autocomplete code

function autocomplete(inp, arr) {
    /*the autocomplete function takes two arguments,
    the text field element and an array of possible autocompleted values:*/
    let currentFocus;
    /*execute a function when someone writes in the text field:*/
    inp.addEventListener("input", function (e) {
        let a, b, i, val = this.value;
        /*close any already open lists of autocompleted values*/
        closeAllLists();
        if (!val) {
            return false;
        }
        currentFocus = -1;
        /*create a DIV element that will contain the items (values):*/
        a = document.createElement("DIV");
        a.setAttribute("id", this.id + "autocomplete-list");
        a.setAttribute("class", "autocomplete-items");
        /*append the DIV element as a child of the autocomplete container:*/
        this.parentNode.appendChild(a);
        /*for each item in the array...*/
        for (i = 0; i < arr.length; i++) {
            /*check if the item starts with the same letters as the text field value:*/
            if (arr[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
                /*create a DIV element for each matching element:*/
                b = document.createElement("DIV");
                /*make the matching letters bold:*/
                b.innerHTML = "<strong>" + arr[i].substr(0, val.length) + "</strong>";
                b.innerHTML += arr[i].substr(val.length);
                /*insert a input field that will hold the current array item's value:*/
                b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
                /*execute a function when someone clicks on the item value (DIV element):*/
                b.addEventListener("click", function (e) {
                    /*insert the value for the autocomplete text field:*/
                    inp.value = this.getElementsByTagName("input")[0].value;
                    /*close the list of autocompleted values,
                    (or any other open lists of autocompleted values:*/
                    closeAllLists();
                });
                a.appendChild(b);
            }
        }
    });
    /*execute a function presses a key on the keyboard:*/
    inp.addEventListener("keydown", function (e) {
        let x = document.getElementById(this.id + "autocomplete-list");
        if (x) x = x.getElementsByTagName("div");
        if (e.keyCode == 40) {
            /*If the arrow DOWN key is pressed,
            increase the currentFocus variable:*/
            currentFocus++;
            /*and and make the current item more visible:*/
            addActive(x);
        } else if (e.keyCode == 38) { //up
            /*If the arrow UP key is pressed,
            decrease the currentFocus variable:*/
            currentFocus--;
            /*and and make the current item more visible:*/
            addActive(x);
        } else if (e.keyCode == 13) {
            /*If the ENTER key is pressed, prevent the form from being submitted,*/
            e.preventDefault();
            if (currentFocus > -1) {
                /*and simulate a click on the "active" item:*/
                if (x) x[currentFocus].click();
            }
        }
    });

    function addActive(x) {
        /*a function to classify an item as "active":*/
        if (!x) return false;
        /*start by removing the "active" class on all items:*/
        removeActive(x);
        if (currentFocus >= x.length) currentFocus = 0;
        if (currentFocus < 0) currentFocus = (x.length - 1);
        /*add class "autocomplete-active":*/
        x[currentFocus].classList.add("autocomplete-active");
    }

    function removeActive(x) {
        /*a function to remove the "active" class from all autocomplete items:*/
        for (let i = 0; i < x.length; i++) {
            x[i].classList.remove("autocomplete-active");
        }
    }

    function closeAllLists(elmnt) {
        /*close all autocomplete lists in the document,
        except the one passed as an argument:*/
        let x = document.getElementsByClassName("autocomplete-items");
        for (let i = 0; i < x.length; i++) {
            if (elmnt != x[i] && elmnt != inp) {
                x[i].parentNode.removeChild(x[i]);
            }
        }
    }

    /*execute a function when someone clicks in the document:*/
    document.addEventListener("click", function (e) {
        closeAllLists(e.target);
    });
}