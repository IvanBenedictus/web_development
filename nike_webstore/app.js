// Product List
const products = [
    {
        id: 1,
        title: "Air Force",
        price: 119,
        colors: [
            {
                code: "#000000",
                img: "./img/air.png",
            },
            {
                code: "#323f5a",
                img: "./img/air2.png",
            },
        ],
    },
    {
        id: 2,
        title: "Air Jordan",
        price: 149,
        colors: [
            {
                code: "#9d978e",
                img: "./img/jordan.png",
            },
            {
                code: "#07956c",
                img: "./img/jordan2.png",
            },
        ],
    },
    {
        id: 3,
        title: "Blazer",
        price: 109,
        colors: [
            {
                code: "lightgrey",
                img: "./img/blazer.png",
            },
            {
                code: "#07956c",
                img: "./img/blazer2.png",
            },
        ],
    },
    {
        id: 4,
        title: "Crater",
        price: 129,
        colors: [
            {
                code: "#000000",
                img: "./img/crater.png",
            },
            {
                code: "#ccd0d9",
                img: "./img/crater2.png",
            },
        ],
    },
    {
        id: 5,
        title: "Hippie",
        price: 99,
        colors: [
            {
                code: "#000000",
                img: "./img/hippie2.png",
            },
            {
                code: "#ada7b1",
                img: "./img/hippie.png",
            },
        ],
    },
];

const wrapper = document.querySelector(".sliderWrapper");
const menuItems = document.querySelectorAll(".menuItem");
const currentProductImg = document.querySelector(".productImg");
const currentProductTitle = document.querySelector(".productTitle");
const currentProductPrice = document.querySelector(".productPrice");
const currentProductColors = document.querySelectorAll(".color");
const currentProductSizes = document.querySelectorAll(".size");

let choosenProduct = products[0];

// Changes for every menuItem selected
menuItems.forEach((item, index) => {
    item.addEventListener("click", () => {
        // Change the current slide
        wrapper.style.transform = `translateX(${-100 * index}vw)`;

        // Change the choosen product
        choosenProduct = products[index];

        // Change text, price and image of currentProduct in choosen product
        currentProductTitle.textContent = choosenProduct.title;
        currentProductPrice.textContent = "$" + choosenProduct.price;
        currentProductImg.src = choosenProduct.colors[0].img;

        // Change product image based on color for choosen product
        currentProductColors.forEach((color, index) => {
            color.style.backgroundColor = choosenProduct.colors[index].code;
        });
    });
});

// Change style of color box for choosen product
currentProductColors.forEach((color, index) => {
    color.addEventListener("click", () => {
        currentProductColors.forEach((color) => {
            color.style.border = "none";
        })
        color.style.border = "2px solid" + choosenProduct.colors[index].code;
        currentProductImg.src = choosenProduct.colors[index].img;
    });
});

// Change style of size box for choosen produc
currentProductSizes.forEach((size) => {
    size.addEventListener("click", () => {
        currentProductSizes.forEach((size) => {
            size.style.backgroundColor = "white";
            size.style.color = "black";
        });
        size.style.backgroundColor = "black";
        size.style.color = "white";
    });
});

const productButton = document.querySelector(".productButton");
const payment = document.querySelector(".payment");
const close = document.querySelector(".close");

// Diplay payment page
productButton.addEventListener("click", () => {
    payment.style.display = "flex";
});

// Close payment page
close.addEventListener("click", () => {
    payment.style.display = "none";
});